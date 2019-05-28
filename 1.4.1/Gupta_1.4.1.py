# module realityArtist.py
class PingPongBall(object):
    def __init__(self, myRadius=20, myColor='#FFFFFF'):
        """ Creates a new PingPongBall
        
        radius expressed in millimeters
        color is expressed in a 6-digit hexadecimal
          color defaults to White, the color of the ball)           
        """
        # Implement with a human so that: 
        self.radius = myRadius
        self.color = myColor
        
    def draw_circle(self, diameter=10, color='#FF0000', fill=False):
        """ Draws a circle on a random location on the ball

        uses colored pencil 
        diameter is expressed in millimeters
        color is expressed in a 6-digit hexadecimal string
           default color red
        """
        # Implement with human
