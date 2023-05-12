from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

# -------------------------UIX------------------------ #
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
# ---------------------------------------------------- #

# -----------------------Config----------------------- #
Config.set('graphics', 'minimum_width', '375');
Config.set('graphics', 'resizable', '0');

Config.write()
# ---------------------------------------------------- #

# -----------------------Window----------------------- #
class Catalog(Screen):
    Builder.load_file('./kv/catalog.kv')

    # -----------------------Widgets---------------------- #
    class Header_Dropdown(DropDown):
        Builder.load_file('./widgets/headerDropDown.kv')

    # ---------------------------------------------------- #

    def __init__(self, **kw):
        super().__init__(**kw)
        dropdown_btn = self.ids.dropdown_profile
        dropdown = Catalog.Header_Dropdown()
        dropdown_btn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(dropdown_btn, 'text', x))
        
        Profile_btn = self.ids.profile
        Profile_btn.bind(on_release=self.root.manager.current('profile'))



class Profile(Screen):
    Builder.load_file('./kv/profile.kv')
# ---------------------------------------------------- #



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

