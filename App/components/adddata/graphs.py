import dearpygui.dearpygui as dpg
from components.adddata.plottingBarrs import PlottingBarrs
from components.adddata.plottingGraph import PlottingGraphs
def ViewGraphs():
        with dpg.tab_bar():
                PlottingGraphs()
                PlottingBarrs()
