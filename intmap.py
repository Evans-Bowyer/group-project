import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# csv_files = []
# def get_csv(path):
#     for csv in os.listdir(path):
#         if os.path.isfile(os.path.join(path, csv)):
#             yield csv
#
# for csv in get_csv(r'C:\Users\andre\OneDrive\Desktop\group-project\Graphdata'):
# 	csv_files.append(csv)
#
# df_csv_append = pd.DataFrame()
# print(csv_files[0])
#
# for file in csv_files:
# 	df = pd.read_csv(r'C:\Users\andre\OneDrive\Desktop\group-project\Graphdata\\'+file)
# 	df_csv_append = df_csv_append.append(df)
#
# print(df_csv_append.set_index('station'))

path=r'C:\Users\andre\OneDrive\Desktop\group-project\China_shapefiles\china_country.shp'
geo_china = gpd.read_file(path)
geo_china.plot()
plt.xlabel('geo-x')
plt.title('Pollution in China over Time')
plt.show()

