from rich.table import Table
from rich import box


def beautify_competition_names(data):
    table = Table(title="Competitions", box=box.SIMPLE_HEAD)
    table.add_column("Name", style="magenta bold")
    table.add_column("Code", justify="right", style="cyan")

    for competition in data:
        table.add_row(competition["name"], competition["code"])

    return table


def create_standings_table(data):
    table = Table(title="Standings", box=box.SIMPLE_HEAD)
    table.add_column("Position", justify="right", style="cyan bold", no_wrap=True)
    table.add_column("Team", style="magenta bold")
    table.add_column("Points", justify="right", style="green")

    for team in data:
        table.add_row(str(team["position"]), team["team"], str(team["points"]))

    return table


def beautify_fixtures(data):
    table = Table(title="Fixtures", box=box.SIMPLE_HEAD)
    table.add_column("Home", style="magenta bold")
    table.add_column("", style="bright_red", ratio=1.5)
    table.add_column("Away", style="magenta bold")
    if "matchday" in data[0]:
        table.add_column("Matchday", justify="right", style="cyan")
    table.add_column("When", justify="right", style="green")

    for fixture in data:
        if "matchday" in fixture:
            table.add_row(
                fixture["home"],
                "vs",
                fixture["away"],
                str(fixture["matchday"]),
                fixture["when"],
            )
        else:
            table.add_row(fixture["home"], "vs", fixture["away"], fixture["when"])

    return table


def beautify_live(data):
    table = Table(title="Live Scores", box=box.SIMPLE_HEAD)
    table.add_column("League", style="cyan dim")
    table.add_column("Home", style="magenta bold")
    table.add_column("", style="bright_red", ratio=1.5)
    table.add_column("Away", style="magenta bold")
    table.add_column("Score", style="green bold")
    table.add_column("Status", style="cyan bold")

    for match in data:
        table.add_row(
            match["league"], match["home"], "vs", match["away"], match["score"], "LIVE"
        )

    return table


def create_top_scorers_table(data):
    table = Table(title="Top Scorers", box=box.SIMPLE_HEAD)
    table.add_column("Position", justify="right", style="cyan bold", no_wrap=True)
    table.add_column("Player", style="magenta bold")
    table.add_column("Team", style="cyan")
    table.add_column("Nationality", style="green")
    table.add_column("Goals", justify="right", style="bright_yellow")

    count = 1
    for player in data:
        table.add_row(
            str(count),
            player["player"],
            player["team"],
            player["nationality"],
            str(player["goals"]),
        )
        count += 1

    return table


def today_score_table(data):
    table = Table(title="Scores", box=box.SIMPLE_HEAD)
    table.add_column("League", style="cyan dim")
    table.add_column("Home", style="magenta bold")
    table.add_column("", style="bright_red", ratio=1.5)
    table.add_column("Away", style="magenta bold")
    table.add_column("FT", style="green bold")

    for match in data:
        table.add_row(
            match["league"],
            match["home"],
            "vs",
            match["away"],
            match["score"],
        )

    return table
