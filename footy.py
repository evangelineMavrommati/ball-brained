import fire
import api_client
import pprint
from halo import Halo
from rich.console import Console


api = api_client.ApiClient()

spinner = Halo(text="Loading", spinner="dots")
console = Console()


class Competition(object):

    def competitions(self):
        spinner.start()

        r = api.get_competitions()

        spinner.stop()
        console.print(r)

    # will return fixtures for specified matchday
    # or
    # will return fixtures for rest of season
    def fixtures(self, league, matchday=None):
        spinner.start()

        current_season = api.get_current_season_info(league)
        r = api.get_fixtures(league, current_season, matchday)

        spinner.stop()
        console.print(r)

    def standings(self, league):
        spinner.start()

        r = api.get_standings(league)

        spinner.stop()
        console.print(r)

    def teams(self, league):
        return "Get teams in league"

    def top_scorers(self, league):
        return "Get top scoreres"


class Team(object):

    def team(self, team):
        return "Show {team}".format(team=team)


class Match(object):

    def matches(self, team):
        return "Get {team} matches".format(team=team)


class Player(object):

    def matches(self, player):
        return "Show matches for {player}".format(player=player)

    def player(self, player):
        return "Show {player}".format(player=player)


class Footy(object):

    def __init__(self):
        self.competition = Competition()
        self.team = Team()
        self.match = Match()
        self.player = Player()


def main():
    fire.Fire(Footy)


if __name__ == "__main__":
    main()
