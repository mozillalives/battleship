
import unittest
import errors
import helpers
import models

from google.appengine.api import memcache, users
from google.appengine.ext import db, testbed


# http://melp.nl/2011/02/enhancing-python-unit-tests-with-more-decorators/
def expect_exception(exception):
    """Marks test to expect the specified exception. Call assertRaises internally"""
    def test_decorator(fn):
        def test_decorated(self, *args, **kwargs):
            self.assertRaises(exception, fn, self, *args, **kwargs)
        return test_decorated
    return test_decorator

# class HelperTestCase(unittest.TestCase):
#     
#     def test_valid_space_keys(self):
#         self.assertEquals(('a', '1'), helpers.split_space_key('a1'))
#         self.assertEquals(('a', '11'), helpers.split_space_key('a11'))
#         self.assertEquals(('aa', '11'), helpers.split_space_key('aa11'))
# 
#     def test_convert_valid_space_keys(self):
#         self.assertEquals(0, helpers.convert_space_key('a1', 10, 11))
#         self.assertEquals(7, helpers.convert_space_key('h1', 10, 11))
#         self.assertEquals(9, helpers.convert_space_key('j1', 10, 11))
#         self.assertEquals(19, helpers.convert_space_key('j2', 10, 11))
#         self.assertEquals(107, helpers.convert_space_key('h11', 10, 11))
#         self.assertEquals(37, helpers.convert_space_key('c6', 7, 7))
# 
#     @expect_exception(errors.SpaceOutOfBounds)
#     def test_outofbound_space_keys(self):
#         helpers.convert_space_key('z11', 10, 10)
# 
#     @expect_exception(errors.InvalidSpace)
#     def test_invalid_space_keys(self):
#         helpers.split_space_key('aa')
# 
#     @expect_exception(errors.InvalidSpace)
#     def test_invalid_space_keys2(self):
#         helpers.split_space_key('11')
# 
#     def test_replace_chars(self):
#         spaces = 'nnnnnnnnnnnnnnnnnffffnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
#         old_spaces = 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
#         new_spaces = helpers.replace_chars([17, 18, 19, 20], 'f', old_spaces)
#         self.assertEqual(spaces, new_spaces)

class GameSetupTestCase(unittest.TestCase):
    pass
    # test adding one player (pass)
    # test adding two players (pass)
    # test adding three players (fail)
    # test adding one player and setting up board (pass)
    # test adding one player, setting up board, playing (fail)
    # test adding one player and playing (fail)
    
# class GameSetupTestCase(unittest.TestCase):
#     
#     def setUp(self):
#         # First, create an instance of the Testbed class.
#         self.testbed = testbed.Testbed()
#         # Then activate the testbed, which prepares the service stubs for use.
#         self.testbed.activate()
#         # Next, declare which service stubs you want to use.
#         self.testbed.init_datastore_v3_stub()
#         #self.testbed.init_memcache_stub()
#         self.testbed.init_user_stub()
# 
#         self.game = models.Game()
#         self.game.put()
# 
#     def tearDown(self):
#         self.game.delete()
#         self.testbed.deactivate()
# 
#     def test_adding_one_player(self):
#         """test adding a single player to the game"""
#         self.game.add_player(users.User('mozillalives@gmail.com'))
# 
#     def test_adding_two_players(self):
#         """test adding two players to the game"""
#         self.game.add_player(users.User('mozillalives@gmail.com'))
#         self.game.add_player(users.User('mozillalives@gmail.com'))
# 
#     @expect_exception(errors.TooManyPlayers)
#     def test_adding_three_players(self):
#         """test adding three players to the game"""
#         self.game.add_player(users.User('mozillalives@gmail.com'))
#         self.game.add_player(users.User('mozillalives@gmail.com'))
#         self.game.add_player(users.User('mozillalives@gmail.com'))
# 
#     @expect_exception(errors.NotSetupYet)
#     def test_adding_one_player(self):
#         """test playing when there is only a single player registered"""
#         self.game.add_player(users.User('mozillalives@gmail.com'))
# 

class AssembleBoardTestCase(unittest.TestCase):
    pass
