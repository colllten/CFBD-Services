from cfbd.rest import ApiException
import cfbd
from CFBD_Configuration import CFBD_Services

configuration = CFBD_Services.configure_cfbd()


def get_players_stats(year: int, week: int, school: str):
    # Get API
    api = cfbd.GamesApi(cfbd.ApiClient(configuration))

    try:
        response = api.get_player_game_stats(year, week=week, team=school)
    except ApiException as e:
        print(f"Exception occurred getting player stats: {e}")
        return None

    # Get the only game stats in the array
    player_game = response[0]

    type_set = set()

    # Iterate through each team
    for team in player_game.teams:
        # Only look through stats of team requested in the parameter list
        if team.school == school:
            # Iterate through each category
            for category in team.categories:
                print(f"**CATEGORY: {category.name}")
                for type in category.types:
                    for athlete in type.athletes:
                        print(athlete.name)
