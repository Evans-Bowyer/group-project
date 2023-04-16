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
         sg.Button('Graph', pad=(((14 / 2), 0), 3), size=(5, 2))]
    ]
    window = sg.Window('', layout, size=(300, 150))
    event, values = window.read()
    while event:
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            exit()
        if event == 'Graph':
            window.close()
            del window
            os.system('python maingraphs.py')
            break
        if event == 'Map':
            window.close()
            del window
            os.system('python intmap.py')
            os.system('python connector.py')
            break

if __name__ == '__main__':
    main()
