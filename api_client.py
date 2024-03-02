import requests
from dotenv import load_dotenv
import os
import sys

load_dotenv()

API_KEY = os.getenv("API_KEY")
# BASE_URL = "https://api.football-data.org" # not working atm


class ApiClient(object):

    def get_competitions(self):
        response = requests.get(
            "https://api.football-data.org/v4/competitions/PL",
            headers={"X-Auth-Token": API_KEY},
        )
        return response.json  # format this
