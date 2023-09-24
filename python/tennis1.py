# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            return self._score_when_same_point()

        if self.p1points >= 4 or self.p2points >= 4:
            return self._score_when_deuce()

        return self._score_when_different_point()

    def _score_when_different_point(self):
        result = ""
        result += self.point_to_score(self.p1points)

        result += "-"
        result += self.point_to_score(self.p2points)
        return result

    @staticmethod
    def point_to_score(a_player_point):
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[a_player_point]

    def _score_when_deuce(self):
        # FIXME: deuce以外の時もあるため、名前が不適切である
        minus_result = self.p1points - self.p2points
        if minus_result == 1:
            result = f"Advantage {self.player1_name}"
        elif minus_result == -1:
            result = f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            result = f"Win for {self.player1_name}"
        else:
            result = f"Win for {self.player2_name}"
        return result

    def _score_when_same_point(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.p1points, "Deuce")
        return result
