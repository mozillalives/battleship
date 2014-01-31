
import unittest
import datetime

import mixins
import errors

# Some boilerplate to set this up

def expect_exception(exception):
    """Marks test to expect the specified exception. Call assertRaises internally"""
    def test_decorator(fn):
        def test_decorated(self, *args, **kwargs):
            self.assertRaises(exception, fn, self, *args, **kwargs)
        return test_decorated
    return test_decorator

class BaseModel(object):
    pass # just a stub

class Board(BaseModel, mixins.BoardMixin):
    player = None
    spaces = ""
    columns = 10
    rows = 10
    last_play = ""

class Game(BaseModel, mixins.GameMixin):
    board1 = None
    board2 = None
    turns = 0
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    ended_at = None
    winner = None

class User(object):
    def __init__(self, email):
        self.email = email

# And now, to the tests

class GameInitTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_adding_one_player(self):
        """test adding a single player to the game"""
        self.game.add_player_board(Board())

    def test_adding_two_players(self):
        """test adding two players to the game"""
        self.game.add_player_board(Board())
        self.game.add_player_board(Board())

    @expect_exception(errors.TooManyPlayers)
    def test_adding_three_players(self):
        """test adding three players to the game"""
        self.game.add_player_board(Board())
        self.game.add_player_board(Board())
        self.game.add_player_board(Board())

    # @expect_exception(errors.NotSetupYet)
    # def test_adding_one_player(self):
    #     """test playing when there is only a single player registered"""
    #     self.game.add_player_board(Board())

    # TODO test adding one player and setting up board (pass)
    # TODO test adding one player, setting up board, playing (fail)
    # TODO test adding one player and playing (fail)

class BoardSetupTestCase(unittest.TestCase):
    pass
    
    # TODO test adding each ship, horizontally
    # TODO test adding each ship, vertically
    # TODO test adding the ships before a second user signs up
    # TODO test adding the ships after a second user signs up
    # TODO test adding each ship, diagonally (fail)
    # TODO test adding each ship, with spaces between (fail)
    # TODO test adding a ship on top of another ship (fail)
    # TODO test adding a ship that extends over the board edge (horizontally, vertically and on either side)
    # TODO test adding a ship to another player's board (fail)

class PlayGameTestCase(unittest.TestCase):
    pass
    # TODO test moving a ship after gameplay has started (fail)
    

if __name__ == '__main__':
    unittest.main()