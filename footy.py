import fire
import api_client
import utils
import beautify
from halo import Halo
from rich.console import Console


api = api_client.ApiClient()

spinner = Halo(text="Loading", spinner="dots")
console = Console()


class Competition(object):

    def competitions(self):
        spinner.start()

        r = api.get_competitions()
        human_res = utils.humanize_competition_names(r)
        beautified = beautify.beautify_competition_names(human_res)

        spinner.stop()
        console.print(beautified)

    # will return fixtures for specified matchday
    # or
    # will return fixtures for rest of season
    def fixtures(self, league, matchday=None):
        spinner.start()

        current_season = api.get_current_season_info(league)
        r = api.get_fixtures(league, current_season, matchday)
        human_res = utils.humanize_fixture_info(r, matchday)
        beautified = beautify.beautify_fixtures(human_res)

        spinner.stop()
        console.print(beautified)

    def standings(self, league):
        spinner.start()

        r = api.get_standings(league)
        human_res = utils.humanize_standings(r)
        beautified = beautify.create_standings_table(human_res)

        spinner.stop()
        console.print(beautified)

    def top_scorers(self, league):
        spinner.start()

        r = api.get_top_scorers(league)
        human_res = utils.humanize_top_scorers(r)
        beautified = beautify.create_top_scorers_table(human_res)

        spinner.stop()
        console.print(beautified)


class Match(object):

    # will return matches for day of
    # optionally filter by live matches or team
    def scores(self, team=None, live=False):
        spinner.start()

        r = api.get_scores(team, live)
        human_res = utils.humanize_scores(team, live, r)
        if live:
            beautified = beautify.beautify_live(human_res)
        else:
            beautified = beautify.today_score_table(human_res)

        spinner.stop()
        console.print(beautified)


class Footy(object):

    def __init__(self):
        self.competition = Competition()
        self.match = Match()


def main():
    fire.Fire(Footy)


if __name__ == "__main__":
    main()
