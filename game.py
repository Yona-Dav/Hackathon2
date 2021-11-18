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

class NumberPoints:
    ''''
    The NumberPoints class allow us to count the points
    '''
    count =int()
    def level(self,level='1'):
        if level=='1':
            self.count = 10
        elif level=='2':
            self.count = 7
        elif level=='3':
            self.count = 4

    def decrease_point(self):
        self.count = self.count - 1
        return self.count

    def show_points(self):
        print(f'You have {self.count} points left\n')
    
    def __int__(self):
        return self.count
    

class Player(NumberPoints):
    '''
    The Player Class is a kind of login plateform
    '''
    def __init__(self):
        self.username = input('Enter your username ')
        self.password = input('Enter your password ')

    def check_login_in(self):
        query = f"select * from players where username ='{self.username}' and password='{self.password}'"
        user = run_query(query,'ra')
        if len(user) != 0:
            print(f'Welcome back {self.username}')
        else:
            print('To play the game, you must have an account')
            signup = input('Would you like to sign up?Y/N ')
            if signup in ['N','n']:
                print('Goodbye')
                return 'none'
            else:
                self.username = input('Enter your username ')
                query = f"select username from players where username ='{self.username}'"
                name = run_query(query,'ra')
                while len(name)!=0 or len(self.username)<2:
                    print('This username is already taken or is not valid')
                    self.username = input('Enter your username ')
                    query = f"select username from players where username ='{self.username}'"
                    name = run_query(query,'ra')
                self.password = input("Enter your password ")
                self.save()
                print(f'Welcome {self.username}!')
        
    def save(self):
        query = f"INSERT INTO players (username, password, points) VALUES ('{self.username}', '{self.password}', 0)"
        run_query(query)

    def show_score(self):
        query = f"select points from players where username='{self.username}' and password='{self.password}'"
        score = run_query(query,'r1')[0]
        print(f"Your score: {score} points")

    def score(self):
        query = f"select points from players where username='{self.username}' and password='{self.password}'"
        number_score = run_query(query,'r1')[0]
        return number_score


    def update_score(self,points):
        query = f"update players set points = {self.score()+points}where username='{self.username}' and password='{self.password}'"
        run_query(query)

    def delete_player(self):
        query = f"delete from players where username='{self.username}' and password='{self.password}'"
        run_query(query)
        print('You account was deleted')




    
        
class CountryCategory:
    '''
    The CountryCategory class gives us all the informations about the coktail that the computer randomly choosed
    '''
    country = ''
    def __init__(self):
        x = random.randint(1,(self.length_db())+1)
        query = f'select name from countries where country_id={x}'
        self.country = run_query(query,'r1')[0]

    def length_db(self):
        query =f'select count(*) from countries'
        length = run_query(query,'ra')[0][0]
        return length


    def first_letter(self):
        print(f'The first letter is : {self.country[0]}')

    def last_letter(self):
        print(f'The last letter is: {self.country[-1]}')
    
    def length_word(self):
        print(f'The length of the word is: {len(self.country)}')

    def capital(self):
        query = f"select capital from countries where name='{self.country}'"
        capital = run_query(query,'r1')[0]
        print(f'The capital of this country is: {capital}')
        return capital

    def continent(self):
        query = f"select continent from countries where name='{self.country}'"
        continent = run_query(query,'r1')[0]
        print(f'This country is in {continent}')

    def subregion(self):
        query = f"select subregion from countries where name='{self.country}'"
        subregion = run_query(query,'r1')[0]
        print(f'This country is in {subregion}')

    def population(self):
        query = f"select population from countries where name='{self.country}'"
        population = run_query(query,'r1')[0]
        print(f'This country has about {population} inhabitants')

    def __str__(self):
        return self.country

    def __repr__(self):
        return self.country



class CoktailCategory:
    '''
    The FruitCategory class gives us all the informations about the fruit that the computer randomly choosed
    '''
    coktail = ''
    def __init__(self):
        x = random.randint(1,self.length_db()+1)
        query = f'select name from coktails where coktail_id={x}'
        self.coktail = run_query(query,'r1')[0]
    
    def length_db(self):
        query =f'select count(*) from coktails'
        length = run_query(query,'ra')[0][0]
        return length

    def first_letter(self):
        print(f'The first letter is : {self.coktail[0]}')

    def last_letter(self):
        print(f'The last letter is: {self.coktail[-1]}')
    
    def length_word(self):
        print(f'The length of the word is: {len(self.coktail)}')

    def ingredient_one(self):
        query = f"select ingredient1 from coktails where name='{self.coktail}'"
        ingredient1 = run_query(query,'r1')[0]
        print(f'One of the ingredient is {ingredient1}')

    def ingredient_two(self):
        query = f"select ingredient2 from coktails where name='{self.coktail}'"
        ingredient2 = run_query(query,'r1')[0]
        print(f'One of the ingredient is {ingredient2}')

    def ingredient_three(self):
        query = f"select ingredient3 from coktails where name='{self.coktail}'"
        ingredient3 = run_query(query,'r1')[0]
        print(f'One of the ingredient is {ingredient3}')

    def __str__(self):
        return self.coktail

    def __repr__(self):
        return self.coktail


class FruitCategory:
    '''
    The CoktailCategory class gives us all the informations about the country that the computer randomly choosed
    '''
    fruit = ''
    def __init__(self):
        x = random.randint(1,self.length_db()+1)
        query = f'select name from fruits where fruit_id={x}'
        self.fruit = run_query(query,'r1')[0]
    
    def length_db(self):
        query =f'select count(*) from fruits'
        length = run_query(query,'ra')[0][0]
        return length

    def first_letter(self):
        print(f'The first letter is : {self.fruit[0]}')

    def last_letter(self):
        print(f'The last letter is: {self.fruit[-1]}')
    
    def length_word(self):
        print(f'The length of the word is: {len(self.fruit)}')

    def genus_of_fruit(self):
        query = f"select genus from fruits where name='{self.fruit}'"
        genus = run_query(query,'r1')[0]
        print(f'The genus of this fruit is {genus}')

    def family_of_fruit(self):
        query = f"select family from fruits where name='{self.fruit}'"
        family = run_query(query,'r1')[0]
        print(f'The family of this fruit is {family}')

    def calories_fruit(self):
        query = f"select calories from fruits where name='{self.fruit}'"
        calories = run_query(query,'r1')[0]
        print(f'There are {calories} calories in this fruit')

    def sugar_fruit(self):
        query = f"select sugar from fruits where name='{self.fruit}'"
        sugar = run_query(query,'r1')[0]
        print(f'The quantity of sugar is: {sugar}')

    def __str__(self):
        return self.fruit

    def __repr__(self):
        return self.fruit

