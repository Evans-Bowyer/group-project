import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import xarray as xr

datasets = {}
for year in range(2013, 2022):
    filename = f"data/PM_2.5/CHAP_PM2.5_Y1K_{year}_V4.nc"
    datasets[year] = xr.open_dataset(filename).to_dataframe().reset_index(drop=False).dropna()

fig, ax = plt.subplots(figsize=(8,6), num='PM 2.5 Pollution in China')
init_yr = 2013
df = datasets[init_yr]
hb = df.plot.hexbin(x='lon', y='lat', ax=ax, C='PM2.5', gridsize=(120,120),
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
plt.show()

