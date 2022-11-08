
# Standard imports.
...

# Third-party imports.
from kivy import require

require('2.0.0')  # Require version equal or greater than.

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.input.motionevent import MotionEvent
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget

# Local imports.
...


class Bird(Widget):
    FPS   = 60
    vpos  = NumericProperty(.0)
    vel   = NumericProperty(3.)

    def __init__(self, **kwargs):
        super(Bird, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / self.FPS)

    def update(self, dt: float):
        self.vpos += self.vel

    def jump(self):
        # TODO: Implement jump logic.
        print(self, 'Jump')
        self.vel *= -1.0


class Root(Widget):
    KEY_SPACE = 32
    bird = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Catch specific window events.
        Window.bind(
            on_touch_down = self._on_touch_down,
            on_key_down   = self._on_key_down
        )

    def _on_touch_down(self, ins: Window, touch: MotionEvent):
        # TODO: Implement jump logic.
        print(ins, 'Jump')
        self.bird.jump()

    def _on_key_down(self, ins: Window, key: int, scancode: int, codepoint: str, modifier: list):
        """
        Callback invoked on key down, when window is focused.
        @param ins: Window to which event belongs.
        @param key: ASCII code of pressed key.
        @param scancode: Data straight from the keyboard.
        @param codepoint: Pressed key letter as string.
        @param modifier: List of additional states (like numlock or control).
        """
        if key == self.KEY_SPACE:
            # TODO: Implement jump logic.
            print(ins, 'Jump')
            self.bird.jump()


class FlappyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Root()


if __name__ == '__main__':
    app = FlappyApp()
    app.run()
