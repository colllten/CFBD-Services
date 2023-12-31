import cfbd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from dotenv import load_dotenv

load_dotenv()

# Set up CFBD API
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = os.getenv("CFBD_API_KEY")
configuration.api_key_prefix['Authorization'] = 'Bearer'

# Set up Firebase API
cred = credentials.Certificate("b1g-fantasy-football-firebase-adminsdk-yg8ju-73d5d2b292.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

offensive_positions = ["QB", "RB", "WR", "PK", "P", "TE"]


def main():
    upload_b1g_rosters(2023)


def upload_b1g_rosters(year: int):
    # Get all teams in B1G
    b1g_teams = get_teams_in_conference(conference="B1G")

    # Get all B1G team names
    b1g_names = []
    for team in b1g_teams:
        b1g_names.append(team.school)

    # Go through each team's roster and get only offensive players
    for team_name in b1g_names:
        team_roster = get_team_roster(team=team_name, year=year)

        # Filter the roster to only offensive positions
        offensive_team_roster = get_offensive_players_from_roster(roster=team_roster)

        # Write each player to Firebase
        print(f"Writing {team_name}'s players...")
        for player in offensive_team_roster:
            player = convert_player_to_map(player)
            db.collection(f"{year}_PLAYERS").document(str(player["id"])).set(player)
        print("All B1G offensive players have been written to Firestore!")


def get_teams_in_conference(conference: str) -> [cfbd.Team]:
    teams_api = cfbd.TeamsApi(cfbd.ApiClient(configuration))

    teams = teams_api.get_teams(conference=conference)
    if len(teams) == 0:
        raise Exception(f"invalid conference ({conference})")
    else:
        return teams


def get_team_roster(team: str, year: int) -> [cfbd.Player]:
    # Get Teams API that will be used to get a team's roster
    teams_api = cfbd.TeamsApi(cfbd.ApiClient(configuration))
    # Roster of desired team and year
    roster = teams_api.get_roster(team=team, year=year)
    # Check if roster was filled
    if len(roster) == 0:
        raise Exception(f"team parameter ({team}) or year parameter ({year}) incorrect")
    else:
        return roster


def get_offensive_players_from_roster(roster: [cfbd.Player]) -> [cfbd.Player]:
    offensive_players = []
    for player in roster:
        if player.position in offensive_positions:
            offensive_players.append(player)
    return offensive_players


def convert_player_to_map(player: cfbd.Player):
    player_map = {}
    player_map.update({"id": player.id})
    player_map.update({"first_name": player.first_name})
    player_map.update({"last_name": player.last_name})
    player_map.update({"team": player.team})
    player_map.update({"height": player.height})
    player_map.update({"weight": player.weight})
    player_map.update({"jersey": player.jersey})
    player_map.update({"position": player.position})
    return player_map



if __name__ == "__main__":
    main()
