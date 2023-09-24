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
            return self.score_when_same_point()

        if self.p1points >= 4 or self.p2points >= 4:
            return self.score_when_deuce()

        return self._score()

    def _score(self):
        # MEMO 良い名前がつけられなかったため
        result = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = self.p1points
            else:
                result += "-"
                temp_score = self.p2points
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[temp_score]
        return result

    def score_when_deuce(self):
        minus_result = self.p1points - self.p2points
        if minus_result == 1:
            result = "Advantage player1"
        elif minus_result == -1:
            result = "Advantage player2"
        elif minus_result >= 2:
            result = "Win for player1"
        else:
            result = "Win for player2"
        return result

    def score_when_same_point(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.p1points, "Deuce")
        return result
