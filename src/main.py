
"""
File contains basic Kivy-based application start, it starts the application with
style defined in file 'flappy.kv'; the name is same as class's but without 'App' postfix,
by this style file is automatically loaded.
"""

from kivy.app import App


class FlappyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':
    app = FlappyApp()
    app.run()
