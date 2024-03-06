from datetime import datetime
from pytz import timezone
import beautify
import pprint


def humanize_competition_names(response):
    rv = []
    for dict in response["competitions"]:
        rv.append({"name": dict["name"], "code": dict["code"]})

    return beautify.beautify_competition_names(rv)


def humanize_fixture_info(response, matchday):
    rv = []
    matches = response["matches"]

    for dict in matches:
        fixture = dict["homeTeam"]["name"] + " vs " + dict["awayTeam"]["name"]

        utc = datetime.strptime(dict["utcDate"], "%Y-%m-%dT%H:%M:%S%z")
        when = utc.astimezone().strftime("%m-%d-%Y %H:%M")

        rv.append({"fixture": fixture, "matchday": dict["matchday"], "when": when})

    return beautify.beautify_fixtures(rv)


def humanize_standings(response):
    rv = []
    standings = response["standings"][0]["table"]

    for dict in standings:
        rv.append(
            {
                "position": dict["position"],
                "team": dict["team"]["name"],
                "points": dict["points"],
            }
        )

    return beautify.create_standings_table(rv)


def humanize_top_scorers(response):
    rv = []
    scorers = response["scorers"]

    for dict in scorers:
        rv.append(
            {
                "player": dict["player"]["name"],
                "team": dict["team"]["name"],
                "nationality": dict["player"]["nationality"],
                "goals": dict["goals"],
                "assists": dict["assists"],
            }
        )

    return beautify.create_top_scorers_table(rv)


def fetch_league(e):
    e["league"]


# def filter_for_team(team, e):


# this needs to be refactored... 🤮
# currently only returns scores for games on day of
def humanize_scores(team, live, response):
    if response["resultSet"]["count"] == 0:
        return "No matches today."

    rv = []

    matches = response["matches"]

    for dict in matches:
        league = dict["competition"]["name"]
        home = dict["homeTeam"]["name"]
        away = dict["awayTeam"]["name"]

        if dict["status"] == "FINISHED" and live is False:
            score = "%s - %s" % (
                dict["score"]["fullTime"]["home"],
                dict["score"]["fullTime"]["away"],
            )
            rv.append({"league": league, "home": home, "away": away, "score": score})

        # probs needs to be fixed
        # do not know response shape for live fixture
        # if dict["status"] == "LIVE":
        #     score = (
        #         dict["score"]["fullTime"]["home"]
        #         + " - "
        #         + dict["score"]["fullTime"]["away"]
        #     )
        #     minute = 60  # stub -- what minute is it?
        #     rv.append(
        #         {
        #             "league": league,
        #             "fixture": fixture,
        #             "score": score,
        #             "minute": minute,
        #             "status": "LIVE",
        #         }
        #     )

    # rv.sort
    # rv.sort(key=fetch_league)
    rv.sort(key=lambda x: x["league"])
    return beautify.today_score_table(rv)
