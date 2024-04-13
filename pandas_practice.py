import pandas as pd
import os
import requests
# create a dataframe from wikipedia 

def world_population():
    country_and_area = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area'
    country_and_population = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    country_and_population_density = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density'

    df_country_area = pd.read_html(country_and_area)
    df_country_area = df_country_area[1].iloc[:, 1:6]

    df_country_population = pd.read_html(country_and_population) 
    df_country_population = df_country_population[0].iloc[:, 1:6]

    df_country_population.loc[0, 'Location'] = 'Earth'

    df = df_country_area.merge(df_country_population, left_on='Country / dependency', right_on='Location', how='outer')
    df['Country / dependency'] = df['Country / dependency'].fillna(df['Location'])

    df.drop('Location', axis=1, inplace=True)

    os.mkdir('./data/world_dataframe')

    df.to_csv('./data/world_dataframe/world_area_population.csv', index=False)

def add_capital_city_to_csv():
    df = pd.read_csv('./data/world_dataframe/world_area_population.csv')
    df_capital = pd.read_html('https://geographyfieldwork.com/WorldCapitalCities.htm')
    df_capital = df_capital[2]
    
    df = df.merge(df_capital, left_on='Country / dependency', right_on='Country', how='left')

    df.drop('Country', axis=1, inplace=True)
    df.to_csv('./data/world_dataframe/world_area_population.csv', index=False)

def remove_comma_from_dataframe():
    df = pd.read_csv('./data/world_dataframe/world_area_population.csv')
    df.replace(',', '', regex=True, inplace=True)
    df.to_csv('./data/world_dataframe/world_area_population.csv', index=False)

def split_area_by_km_mi():
    df = pd.read_csv('./data/world_dataframe/world_area_population.csv')
    df.replace(r'[()]', '', regex=True, inplace=True)
    area = df['Total in km2 (mi2)'].str.split(' ',expand=True)
    df.insert(2, 'Total in km2', area[0])
    df.insert(3, 'Total in mi2', area[1])

    land = df['Land in km2 (mi2)'].str.split(' ',expand=True)
    df.insert(6, 'Land in km2', land[0])
    df.insert(7, 'Land in mi2', land[1])

    water = df['Water in km2 (mi2)'].str.split(' ',expand=True)
    df.insert(9, 'Water in km2', water[0])
    df.insert(10, 'Water in mi2', water[1])

    df.drop(['Total in km2 (mi2)', 'Land in km2 (mi2)', 'Water in km2 (mi2)'], axis=1, inplace=True)
    df.to_csv('./data/world_dataframe/world_area_population.csv', index=False)

def change_capital_column_loc():
    df = pd.read_csv('./data/world_dataframe/world_area_population.csv')
    df.insert(1, 'Capital', df['Capital City'])
    df.drop('Capital City', axis=1, inplace=True)
    df.to_csv('./data/world_dataframe/world_area_population.csv', index=False)
    
def add_region():
    df = pd.read_csv('./data/world_dataframe/world_area_population.csv')
    html = requests.get('https://www.ucl.ac.uk/global/regional-activity/countries-and-regions-directory').content

    data = pd.read_html(html)
    df_region = pd.concat([data[0], data[1]], ignore_index=True)

    df = df.merge(df_region, how='left', left_on='Country / dependency', right_on='COUNTRY')
    df.to_csv('./data/world_dataframe/world_area_population.csv', index=False)
add_region()