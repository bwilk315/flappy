
"""
File defining bird's logic. The bird has own main loop in which checks various things, for instance
height checks are performed to detect if bird touches upper or lower window's limit. 
"""

from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window


class Bird(Widget):
    GRAVITY   = -9.81  # Gravity force.
    FPS       = 60     # Amount of frames per second.
    ROT_MIN   = -60.   # Minimum rotation bird can have.
    ROT_MAX   = 60.    # Maximum rotation bird can reach.
    ROT_SPEED = 1.     # Speed of bird rotation.
    vpos      = NumericProperty(.0)  # Horizontal position.
    hpos      = NumericProperty(.0)  # Vertical position.
    vel       = NumericProperty(3.)  # Velocity of vertical movement.
    rot       = NumericProperty(.0)  # Variable storing rotation of bird.
    timer     = .0     # Timer summing time deltas for ever.
    jump_time = 5 / 9  # Time in seconds describing length of bird's jump.

    def __init__(self, **kwargs):
        super(Bird, self).__init__(**kwargs)
        # Use Kivy clock to make update loop for a bird exclusively.
        Clock.schedule_interval(self.update, 1 / self.FPS)

    def update(self, dt: float):
        # If bird goes outside vertical limits kill him.
        if self.vpos < .0 or self.vpos > Window.size[1]:
            print('die')
            # self.die()
        # Decrease (rotate clockwisely) rotation until it reaches bottom limit.
        if self.rot > self.ROT_MIN:
            self.rot -= self.ROT_SPEED
        # Update position height, velocity and timer.
        self.vpos  += self.vel
        self.vel   += self.GRAVITY * dt
        self.timer += dt

    def die(self):
        """
        Raises error that tells you lose.
        """
        raise LookupError('You died!')

    def jump(self):
        """
        Performs a jump by setting velocity to opposite vector,
        sets the rotation value of bird to the highest (specified by constant).
        """
        self.rot = self.ROT_MAX
        self.vel = -1.0 * self.GRAVITY * self.jump_time

