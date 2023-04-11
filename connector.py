import PySimpleGUI as sg
import matplotlib
import os

# Selects a PySimpleGUI theme.
sg.theme('DarkTeal2')

def main():
    matplotlib.use('TkAgg')
    layout = [
        [sg.Text(f"Map or Graph")],

        [sg.Button('Map', size=(4, 2)),
         sg.Button('Graph', pad=(((14 / 1.152), 0), 3), size=(4, 2))]
    ]
    window = sg.Window('Patrolling Emission in China', layout, size=(330, 120))
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