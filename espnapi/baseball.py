from typing import List
from espnapi import espnapi


class BaseballTeam(espnapi.Team):
    def __init__(self, data) -> None:
        super().__init__()
        self.rawdata = data


class BaseballBoxscore(espnapi.Team):
    def __init__(self, data) -> None:
        super().__init__()
        self.rawdata = data


class BaseballEvent(espnapi.Event):
    def __init__(self, data) -> None:
        super().__init__()
        # self.notes = data["notes"]
        self.boxscore = data["boxscore"]  # TODO - create boxscore class
        self.format = data["format"]
        self.gameInfo = data["gameInfo"]
        self.seasonseries = data["seasonseries"]
        self.rosters = data["rosters"]
        self.header = data["header"]
        self.plays = data["plays"]
        self.rawdata = data


def get_events(date="") -> List[BaseballEvent]:
    data = espnapi.get_scoreboard("baseball", "mlb", date)
    if data == {}:
        raise ValueError("No data found")
    return [BaseballEvent(e) for e in data["events"]]

    # self.displayName: str = data["team"]["displayName"]
    # self.shortName: str = data["team"]["shortDisplayName"]
    # self.abbreviation: str = data["team"]["abbreviation"]
    # self.location: str = data["team"]["location"]
    # self.name: str = data["team"]["name"]
    # self.score: int = data["score"]
    # self.id: int = data["id"]
    # self.uid: str = data["uid"]
    # self.homeAway: str = data["homeAway"]
    # self.record: str = data["records"][0]["summary"]
    # self.homeRecord: str = data["records"][1]["summary"]
    # self.awayRecord: str = data["records"][2]["summary"]
    # self.color: str = data["team"]["color"]
    # self.alternateColor: str = data["team"]["alternateColor"]

    # self.id: int = data["id"]
    # self.uid: str = data["uid"]
    # self.date: str = data["date"]
    # self.attendance: int = data["attendance"]
    # self.wasSuspended: bool = data["wasSuspended"]
    # self.neutralSite: bool = data["neutralSite"]
    # self.conferenceCompetition: bool = data["conferenceCompetition"]
    # self.homeTeam: BaseballTeam = BaseballTeam(
    # data["competitions"][0]["competitors"][0]
    # )
    # self.awayTeam: BaseballTeam = BaseballTeam(
    # data["competitions"][0]["competitors"][1]
    # )
    #     self.homeTeam: BaseballTeam = BaseballTeam(
    #         data["competitions"][0]["competitors"][0]
    #     )
    #     self.awayTeam: BaseballTeam = BaseballTeam(
    #         data["competitions"][0]["competitors"][1]
    #     )

    # def getWinner(self):
    #     return (
    #         self.homeTeam
    #         if self.homeTeam.score > self.awayTeam.score
    #         else self.awayTeam
    #     )
