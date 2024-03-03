import fire
import api_client
import pprint
from halo import Halo
from rich.console import Console


api = api_client.ApiClient()


class Competition(object):

    def competitions(self):
        r = api.get_competitions()
        pprint.pprint(r)

    # will return fixtures for specified matchday
    # or
    # will return fixtures for rest of season
    def fixtures(self, league, matchday=None):
        spinner = Halo(text='Loading', spinner='dots')
        spinner.start()

        current_season = api.get_current_season_info(league)
        r = api.get_fixtures(league, current_season, matchday)
    
        spinner.stop()
    
        pprint.pprint(r) # replace with beautify

    def standings(self, league):
        r = api.get_standings(league)
        console = Console()
        console.print(r) 

    def teams(self, league):
        return "Get teams in league"

    def top_scorers(self, league):
        return "Get top scoreres"


class Team(object):

    def get_team(self, team):
        return "Show {team}".format(team=team)


class Match(object):

    def get_team_matches(self, team):
        return "Get {team} matches".format(team=team)


class Player(object):

    def get_matches(self, player):
        return "Show matches for {player}".format(player=player)

    def get_player(self, player):
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
