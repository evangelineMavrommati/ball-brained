from datetime import datetime
from pytz import timezone
import beautify


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
