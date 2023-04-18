import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import xarray as xr
import pandas as pd

def create_map():
    datasets = {}
    for year in range(2013, 2022):
        filename = f"data/PM_2.5/CHAP_PM2.5_Y1K_{year}_V4.nc"
        df = xr.open_dataset(filename).to_dataframe().reset_index(drop=False).dropna()
        df = df.iloc[::500, :]
        datasets[year] = pd.DataFrame(df.values, columns=df.columns).dropna()

    fig, ax = plt.subplots(figsize=(8,6), num='PM 2.5 Pollution in China')
    init_yr = 2013
    df = datasets[init_yr]
    hb = df.plot.hexbin(x='lon', y='lat', ax=ax, C='PM2.5', gridsize=(60,60),
                   cmap='plasma', title=f'PM 2.5 Pollution in China, {init_yr}',
                   xlabel='Longitude', ylabel='Latitude')
    plt.subplots_adjust(left=0.25, bottom=0.25)
    yr_ax = fig.add_axes([0.17, 0.1, 0.65, 0.03])
    yr_slider = Slider(ax=yr_ax, label='Year',valmin=2013, valmax=2021,
                       valinit=2013, valstep=1)
    yr_slider.valtext.set_visible(False)
    yr_ax.add_artist(yr_ax.xaxis)
    yr_ticks = range(2013, 2022)
    yr_ax.set_xticks(yr_ticks)
    back_ax = fig.add_axes([0.03, 0.09, 0.08, 0.05])
    back = Button(back_ax, "Back")

    def return_to_start(val):
        plt.close()
        exit()

    def update(val):
        yr = int(yr_slider.val)
        hb.set_title(f'PM 2.5 Pollution in China, {yr}')
        df_new = datasets[yr]
        hb_collections = hb.collections[0]
        hb_collections.set_offsets(df_new[['lon', 'lat']].values)
        hb_collections.set_array(df_new['PM2.5'].values)
        hb.autoscale()
        fig.canvas.draw_idle()

    yr_slider.on_changed(update)
    back.on_clicked(return_to_start)
    plt.show()

create_map()

