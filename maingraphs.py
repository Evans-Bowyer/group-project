import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import os

# Selects a PySimpleGUI theme.
sg.theme('DarkTeal2')


# Creates a GUI that accepts user input using PySimpleGUI.
def main_graph_gui():

    width = max(map(len, selection)) + 1
    matplotlib.use('TkAgg')

    # define GUI elements and window
    layout = [
        [sg.Text('Graph:')],

        [sg.Text('Select Air Pollutant:', size=(17, 1)),
         sg.Combo(types, size=(width, 5), enable_events=False, key='-type-')],

        [sg.Text('Select Station:', size=(17, 1)),
         sg.Combo(selection, size=(width, 5), enable_events=False, key='-city-')],

        [sg.Button('Back', size=(4, 2)), sg.Submit(), sg.Button('Exit')]
    ]
    window = sg.Window('Patrolling Emission in China', layout, size=(330, 120))
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
        exit()
    if event == 'Back':
        window.close()
        os.system('connector.py')
        exit()

    airp = values['-type-']
    city = values['-city-']

    # close selection window and draw graph
    window.close()
    create_graph(city, airp)


# Uses matplotlib to create graphs using user input and data files.
def create_graph(city, airp):
    if city == "All":

        for i in range(1, 13):

            cityname = selection[i]

            plot = make_graph(cityname, airp)

            create_all_graphs_gui(plot, cityname, airp)
            plt.clf()
    else:

        plot = make_graph(city, airp)

        create_graph_gui(plot, city, airp)
        plt.clf()


# creates a pyplot graph given a stations name and air pollutant
def make_graph(city, airp): 

    file = pd.read_csv(f'Graphdata/PRSA_Data_{city}_20130301-20170228.csv')

    x_axis = file['No']
    y_axis = file[airp]

    plt.stem(x_axis, y_axis, markerfmt=" ")
    plt.xlabel("Hours since March 1st 2013")
    plt.ylabel(f'{airp} (ug / m\u00b3)')

    return plt.gcf()


# Uses the created matplotlib graphs to create a GUI that visualizes the data of all the cities using PySimpleGUI.
def create_all_graphs_gui(fig, cityname, airp):

    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    layout = [
                [sg.Text(f"{cityname} Station's {airp} emissions from 03/01/13 to 03/01/17", font='Any 18')],

                [sg.Canvas(size=(figure_w, figure_h), key='canvas')],

                [sg.Button('Back', size=(4, 2)),
                 sg.Button('Next', pad=((figure_w / 2.4, 0), 2), size=(4, 2)),
                 sg.Button('Exit', pad=((figure_w / 2.57, 0), 2), size=(4, 2))]
             ]

    window = sg.Window('Air Pollution', layout, force_toplevel=True,
                       finalize=True, enable_close_attempted_event=True)
    draw_figure(window['canvas'].TKCanvas, fig)
    event, values = window.read()

    while event:

        if event == 'Back':
            window.close()
            plt.clf()
            del window
            main_graph_gui()
            break

        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            exit()

        if event == 'Next':
            plt.clf()
            window.close()
            break


# Uses the created matplotlib graphs to create a GUI that visualizes the data of the inputted station using PySimpleGUI.
def create_graph_gui(fig, city, airp):

    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

    layout = [
                [sg.Text(f"{city} Station's {airp} emissions from 03/01/13 to 03/01/17", font='Any 18')],

                [sg.Canvas(size=(figure_w, figure_h), key='canvas')],

                [sg.Button('Back', size=(4, 2)),
                 sg.Button('Exit', pad=(((figure_w / 1.152), 0), 3), size=(4, 2))]
            ]

    window = sg.Window('Air Pollution', layout, force_toplevel=True,
                       finalize=True, enable_close_attempted_event=True)
    draw_figure(window['canvas'].TKCanvas, fig)
    event, values = window.read()

    while event:

        if event == 'Back':
            window.close()
            plt.clf()
            del window
            main_graph_gui()
            break

        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            exit()


# Used within create_graph_gui() and create_all_graph_gui() to draw the graphs onto the GUI using PySimpleGUI.
def draw_figure(canvas, figure):

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)


# Runs the program by calling the main_graph_gui() function.
if __name__ == '__main__':

    # Initialize neccessary lists
    global selection
    selection = (
            'All', 'Aotizhongxin', 'Changping', 'Dingling', 'Dongsi', 'Guanyuan',
            'Gucheng', 'Huairou', 'Nongzhanguan', 'Shunyi', 'Tiantan', 'Wanliu', 
            'Wanshouxigong'
            )
    global types
    types = ('SO2', 'NO2', 'CO', 'O3')
    
    main_graph_gui()