# class AssembleShipsTestCase(unittest.TestCase):
#     """test the placing of ships"""
# 
#     def setUp(self):
#         self.testbed = testbed.Testbed()
#         self.testbed.activate()
#         self.testbed.init_datastore_v3_stub()
#         self.testbed.init_user_stub()
# 
#         self.board = models.Board(spaces=helpers.default_gameboard(7, 7),
#             columns=7, rows=7)
#         self.board.put()
# 
#     def tearDown(self):
#         self.board.delete()
#         self.testbed.deactivate()
# 
#     def test_generating_a_horizontal_range(self):
#         # TODO move this to the helper tests
#         a = models.generate_range('a1', 'd1')
#         self.assertEquals(['a1', 'b1', 'c1', 'd1'], a)
#         a = models.generate_range('f11', 'j11')
#         self.assertEquals(['f11', 'g11', 'h11', 'i11', 'j11'], a)
#  
#     def test_generating_a_vertical_range(self):
#         # TODO move this to the helper tests
#         a = models.generate_range('a1', 'a4')
#         self.assertEquals(['a1', 'a2', 'a3', 'a4'], a)
#         a = models.generate_range('e5', 'e9')
#         self.assertEquals(['e5', 'e6', 'e7', 'e8', 'e9'], a)
# 
#     def test_plain_board(self):
#         #   A B C D E F G
#         # 1 n n n n n n n
#         # 2 n n n n n n n
#         # 3 n n n n n n n
#         # 4 n n n n n n n
#         # 5 n n n n n n n
#         # 6 n n n n n n n
#         # 7 n n n n n n n
# 
#         spaces = 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
#         self.assertEqual(spaces, self.board.spaces)
# 
#     @expect_exception(errors.CannotPlaceDiagonally)
#     def test_generating_a_diagonal_range(self):
#         # TODO move this to the helper tests
#         models.generate_range('a1', 'd4')
#  
#     def test_placing_a_ship_horizontally(self):
#         #   A B C D E F G
#         # 1 n n n n n n n
#         # 2 n n n n n n n
#         # 3 n n n 4 4 4 4
#         # 4 n n n n n n n
#         # 5 n n n n n n n
#         # 6 n n n n n n n
#         # 7 n n n n n n n
#         #
# 
#         spaces = 'nnnnnnnnnnnnnnnnn4444nnnnnnnnnnnnnnnnnnnnnnnnnnnn'
#         self.board.place_ship(4, 'd3', 'g3')
#         self.assertEqual(spaces, self.board.spaces)
# 
# 
#     def test_placing_a_ship_vertically(self):
#         #   A B C D E F G
#         # 1 n n n n n n n
#         # 2 n n n n n n n
#         # 3 n n n n n n n
#         # 4 n n 3 n n n n
#         # 5 n n 3 n n n n
#         # 6 n n 3 n n n n
#         # 7 n n n n n n n
#         #
# 
#         # TODO invalidate if range is 3 but ship is not
#         spaces = 'nnnnnnnnnnnnnnnnnnnnnnn3nnnnnn3nnnnnn3nnnnnnnnnnn'
#         self.board.place_ship(3, 'c4', 'c6')
#         self.assertEqual(spaces, self.board.spaces)
#         
#     @expect_exception(errors.CannotPlaceDiagonally)
#     def test_placing_a_ship_diagonally(self):
#         self.board.place_ship(3, 'a1', 'c3')
# 
#     @expect_exception(errors.CannotPlaceDiagonally)
#     def test_placing_a_ship_across_the_board(self):
#         self.board.place_ship(5, 'a1', 'j11')
#         
#     @expect_exception(errors.SpaceOutOfBounds)
#     def test_placing_a_ship_on_a_nonexistant_space(self):
#         self.board.place_ship(3, 'aa1', 'aa3')
# 
#     def test_spaces_filled_by_ships(self):
#         self.board.place_ship(4, 'd3', 'g3')
# 
#         board = self.board
#         self.assertEquals(board.get_space_state('d3'), '4')
#         self.assertEquals(board.get_space_state('e3'), '4')
#         self.assertEquals(board.get_space_state('f3'), '4')
#         self.assertEquals(board.get_space_state('g3'), '4')
# 
#         self.assertEquals(board.get_space_state('g4'), 'n')
#         self.assertEquals(board.get_space_state('d2'), 'n')
#         self.assertEquals(board.get_space_state('c3'), 'n')
#         self.assertEquals(board.get_space_state('h3'), 'n')
# 
#     @expect_exception(errors.SpaceTaken)
#     def test_placing_overlapping_ships(self):
#         self.board.place_ship(3, 'd3', 'f3')
#         self.board.place_ship(3, 'e2', 'e4')
# 
#     @expect_exception(errors.NoMoreShipsToPlace)
#     def test_placing_two_two_space_ships(self):
#         self.board.place_ship(2, 'a1', 'b1')
#         self.board.place_ship(2, 'a2', 'b2')
# 
#     @expect_exception(errors.NoMoreShipsToPlace)
#     def test_placing_three_three_space_ships(self):
#         self.board.place_ship(3, 'a1', 'c1')
#         self.board.place_ship(3, 'a2', 'c2')
#         self.board.place_ship(3, 'a3', 'c3')
# 
#     @expect_exception(errors.NoMoreShipsToPlace)
#     def test_placing_two_four_space_ships(self):
#         self.board.place_ship(4, 'a1', 'd1')
#         self.board.place_ship(4, 'a2', 'd2')
# 
#     @expect_exception(errors.NoMoreShipsToPlace)
#     def test_placing_two_five_space_ships(self):
#         self.board.place_ship(5, 'a1', 'e1')
#         self.board.place_ship(5, 'a2', 'e2')
# 
#     def test_all_placed(self):
#         self.assertFalse(self.board.all_placed())
#         self.board.place_ship(2, 'a1', 'b1')
#         self.assertFalse(self.board.all_placed())
#         self.board.place_ship(3, 'a2', 'c2')
#         self.assertFalse(self.board.all_placed())
#         self.board.place_ship(3, 'a3', 'c3')
#         self.assertFalse(self.board.all_placed())
#         self.board.place_ship(4, 'a4', 'd4')
#         self.assertFalse(self.board.all_placed())
#         self.board.place_ship(5, 'a5', 'e5')
#         self.assertTrue(self.board.all_placed())
# 
#     def test_shooting_a_filled_space(self):
#         #   A B C D E F G
#         # 1 n n n n n n n
#         # 2 n n n n n n n
#         # 3 n n n x 4 4 4
#         # 4 n n n n n n n
#         # 5 n n n n n n n
#         # 6 n n n n n n n
#         # 7 n n n n n n n
#         #
# 
#         spaces = 'nnnnnnnnnnnnnnnnnx444nnnnnnnnnnnnnnnnnnnnnnnnnnnn'
#         self.board.place_ship(4, 'd3', 'g3')
#         self.board.shoot_space('d3')
#         self.assertEqual(spaces, self.board.spaces)
# 
#     def test_shooting_an_empty_space(self):
#         #   A B C D E F G
#         # 1 n n n n n n n
#         # 2 n n n n n n n
#         # 3 n n m 4 4 4 4
#         # 4 n n n n n n n
#         # 5 n n n n n n n
#         # 6 n n n n n n n
#         # 7 n n n n n n n
#         #
# 
#         spaces = 'nnnnnnnnnnnnnnnnm4444nnnnnnnnnnnnnnnnnnnnnnnnnnnn'
#         self.board.place_ship(4, 'd3', 'g3')
#         self.board.shoot_space('c3')
#         self.assertEqual(spaces, self.board.spaces)
# 
#     @expect_exception(errors.AlreadyPlayedHere)
#     def test_shooting_same_empty_space(self):
# 
#         spaces = 'nnnnnnnnnnnnnnnnm4444nnnnnnnnnnnnnnnnnnnnnnnnnnnn'
#         self.board.place_ship(4, 'd3', 'g3')
#         self.board.shoot_space('c3')
#         self.assertEqual(spaces, self.board.spaces)
#         self.board.shoot_space('c3')
# 
#     @expect_exception(errors.AlreadyPlayedHere)
#     def test_shooting_same_filled_space(self):
# 
#         spaces = 'nnnnnnnnnnnnnnnnnx444nnnnnnnnnnnnnnnnnnnnnnnnnnnn'
#         self.board.place_ship(4, 'd3', 'g3')
#         self.board.shoot_space('d3')
#         self.assertEqual(spaces, self.board.spaces)
#         self.board.shoot_space('d3')
# 
#

