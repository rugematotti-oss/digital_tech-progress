from task03 import Athlete

class SoccerAthlete(Athlete):
    def __init__(self, name, country, birthdate, team, post):
        super().__init__(name, country, birthdate)

        if not isinstance(team, str) or not team.strip():
            raise ValueError("team must be a non-empty string")
        if not isinstance(post, str) or not post.strip():
            raise ValueError("post must be a non-empty string")

        self._team = team
        self._post = post

    def print(self):
        super().print()
        print(f"As a soccer player: I am a {self._post} at {self._team}.")

class FighterAthlete(Athlete):
    def __init__(self, name, country, birthdate, wins=0, draws=0, loss=0):
        super().__init__(name, country, birthdate)

        if not all(isinstance(x, int) and x >= 0 for x in [wins, draws, loss]):
            raise ValueError("wins, draws, loss must be integers >= 0")

        self._wins = wins
        self._draws = draws
        self._loss = loss

    def print(self):
        super().print()
        print(f"As a fighter athlete: I have {self._wins} wins, {self._draws} draws, {self._loss} loss.")

class MMAFighterAthlete(FighterAthlete):
    def __init__(self, name, country, birthdate, organizations, wins=0, draws=0, loss=0):
        super().__init__(name, country, birthdate, wins, draws, loss)

        if not isinstance(organizations, list) or not all(isinstance(o, str) for o in organizations):
            raise ValueError("organizations must be a list of strings")

        self._organizations = organizations

    def print(self):
        super(Athlete, self).print()  # skip Fighter print, use custom
        print(f"As a fighter athlete: I have {self._wins} wins, {self._draws} draws, {self._loss} loss and I fight MMA in the organizations")
        print(f"[{', '.join(self._organizations)}].")

s = SoccerAthlete("Leo", "Argentina", "1987-06-24", "Inter Miami", "Forward")
s.print()

f = FighterAthlete("Mike", "USA", "1990-01-01", wins=10, draws=2, loss=1)
f.print()

m = MMAFighterAthlete(
    "Khabib",
    "Russia",
    "1988-09-20",
    ["UFC", "Eagle FC"],
    wins=29,
    draws=0,
    loss=0
)
