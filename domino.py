import random
from player import Player
from tile import Tile

class Domino:
  def __init__(self, player1, player2):
    self.tiles = [Tile(i, j) for i in range(6, -1, -1) for j in range(i, -1, -1)]
    self.p1 = player1
    self.p2 = player2
    self.board = []
    self.current = self.p1

  def shuffle(self):
    for _ in range(3):
      random.shuffle(self.tiles) 

  def draw(self, p, n):
    for _ in range(n):
      p.tiles.append(self.tiles.pop())

  def determine_starting_player(self):
    p1_buffa = self.p1.highest_buffa()
    p2_buffa = self.p2.highest_buffa()

    if p1_buffa and (not p2_buffa or p1_buffa.left > p2_buffa.left):
      return self.p1, p1_buffa
    elif p2_buffa:
      return self.p2, p2_buffa

    # If no buffas, check the highest sum tile
    p1_highest_tile = self.p1.highest_tile_sum()
    p2_highest_tile = self.p2.highest_tile_sum()

    if p1_highest_tile.left + p1_highest_tile.right > p2_highest_tile.left + p2_highest_tile.right:
      return self.p1, p1_highest_tile
    else:
      return self.p2, p2_highest_tile

  def start(self):
    self.draw(self.p1, 7)
    self.draw(self.p2, 7)
    starting_player, starting_tile = self.determine_starting_player()

    # Set the starting player and place the starting tile on the board
    self.current_player = starting_player
    self.board.append(starting_tile)
    starting_player.tiles.remove(starting_tile)

  def play(self):
    self.shuffle()
    self.start()

  def printTiles(self, til):
    for tile in til:
      print(tile)
        

p1 = Player('David')
p2 = Player('Mark')
game = Domino(p1, p2)
game.play()

print("player 1 tiles:")
game.printTiles(p1.tiles)
print("player 2 tiles:")
game.printTiles(p2.tiles)

print("EL ARD:")
game.printTiles(game.board)

print("rest of the tiles:")
game.printTiles(game.tiles)