class BadPlaysTestCase(unittest.TestCase):
    pass
 
# class BadPlayTestCase(unittest.TestCase):
# 
#     def setUp(self):
#         self.testbed = testbed.Testbed()
#         self.testbed.activate()
#         self.testbed.init_datastore_v3_stub()
#         self.testbed.init_user_stub()
# 
#         self.game = models.Game()
#         self.game.put()
#         self.game.add_player(users.User('mozillalives@gmail.com'))
#         self.game.add_player(users.User('mozillalives@gmail.com'))
# 
#     def tearDown(self):
#         self.game.delete()
#         self.testbed.deactivate()
# 
#     @expect_exception(errors.NotAllShipsPlaced)
#     def test_playing_before_all_ships_are_placed(self):
#         self.game.place_ship(1, 5, 'a1', 'e1')
#         self.game.play(1, 'a1')
# 

class GoodPlaysTestCase(unittest.TestCase):
    pass

# class PlayTestCase(unittest.TestCase):
# 
#     def setUp(self):
#         self.testbed = testbed.Testbed()
#         self.testbed.activate()
#         self.testbed.init_datastore_v3_stub()
#         self.testbed.init_user_stub()
# 
#         #board = models.Board(spaces=helpers.default_gameboard(7, 7),
#         #    columns=7, rows=7)
#         self.game = models.Game()
#         self.game.put()
#         self.game.add_player(users.User('mozillalives@gmail.com'))
#         self.game.add_player(users.User('mozillalives@gmail.com'))
# 
#         self.game.place_ship(1, 2, 'a1', 'b1')
#         self.game.place_ship(1, 3, 'd3', 'f3')
#         self.game.place_ship(1, 3, 'h7', 'h9')
#         self.game.place_ship(1, 4, 'b5', 'b8')
#         self.game.place_ship(1, 5, 'c6', 'g6')
# 
#         self.game.place_ship(2, 2, 'a1', 'b1')
#         self.game.place_ship(2, 3, 'd3', 'f3')
#         self.game.place_ship(2, 3, 'h7', 'h9')
#         self.game.place_ship(2, 4, 'b5', 'b8')
#         self.game.place_ship(2, 5, 'c6', 'g6')
# 
#     def tearDown(self):
#         self.game.delete()
#         self.testbed.deactivate()
# 
#     def test_play_a_hit(self):
#         self.game.play(1, ['a1'])
#         self.assertEquals('x', self.game.boards[1].get_space_state('a1'))
# 
#     def test_play_a_miss(self):
#         self.game.play(1, ['h5'])
#         self.assertEquals('m', self.game.boards[1].get_space_state('h5'))
# 
#     def test_ship_is_sunk(self):
#         self.game.play(1, ['a1', 'b1'])
#         self.assertEquals(True, self.game.is_sunk(2, 2))
# 
#     @expect_exception(errors.AlreadyPlayedHere)
#     def test_play_the_same_space(self):
#         self.game.play(1, ['a1'])
#         self.game.play(1, ['a1'])
# 
#     @unittest.skip
#     def test_game_is_won(self):
#         pass
# 
#     def test_play_passes_to_next_player(self):
#         self.game.play(1, ['a1', 'b1', 'h5', 'h1', 'c2'])
#         self.assertEquals(True, self.game.whose_turn)
#         self.game.play(2, ['a1', 'b1', 'h5', 'h1', 'c2'])
# 
#     @expect_exception(errors.TurnHasEnded)
#     def test_play_when_not_your_turn(self):
#         self.game.play(1, ['a1', 'b1', 'h5', 'h1', 'c2'])
#         self.game.play(1, ['b2'])
# 
#     @expect_exception(errors.NotYourTurn)
#     def test_play_when_not_your_turn(self):
#         self.game.play(2, ['a1', 'b1', 'h5', 'h1', 'c2'])
# 
