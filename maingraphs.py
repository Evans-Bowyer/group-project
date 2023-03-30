import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sg.theme('DarkTeal2')
selection = (
    'All', 'Aotizhongxin', 'Changping', 'Dingling', 'Dongsi', 'Guanyuan', 'Gucheng',
    'Huairou', 'Nongzhanguan', 'Shunyi', 'Tiantan', 'Wanliu', 'Wanshouxigong')
types = (
    'SO2', 'NO2', 'CO', 'O3')
airp = None
city = None
cityname = None
file1 = pd.read_csv('Graphdata/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
file2 = pd.read_csv('Graphdata/PRSA_Data_Changping_20130301-20170228.csv')
file3 = pd.read_csv('Graphdata/PRSA_Data_Dingling_20130301-20170228.csv')
file4 = pd.read_csv('Graphdata/PRSA_Data_Dongsi_20130301-20170228.csv')
file5 = pd.read_csv('Graphdata/PRSA_Data_Guanyuan_20130301-20170228.csv')
file6 = pd.read_csv('Graphdata/PRSA_Data_Gucheng_20130301-20170228.csv')
file7 = pd.read_csv('Graphdata/PRSA_Data_Huairou_20130301-20170228.csv')
file8 = pd.read_csv('Graphdata/PRSA_Data_Nongzhanguan_20130301-20170228.csv')
file9 = pd.read_csv('Graphdata/PRSA_Data_Shunyi_20130301-20170228.csv')
file10 = pd.read_csv('Graphdata/PRSA_Data_Tiantan_20130301-20170228.csv')
file11 = pd.read_csv('Graphdata/PRSA_Data_Wanliu_20130301-20170228.csv')
file12 = pd.read_csv('Graphdata/PRSA_Data_Wanshouxigong_20130301-20170228.csv')
files = (file1, file2, file3, file4, file5, file6, file7, file8, file9, file10, file11, file12)


def runstart():
    width = max(map(len, selection)) + 1
    matplotlib.use('TkAgg')
    layout = [
        [sg.Text('Graph:')],
        [sg.Text('Select Air Pollutant:', size=(17, 1)),
         sg.Combo(types, size=(width, 5), enable_events=False, key='-type-')],
        [sg.Text('Select City:', size=(17, 1)),
         sg.Combo(selection, size=(width, 5), enable_events=False, key='-city-')],
        [sg.Submit(), sg.Button('Exit')]
    ]
    window = sg.Window('Patrolling Emission in China', layout, size=(330, 120))
    event, values = window.read()
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
        exit()
    global airp
    airp = values['-type-']
    global city
    city = values['-city-']
    window.close()
    runcode()


def set_scale(scale):

    root = sg.tk.Tk()
    root.tk.call('tk', 'scaling', scale)
    root.destroy()

def run():
    fig = plt.gcf()
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    layout = [[sg.Text(f"{city}'s {airp} emissions", font='Any 18')],
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
              [sg.Button('Back', size=(4, 2)), sg.Button('Exit', pad=(((figure_w / 2.4), 0), 3), size=(4, 2))]]
    window = sg.Window('Air Pollution', layout, force_toplevel=True,
                       finalize=True, enable_close_attempted_event=True)
    draw_figure(window['canvas'].TKCanvas, fig)
    event, values = window.read()
    while event:
        if event == 'Back':
            window.close()
            del window
            runstart()
            break
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            exit()


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)


def runall():
    fig = plt.gcf()
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    layout = [[sg.Text(f"{cityname}'s {airp} emissions", font='Any 18')],
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
              [sg.Button('Back', size=(4, 2)), sg.Button('Next', pad=((figure_w / 2.4, 0), 2), size=(4, 2)),
               sg.Button('Exit', pad=((figure_w / 2.57, 0), 2), size=(4, 2))]],
    window = sg.Window('Air Pollution', layout, force_toplevel=True,
                       finalize=True, enable_close_attempted_event=True)
    draw_figure(window['canvas'].TKCanvas, fig)
    event, values = window.read()
    while event:
        if event == 'Back':
            window.close()
            del window
            runstart()
            break
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            exit()
        if event == 'Next':
            window.close()
            break


def runcode():
    plt.clf()
    if city == "All":
        i = 0
        while i < 12:
            global cityname
            cityname = selection[i + 1]
            x_axis = files[i]['No']
            y_axis = files[i][airp]
            plt.stem(x_axis, y_axis, markerfmt=" ")
            plt.xlabel("Hours since March 1st 2013")
            plt.ylabel(airp)
            runall()
            plt.clf()
            i += 1
            if i == 12:
                exit()
    else:
        x_axis = file1['No']
        y_axis = file1[airp]
        plt.stem(x_axis, y_axis, markerfmt=" ")
        plt.xlabel("Hours since March 1st 2013")
        plt.ylabel(airp)
        run()
        plt.clf()


if __name__ == '__main__':
    runstart()
