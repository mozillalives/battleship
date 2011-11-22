
class Error(Exception):
    pass

class InvalidSpace(Error):
    pass

class TooManyPlayers(Error):
    pass

class CannotPlaceDiagonally(Error):
    pass

class SpaceNotFound(Error):
    pass

class SpaceOutOfBounds(Error):
    pass

class SpaceTaken(Error):
    pass

class NoMoreShipsToPlace(Error):
    pass

class NotAllShipsPlaced(Error):
    pass

class NotYourTurn(Error):
    pass

class TurnHasEnded(Error):
    pass

class AlreadyPlayedHere(Error):
    pass

