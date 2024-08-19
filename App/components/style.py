import dearpygui.dearpygui as dpg
class Sytle():
    def __init__(self):
       self.viewport()
    
    def body(self):

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (140, 255, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)


    def viewport(self):
        with dpg.theme() as global_theme:
            self.body()
        dpg.bind_theme(global_theme)
        dpg.show_style_editor()

    def visualEvent(self): 
       pass
