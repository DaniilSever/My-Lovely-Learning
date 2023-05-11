from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

# -------------------------UIX------------------------ #
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
# ---------------------------------------------------- #

# -----------------------Config----------------------- #
Config.set('graphics', 'minimum_width', '375');
Config.set('graphics', 'resizable', '0');

Config.write()
# ---------------------------------------------------- #

# -----------------------Window----------------------- #
class Catalog(Screen):pass
class Profile(Screen):pass
# ---------------------------------------------------- #



Builder.load_file('./kv/main.kv')
class start(App):
    def build(self):
        # -------------------ScreenManager-------------------- #
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Catalog(name='main'))
        sm.add_widget(Profile(name='profile'))
        # ---------------------------------------------------- #

        return sm

if __name__ == "__main__":
    start().run()

