import requests
import json
import random
import psycopg2
from tabulate import tabulate


pg_details = {'host': 'localhost', 'user':'postgres', 'password': 'yoshir34', 'dbname':'GuessGame'}
def run_query(query, mode='w'):
    connection = psycopg2.connect(**pg_details)
    cursor = connection.cursor()
    cursor.execute(query)
    if mode == 'ra':
        results = cursor.fetchall()
    if mode == 'r1':
        results = cursor.fetchone()
    connection.commit()
    connection.close()
    if 'r' in mode :
        return results
    print('db update successfully')



def get_info_countries():
    url = 'https://restcountries.com/v3.1/all'
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        for country_data in data:
            capital = str(country_data.get('capital','none')[0]).replace("'", "")
            query = f"INSERT INTO countries (name, capital, continent, subregion, population) VALUES ('{country_data['name']['common']}', '{capital}','{country_data['continents'][0]}','{country_data.get('subregion', 'no subregion')}','{country_data['population']}') "
            run_query(query)
                
# get_info_countries()


def get_info_coktails():
    list_coktails = ['Margarita','Martini','Gin','Sidecar', 'Negroni','Cosmopolitan', 'Manhattan','Mojito', 'Bloody','Mai', 'Sazerac', 'Whiskey', 'Daiquiri']
    for i in list_coktails:
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={i}'
        data = requests.get(url)
        if data.status_code == 200:
            data = data.json()
            name = data['drinks'][0]['strDrink']
            category = data['drinks'][0]['strCategory'] 
            ingredient1 = data['drinks'][0]['strIngredient1']
            ingredient2 = data['drinks'][0]['strIngredient2']
            ingredient3 = data['drinks'][0]['strIngredient3']
            ingredient4 = data['drinks'][0]['strIngredient4']
            query = f"INSERT INTO coktails (name, category, ingredient1, ingredient2, ingredient3,ingredient4) VALUES ('{name}', '{category}','{ingredient1}','{ingredient2}','{ingredient3}','{ingredient4}') "
            run_query(query)

# get_info_coktails()

def get_info_fruits():
    url = 'https://www.fruityvice.com/api/fruit/all'
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        for fruit in data:
            query = f"INSERT INTO fruits (name, genus, family, calories, sugar) VALUES ('{fruit['name']}', '{fruit['genus']}','{fruit['family']}',{fruit['nutritions']['calories']},{fruit['nutritions']['sugar']}) "
            run_query(query)

# get_info_fruits()



 





