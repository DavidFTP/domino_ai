class Tile:
  def __init__(self, l, r):
    self.left = l
    self.right = r

  def __str__(self):
    return f"{self.left} : {self.right}"