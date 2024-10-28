import dearpygui.dearpygui as dpg
class Color():
    def __init__(self):
        self.viewport()

    def body(self):
        with dpg.group(height=115,width=100,horizontal=True):
            with dpg.group(horizontal=True):

                self.table_color()
            with dpg.child_window(height=115, width=100):
               # with dpg.tree_node(label="add"):
                dpg.add_color_picker(height=100, width=100)
        #with dpg.group(height=50, width=50):
                dpg.add_button(label="add")


    def viewport(self):

            self.body()

    def table_color (self):
        with dpg.child_window(height=115):
            with dpg.table(tag="color_table", header_row=True) as selectablerows:
                dpg.add_table_column(label="First")
                dpg.add_table_column(label="Second")
                dpg.add_table_column(label="Third")

                for i in range(15):
                    with dpg.table_row():
                        for j in range(3):
                            dpg.add_selectable(label=f"Row{i} Column{j}", callback=self.clb_selectable, user_data=j)

    def clb_selectable(self, sender, app_data, user_data):
        print(f"Row {user_data}")