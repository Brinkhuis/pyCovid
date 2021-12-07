# imports
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import zipfile

# base url
base_url = 'https://data.rivm.nl/covid-19/'

# read csv
file_name = 'COVID-19_Infectieradar_symptomen_per_dag.csv'
try:
    print('Trying to read data from {} ...'.format(base_url))
    df = pd.read_csv(
        base_url + file_namee, 
        usecols = ['Date_of_statistics', 'Perc_covid_symptoms', 'MA_perc_covid_symptoms'], 
        parse_dates = ['Date_of_statistics'], 
        index_col = ['Date_of_statistics'], 
        sep = ';'
    )
    df.reset_index().to_csv('data/{}'.format(file_name), sep=';', index=False)
except:
    print('Reading data from {} failed. Now reading cached data from directory \'data\''.format(base_url))
    df = pd.read_csv(
        'data/{}'.format(file_name), 
        parse_dates = ['Date_of_statistics'], 
        index_col = ['Date_of_statistics'], 
        sep = ';'
    )    

# sample
print('Number of records read:', df.shape[0])
print('Most recent data      :', df.index[-1].date())
print()
print(df.tail(n=5))

# plot
df.plot(figsize=(10, 5))
plt.title('Infectieradar symptomen per dag')
plt.show()
