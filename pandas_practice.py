import pandas as pd

# create a dataframe from wikipedia 

def world_population():
    country_and_area = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area'
    country_and_population = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    country_and_population_density = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density'

    df_country_area = pd.read_html(country_and_area)
    df_country_area = df_country_area[1].iloc[:, 1:6]

    df_country_population = pd.read_html(country_and_population) 
    df_country_population = df_country_population.iloc[:, 1:6]


