from statistics import mean

class Game:
    all_games = []

    def __init__(self, title):
        self._title = title
        type(self).all_games.append(self)

    @property
    def title(self):
        return self._title

    def results(self):
        return [result for result in Result.all_results if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return mean(scores) if scores else 0


class Player:
    all_players = []

    def __init__(self, username):
        self._username = username
        type(self).all_players.append(self)

    @property
    def username(self):
        return self._username

    def results(self):
        return [result for result in Result.all_results if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)


class Result:
    all_results = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all_results.append(self)
