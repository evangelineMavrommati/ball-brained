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

    def top_scorers(self, league):
        spinner.start()

        r = api.get_top_scorers(league)

        spinner.stop()
        console.print(r)


class Match(object):

    # will return matches for day of
    # optionally filter by live matches or team
    def scores(self, team=None, live=False):
        # spinner.start()

        r = api.get_scores(team, live)

        # spinner.stop()
        console.print(r)


class Player(object):

    def matches(self, player):
        return "Show matches for {player}".format(player=player)

    def player(self, player):
        return "Show {player}".format(player=player)


class Footy(object):

    def __init__(self):
        self.competition = Competition()
        self.match = Match()
        self.player = Player()


def main():
    fire.Fire(Footy)


if __name__ == "__main__":
    main()
