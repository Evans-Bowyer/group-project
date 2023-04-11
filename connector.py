import PySimpleGUI as sg
import matplotlib
import os

# Selects a PySimpleGUI theme.
sg.theme('DarkTeal2')

def main():
    matplotlib.use('TkAgg')
    layout = [
        [sg.Text(f"Select Data Visualization Type:")],

        [sg.Button('Map', pad=(((14 / 2), 10), 3), size=(5, 2)),
         sg.Button('Graph', pad=(((80), 0), 3), size=(5, 2))]
    ]
    window = sg.Window('', layout, size=(220, 100))
    event, values = window.read()
    while event:
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            exit()
        if event == 'Graph':
            window.close()
            del window
            os.system('maingraphs.py')
            break
        if event == 'Map':
            os.system('intmap.py')

if __name__ == '__main__':
    main()