from rich.table import Table


def beautify_competition_names(data):
    table = Table(title="Competitions")
    table.add_column("Name", style="magenta bold")
    table.add_column("Code", justify="right", style="cyan")

    for competition in data:
        table.add_row(competition["name"], competition["code"])

    return table


def create_standings_table(data):
    table = Table(title="Standings")
    table.add_column("Position", justify="right", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Points", justify="right", style="green")

    for team in data:
        table.add_row(str(team["position"]), team["team"], str(team["points"]))

    return table


def beautify_fixtures(data):
    table = Table(title="Fixtures")
    table.add_column("Fixture", style="magenta bold")
    if "matchday" in data[0]:
        table.add_column("Matchday", justify="right", style="cyan")
    table.add_column("When", justify="right", style="green")

    for fixture in data:
        if "matchday" in fixture:
            table.add_row(fixture["fixture"], str(fixture["matchday"]), fixture["when"])
        else:
            table.add_row(fixture["fixture"], fixture["when"])

    return table
