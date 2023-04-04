import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import xarray as xr

init_yr = 2013
fig, ax = plt.subplots()
ds = xr.open_dataset(f'data/PM_2.5/CHAP_PM2.5_Y1K_{init_yr}_V4.nc')
df = ds.to_dataframe()
df = df.reset_index(drop=False).dropna()
df.plot.hexbin(x='lon', y='lat', ax=ax, C='PM2.5', gridsize=(120,120), cmap='plasma',
               title=f'PM 2.5 Pollution in China, {init_yr}',
               xlabel='Longitude', ylabel='Latitude')
plt.subplots_adjust(left=0.25, bottom=0.25)
yr_ax = fig.add_axes([0.17, 0.1, 0.65, 0.03])
yr_slider = Slider(ax=yr_ax, label='Year',valmin=2013, valmax=2021, valinit=2013, valstep=1)
plt.show()
