import requests


class Team:
    def __init__(self) -> None:
        pass


class Event(object):
    def __init__(self) -> None:
        pass


class Boxscore(object):
    def __init__(self) -> None:
        pass


def get_scoreboard(sport: str, league: str, date: str):
    """
    returns a json object of the scoreboard
    sport: str - the sport you want to get the scoreboard for (baseball, football, basketball, hockey)
    league: str - the league you want to get the scoreboard for (mlb, nfl, nba  , nhl)
    date: str - the date you want to get the scoreboard for in the format YYYYMMDD
    """

    data: requests.Response = requests.get(
        f"https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/scoreboard?dates={date}"
    )
    if data.status_code == 200:
        return data.json()
    return {}
