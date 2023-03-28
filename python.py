import PySimpleGUI as sg
sg.theme('DarkTeal2')
selection = (
    'All', 'Aotizhongxin', 'Changping', 'Dingling', 'Dongsi', 'Guanyuan', 'Gucheng',
    'Huairou', 'Nongzhanguan', 'Shunyi', 'Tiantan', 'Wanliu', 'Wanshouxigong')
types = (
    'SO2', 'NO2', 'CO', 'O3')
width = max(map(len, selection)) + 1
layout = [
    [sg.Text('Select Air Pollutant:')],
    [sg.Text('SO2, NO2, CO, or O3:', size=(17, 1)),
     sg.Combo(types, size=(width, 5), enable_events=False, key='-type-')],
    [sg.Text('Select City:', size=(17, 1)),
     sg.Combo(selection, size=(width, 5), enable_events=False, key='-city-')],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Patrolling Emission in China', layout, size=(330, 120))
event, values = window.read()
type = values['-type-']
city = values['-city-']
window.close()

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def run():
    fig = plt.gcf()
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    def draw_figure(canvas, figure, loc=(0, 0)):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    layout = [[sg.Text(f"{city}'s {type} emissions", font='Any 18')],
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
              [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]
    window = sg.Window('Air Pollution', layout, force_toplevel=True,
                       finalize=True)
    fig_photo = draw_figure(window['canvas'].TKCanvas, fig)
    event, values = window.read()

def runall():
    fig = plt.gcf()
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    def draw_figure(canvas, figure, loc=(0, 0)):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    layout = [[sg.Text(f"{type} emissions", font='Any 18')],
                [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
                [sg.Button('Next', pad=((figure_w / 2, 0), 3), size=(4, 2)), sg.Button('Exit', pad=((figure_w / 2, 0), 3), size=(4, 2))]],
    window = sg.Window('Air Pollution', layout, force_toplevel=True,
                       finalize=True, enable_close_attempted_event=True)
    fig_photo = draw_figure(window['canvas'].TKCanvas, fig)
    event, values = window.read()
    while event:
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            exit()
        if event == 'Next':
            break

if city == "All":
    f1 = plt.figure(1)
    x_axis = file1['No']
    y_axis = file1[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Aotizhongxin")
    plt.ylabel(type)
    runall()
    f2 = plt.figure(2)
    x_axis = file2['No']
    y_axis = file2[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Changping")
    plt.ylabel(type)
    runall()
    f3 = plt.figure(3)
    x_axis = file3['No']
    y_axis = file3[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Dingling")
    plt.ylabel(type)
    runall()
    f4 = plt.figure(4)
    x_axis = file4['No']
    y_axis = file4[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Dongsi")
    plt.ylabel(type)
    runall()
    f5 = plt.figure(5)
    x_axis = file5['No']
    y_axis = file5[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Guanyuan")
    plt.ylabel(type)
    runall()
    f6 = plt.figure(6)
    x_axis = file6['No']
    y_axis = file6[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Gucheng")
    plt.ylabel(type)
    runall()
    f7 = plt.figure(7)
    x_axis = file7['No']
    y_axis = file7[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Huairou")
    plt.ylabel(type)
    runall()
    f8 = plt.figure(8)
    x_axis = file8['No']
    y_axis = file8[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Nongzhanguan")
    plt.ylabel(type)
    runall()
    f9 = plt.figure(9)
    x_axis = file9['No']
    y_axis = file9[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Shunyi")
    plt.ylabel(type)
    runall()
    f10 = plt.figure(10)
    x_axis = file10['No']
    y_axis = file10[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Tiantan")
    plt.ylabel(type)
    runall()
    f11 = plt.figure(11)
    x_axis = file11['No']
    y_axis = file11[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Wanliu")
    plt.ylabel(type)
    runall()
    f12 = plt.figure(12)
    x_axis = file12['No']
    y_axis = file12[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Wanshouxigong")
    plt.ylabel(type)
    runall()
elif city == "Aotizhongxin":
    f1 = plt.figure(1)
    x_axis = file1['No']
    y_axis = file1[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Aotizhongxin")
    plt.ylabel(type)
    run()
elif city == "Changping":
    f2 = plt.figure(2)
    x_axis = file2['No']
    y_axis = file2[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Changping")
    plt.ylabel(type)
    run()
elif city == "Dingling":
    f3 = plt.figure(3)
    x_axis = file3['No']
    y_axis = file3[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Dingling")
    plt.ylabel(type)
    run()
elif city == "Dongsi":
    f4 = plt.figure(4)
    x_axis = file4['No']
    y_axis = file4[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Dongsi")
    plt.ylabel(type)
    run()
elif city == "Guanyuan":
    f5 = plt.figure(5)
    x_axis = file5['No']
    y_axis = file5[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Guanyuan")
    plt.ylabel(type)
    run()
elif city == "Gucheng":
    f6 = plt.figure(6)
    x_axis = file6['No']
    y_axis = file6[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Gucheng")
    plt.ylabel(type)
    run()
elif city == "Huairou":
    f7 = plt.figure(7)
    x_axis = file7['No']
    y_axis = file7[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Huairou")
    plt.ylabel(type)
    run()
elif city == "Nongzhanguan":
    f8 = plt.figure(8)
    x_axis = file8['No']
    y_axis = file8[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Nongzhanguan")
    plt.ylabel(type)
    run()
elif city == "Shunyi":
    f9 = plt.figure(9)
    x_axis = file9['No']
    y_axis = file9[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Shunyi")
    plt.ylabel(type)
    run()
elif city == "Tiantan":
    f10 = plt.figure(10)
    x_axis = file10['No']
    y_axis = file10[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Tiantan")
    plt.ylabel(type)
    run()
elif city == "Wanliu":
    f11 = plt.figure(11)
    x_axis = file11['No']
    y_axis = file11[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Wanliu")
    plt.ylabel(type)
    run()
elif city == "Wanshouxigong":
    f12 = plt.figure(12)
    x_axis = file12['No']
    y_axis = file12[type]
    plt.plot(x_axis, y_axis)
    plt.xlabel("Wanshouxigong")
    plt.ylabel(type)
    run()
else:
    exit()


