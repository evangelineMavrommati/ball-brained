from datetime import datetime
from pytz import timezone
import json

# helper methods


def humanize_competition_names(response):
    rv = []
    for dict in response["competitions"]:
        rv.append(dict["name"])
    return rv


def humanize_fixture_info(response):
    rv = []
    matches = response["matches"]

    for dict in matches:
        fixture = dict["homeTeam"]["name"] + " vs " + dict["awayTeam"]["name"]

        utc = datetime.strptime(dict["utcDate"], "%Y-%m-%dT%H:%M:%S%z")
        when = utc.astimezone().strftime("%m-%d-%Y %H:%M")

        rv.append({"fixture": fixture, "when": when})

    return rv