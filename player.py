class Player:
  def __init__(self, n):
    self.tiles = []
    self.name = n
    self.score = 0

  def has_buffa(self):
      return any(tile.left == tile.right for tile in self.tiles)

  def highest_buffa(self):
      return max((tile for tile in self.tiles if tile.left == tile.right), default=None, key=lambda tile: tile.left)

  def highest_tile_sum(self):
      return max(self.tiles, key=lambda tile: tile.left + tile.right)
