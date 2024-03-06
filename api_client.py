import requests
from dotenv import load_dotenv
import os
from datetime import date


load_dotenv()
API_KEY = os.getenv("API_KEY")


class ApiClient(object):

    def get_competitions(self):
        response = requests.get(
            "https://api.football-data.org/v4/competitions/",
            headers={"X-Auth-Token": API_KEY},
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "response_code": response.status_code,
                "message": "Could not return competitions. Please try again later.",
            }

    def get_current_season_info(self, league):
        response = requests.get(
            "https://api.football-data.org/v4/competitions/ % s" % league,
            headers={"X-Auth-Token": API_KEY},
        )

        if response.status_code == 200:
            return response.json()["currentSeason"]
        else:
            return {
                "response_code": response.status_code,
                "message": "Could not return % s matchday. Please try again later."
                % league,
            }

    def get_fixtures(self, league, season_info, matchday=None):
        payload = {}
        matchday = matchday
        end_date = season_info["endDate"]

        if matchday is not None:
            payload = {"matchday": matchday}
        else:
            today = date.today().strftime("%Y-%m-%d")
            payload = {"dateFrom": today, "dateTo": end_date}

        response = requests.get(
            "https://api.football-data.org/v4/competitions/ % s/matches" % league,
            headers={"X-Auth-Token": API_KEY},
            params=payload,
        )

        if response.status_code == 200:
            return response.json()
        else:
            return {
                "response_code": response.status_code,
                "message": "Could not return % s fixtures. Please try again later."
                % league,
            }

    def get_standings(self, league):
        response = requests.get(
            "https://api.football-data.org/v4/competitions/% s/standings" % league,
            headers={"X-Auth-Token": API_KEY},
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "response_code": response.status_code,
                "message": "Could not return % s standings. Please try again later."
                % league,
            }

    def get_top_scorers(self, league):
        response = requests.get(
            "https://api.football-data.org/v4/competitions/% s/scorers" % league,
            headers={"X-Auth-Token": API_KEY},
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "response_code": response.status_code,
                "message": "Could not return % s top scorers. Please try again later."
                % league,
            }

    def get_scores(self, team=None, live=False):
        payload = {"date": date.today().strftime("%Y-%m-%d")}

        if live is True:
            payload["live"] = live
        if team is not None:
            payload["team"] = team

        response = requests.get(
            "https://api.football-data.org/v4/matches",
            headers={"X-Auth-Token": API_KEY},
            params=payload,
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "response_code": response.status_code,
                "message": "Could not return scores. Please try again later.",
            }
