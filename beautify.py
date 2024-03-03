from rich.table import Table

def create_standings_table(dict):
    table = Table(title="Standings")
    table.add_column("Position", justify="right", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Points", justify="right", style="green")

    for team in dict:
        table.add_row(str(team["position"]), team["team"], str(team["points"]))

    return table

