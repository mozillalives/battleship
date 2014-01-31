
import errors

class BoardMixin(object):
    pass


class GameMixin(object):
    
    def add_player_board(self, board):
        if self.board1 is None:
            self.board1 = board
        elif self.board2 is None:
            self.board2 = board
        else:
            raise errors.TooManyPlayers()