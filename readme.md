WIP

CLI for ball-brained individuals

inspired by https://github.com/manrajgrover/football-cli

## How to use

```
python footy.py <command> <options>

Command
  competition
  match

python footy.py match scores --team="Napoli"
```

Options for `competition`

*Use `competitions` to get Leagues to pass as param to other options*

```
competitions
fixtures <league> <matchday>
standings <league>
top_scorers <league>
```

Options for `match`

```
scores <team> <live>
```
