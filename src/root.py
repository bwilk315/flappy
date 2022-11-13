
"""
Together with style file control entire game mechanics, and connects its components together.
It handles window events and manages them so they call proper methods of child components (like Bird or Pipe).
"""

from kivy.input.motionevent import MotionEvent
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window


class Root(Widget):
    KEY_SPACE = 32
    bird      = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Catch specific window events.
        Window.bind(
            on_touch_down = self._on_touch_down,
            on_key_down   = self._on_key_down
        )

    def _on_touch_down(self, ins: Window, touch: MotionEvent):
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
            self.bird.jump()

