import requests
import utils
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")

# BASE_URL = "https://api.football-data.org" # not working atm


class ApiClient(object):

    def get_competitions(self):
        response = requests.get(
            "https://api.football-data.org/v4/competitions/",
            headers={"X-Auth-Token": API_KEY},
        )
        if response.status_code == 200:
            names = utils.get_names(response.json())
            return names

