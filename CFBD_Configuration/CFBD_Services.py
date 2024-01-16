import cfbd
import os

from dotenv import load_dotenv
load_dotenv()

offensive_player_positions = ["QB", "RB", "WR", "PK", "P", "TE"]
def configure_cfbd():
    configuration = cfbd.Configuration()
    configuration.api_key["Authorization"] = os.getenv("CFBD_API_KEY")
    configuration.api_key_prefix["Authorization"] = "Bearer"
    return configuration

configuration = configure_cfbd()


def get_conferences() -> [cfbd.Conference]:
    conferences_api = cfbd.ConferencesApi(cfbd.ApiClient(configuration))
    conferences = conferences_api.get_conferences()
    return conferences
