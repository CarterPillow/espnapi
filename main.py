from typing import List
from espnapi import baseball


def main():
    try:
        events: List[baseball.BaseballEvent] = baseball.get_events()
        for e in events:
            print(
                f"{e.away_team.name}({e.away_team.record}) @ {e.home_team.name}({e.home_Team.record})"
            )
    except ValueError:
        print("No data found")


if __name__ == "__main__":
    main()
