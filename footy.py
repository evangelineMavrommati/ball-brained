import fire
import api_client
import pprint

api = api_client.ApiClient()


class Competition(object):

    def get_competitions(self):
        r = api.get_competitions()
        pprint.pprint(r)

    def list_fixtures(self, league):
        return "Get fixtures for {league}".format(league=league)

    def get_standings(self, league):
        return "Get competition \n Get Standings"

    def list_teams(self, league):
        return "Get teams in league"

    def get_top_scorers(self, league):
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


if __name__ == "__main__":
    fire.Fire(Footy)
