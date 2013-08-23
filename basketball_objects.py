class BasketballPlayer:
  def __init__(self, name):
    self.name = name
    self.weight = 150   # (unit in lbs)
    self.height = 72    # (unit in inches)
    self.hasBall = False

  def Dribble():
    if (self.hasBall):
      print(self.name+" dribbles the ball!")

  def Pass(self, player):
    if (self.hasBall):
      print(self.name+" passes the ball to " + player.name)
      self.hasBall = False
      player.hasBall = True

  def Shoot(self):
    if (self.hasBall):
      print(self.name+ " shoots the ball")
      self.hasBall = False
        
def example():
  player_1 = BasketballPlayer("Kobe Bryant")
  player_2 = BasketballPlayer("Michael Jordan")
  player_1.hasBall = True
  player_1.Pass(player_2)
  player_2.Shoot()
    
example()
