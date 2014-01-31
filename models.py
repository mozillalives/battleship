
from google.appengine.ext import ndb

from helpers import default_gameboard
# from errors import *

# I know, I know - this isn't ruby
from mixins import BoardMixin, GameMixin


class Board(ndb.Model, BoardMixin):
    player = ndb.UserProperty()
    spaces = ndb.StringProperty(default=default_gameboard(10, 10))
    columns = ndb.IntegerProperty(default=10)
    rows = ndb.IntegerProperty(default=10)
    last_play = ndb.StringProperty()


class Game(ndb.Model, GameMixin):
    board1_key = ndb.KeyProperty(kind=Board)
    board2_key = ndb.KeyProperty(kind=Board)
    turns = ndb.IntegerProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty()
    ended_at = ndb.DateTimeProperty()
    winner = ndb.UserProperty()
    
    @property
    def board1(self):
        if self.board1_key is None:
            return None
        return ndb.Key(Board, self.board1_key).get()

    @property
    def board2(self):
        if self.board2_key is None:
            return None
        return ndb.Key(Board, self.board2_key).get()

# class Game(db.Model):
#     player1 = db.UserProperty()
#     player2 = db.UserProperty()
#     started_at = db.DateTimeProperty(auto_now_add=True)
#     ended_at = db.DateTimeProperty()
#     player1_score = db.IntegerProperty()
#     player2_score = db.IntegerProperty()
#     whose_turn = db.BooleanProperty(default=False)
#     current_play = db.ListProperty(str)
# 
#     def add_player(self, user):
#         if self.player1 is None:
#             self.player1 = user
#             self.put()
#             Board(game=self, player=1).put()
#         elif self.player2 is None:
#             self.player2 = user
#             self.put()
#             Board(game=self, player=2).put()
#         else:
#             raise TooManyPlayers()
#     
#     def place_ship(self, player, ship, start, end):
#         if player == 1:
#             self.boards[0].place_ship(ship, start, end)
#         else:
#             self.boards[1].place_ship(ship, start, end)
# 
#     def play(self, player, spaces):
# 
#         if not self.boards[0].all_placed() or \
#             not self.boards[1].all_placed():
#             raise NotAllShipsPlaced()
#         
#         if int(self.whose_turn)+1 != player:
#             raise NotYourTurn()
# 
#         if player == 1:
#             enemies_board = self.boards[0]
#         else:
#             enemies_board = self.boards[1]
# 
#         for space in spaces:
#             if len(self.current_play) > 4:
#                 raise TurnHasEnded()
#             enemies_board.shoot_space(space)
#             self.current_play.append(space)
# 
#         if len(self.current_play) == 5:
#             Play(game=self, player=player, shots=self.current_play).put()
#             self.whose_turn = not self.whose_turn
#             self.current_play = []
#             self.put()
# 
# class Board(db.Model):
#     game = db.ReferenceProperty(Game, collection_name='boards')
#     player = db.IntegerProperty()
#     spaces = db.TextProperty(default=default_gameboard())
#     columns = db.IntegerProperty(default=10)
#     rows = db.IntegerProperty(default=10)
#     placed = db.ListProperty(str)
# 
#     def shoot_space(self, space):
#         try:
#             index = convert_space_key(space, self.columns, self.rows)
#             if self.spaces[index] in ['x', 'm']:
#                 raise AlreadyPlayedHere(space)
#             elif self.spaces[index] == 'n':
#                 val = 'm'
#             else:
#                 val = 'x'
#             self.spaces = replace_chars([index], val, self.spaces)
#             self.put()
#         except IndexError:
#             raise SpaceNotFound(space)
# 
# 
#     def already_placed(self, ship):
#         s = str(ship)
#         p = filter(lambda i: str(i) == s, self.placed)
#         if str(ship) == '3':
#             return len(p) > 1
#         else:
#             return len(p) > 0
# 
#     def all_placed(self):
#         return sorted(self.placed) == sorted(['3', '2', '5', '4', '3'])
# 
#     def get_space_state(self, space):
#         try:
#             index = convert_space_key(space, self.columns, self.rows)
#             return self.spaces[index]
#         except IndexError:
#             raise SpaceNotFound(space)
# 
#     def place_ship(self, ship, start, end):
#         spaces_needed = generate_range(start, end)
#         indexes = []
#         
#         if self.already_placed(ship):
#             raise NoMoreShipsToPlace(ship)
# 
#         for s in spaces_needed:
#             if self.get_space_state(s) != 'n':
#                 raise SpaceTaken()
#             indexes.append(convert_space_key(s, self.columns, self.rows))
# 
#         self.spaces = replace_chars(indexes, str(ship), self.spaces)
#         self.placed.append(str(ship))
#         self.put()
# 
# class Play(db.Model):
#     game = db.ReferenceProperty(Game)
#     player = db.IntegerProperty()
#     shots = db.ListProperty(str)
#     played_at = db.DateTimeProperty(auto_now_add=True)
