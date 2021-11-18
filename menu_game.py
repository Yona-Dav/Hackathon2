from game import CountryCategory,Player,NumberPoints,CoktailCategory, FruitCategory



def main():
    count=int()
    print('*****************************\n* Welcome to the Guess game * \n*****************************')

    while True:
        print('''
        P. Play the Game
        H. How to play?
        A. My Account
        X. Exit
        ''')
        choice = input('What do you want to do? ')
        if choice in 'xX':
            print(f'Goodbye')
            break
        elif choice in 'Hh':
            print('''
            The goal of this game is to find the word
            How?
            First, you have to choice a category and a level.
            Each level has a different number of points (easy=10, intermediate=7, hard=
            4)
            In order to find the word, the computer can give you clues in exchange a price.
            If you find the word, you score will raise by the number of points that left.
            If you lose, you can play again.
            
            Good Luck !!!
            ''')
        elif choice in 'Aa':
            player = Player()
            if player.check_login_in() !='none':
                while True:
                    print('''
                    S. View my Score
                    D. Delete my account
                    X. Exit''')
                    ans = input('Enter your choice: ')
                    if ans in 'Ss':
                        player.show_score()
                    elif ans in 'Dd':
                        player.delete_player()
                    elif ans in 'Xx':
                        break
        elif choice in 'Pp':
            new_player = Player()
            if new_player.check_login_in() == 'none':
                break
            else:
                while True:
                    print("\nChoose a level")
                    print('''
                    1. Easy
                    2. Intermediate
                    3. Hard\n''')

                    print('Choose a category')
                    print('''
                    1. Country
                    2. Coktail
                    3. Fruits
                    X. Exit''')
                    level1 = input('Your level: ')
                    choice2 = input('Your category: ')
                    if choice2 == '1':
                        country_init = CountryCategory()
                        country_to_guess= country_init.country
                        new_player.level(level1)
                        while True:
                            new_player.show_points()
                            if new_player.count ==0:
                                print(f'\nYou lose... The country was {country_init}')
                                break
                            else:
                                print('''
                                Y. Your answer (if you are wrong, your points will decrease by 1)
                                Some clues to help you:
                                (For each clue used, your points will decrease by 1)
                                1. The first letter of the country
                                2. The last letter of the country
                                3. The length of the country
                                4. The capital of the country
                                5. The continent where the country is
                                6. The subregion where the country is (the value is 2 points)
                                7. The number of inhabitants of the country
                                X. Exit''')
                                choice3= input('Enter your choice:  ')
                                if choice3 in 'Yy':
                                    word_guess = input('The country is: ')
                                    if word_guess.lower() == country_to_guess.lower():
                                        print(f'Congrats {new_player.username}! You find the country!')
                                        print(f'You won {new_player.count} points')
                                        new_player.update_score(new_player.count)
                                        new_player.show_score()
                                        break
                                    else:
                                        print('This is not the good country, you lose one point')
                                        new_player.decrease_point()
                                elif choice3=='1':
                                    country_init.first_letter()
                                    new_player.decrease_point()
                                elif choice3=='2':
                                    country_init.last_letter()
                                    new_player.decrease_point()
                                elif choice3=='3':
                                    country_init.length_word()
                                    new_player.decrease_point()
                                elif choice3=='4':
                                    if country_init.capital() != 'n':
                                        new_player.decrease_point()
                                elif choice3=='5':
                                    country_init.continent()
                                    new_player.decrease_point()
                                elif choice3=='7':
                                    country_init.population()
                                    new_player.decrease_point()
                                elif choice3=='6':
                                    country_init.subregion()
                                    new_player.decrease_point()
                                    new_player.decrease_point()
                                elif choice3 in 'xX':
                                    print(f'\nYou lose... The country was {country_init}')
                                    break
                    elif choice2 =='2':
                        coktail_init = CoktailCategory()
                        coktail_to_guess= coktail_init.coktail
                        new_player.level(level1)
                        while True:
                            new_player.show_points()
                            if new_player.count ==0:
                                print(f'\nYou lose... The coktail was {coktail_init}')
                                break
                            else:
                                print('''
                                Y. Your answer (if you are wrong, your points will decrease by 1)
                                Some clues to help you:
                                (For each clue used, your points will decrease by 1)
                                1. The first letter of the coktail
                                2. The last letter of the coktail
                                3. The length of the coktail
                                4. The first ingredient
                                5. The second ingredient
                                6. The third ingredient
                                X. Exit''')
                                choice4= input('Enter your choice:  ')
                                if choice4 in 'Yy':
                                    coktail_guess = input('The coktail is: ')
                                    if coktail_guess.lower() == coktail_to_guess.lower():
                                        print(f'Congrats {new_player.username}! You find the coktail!')
                                        print(f'You won {new_player.count} points')
                                        new_player.update_score(new_player.count)
                                        new_player.show_score()
                                        break
                                    else:
                                        print('This is not the good coktail, you lose one point')
                                        new_player.decrease_point()
                                elif choice4=='1':
                                    coktail_init.first_letter()
                                    new_player.decrease_point()
                                elif choice4=='2':
                                    coktail_init.last_letter()
                                    new_player.decrease_point()
                                elif choice4=='3':
                                    coktail_init.length_word()
                                    new_player.decrease_point()
                                elif choice4=='4':
                                    coktail_init.ingredient_one()
                                    new_player.decrease_point()
                                elif choice4=='5':
                                    coktail_init.ingredient_two()
                                    new_player.decrease_point()
                                elif choice4=='6':
                                    coktail_init.ingredient_three()
                                    new_player.decrease_point()
                                elif choice4 in 'xX':
                                    print(f'\nYou lose... The coktail was {coktail_init}')
                                    break
                    elif choice2 =='3':
                        fruit_init = FruitCategory()
                        fruit_to_guess= fruit_init.fruit
                        new_player.level(level1)
                        while True:
                            new_player.show_points()
                            if new_player.count ==0:
                                print(f'\nYou lose... The fruit was {fruit_init}')
                                break
                            else:
                                print('''
                                A. Your Answer (if you are wrong, your points will decrease by 1)
                                Some clues to help you:
                                (For each clue used, your points will decrease by 1)
                                1. The first letter of the fruit
                                2. The last letter of the fruit
                                3. The length of the word
                                4. The genus of this fruit
                                5. The family of this fruit
                                6. The calorie in this fruit
                                7. The sugar in this fruit
                                X. Exit''')
                                choice5= input('Enter your choice:  ')
                                if choice5 in 'Aa':
                                    fruit_guess = input('The coktail is: ')
                                    if fruit_guess.lower() == fruit_to_guess.lower():
                                        print(f'Congrats {new_player.username}! You find the Fruit!')
                                        print(f'You won {new_player.count} points')
                                        new_player.update_score(new_player.count)
                                        new_player.show_score()
                                        break
                                    else:
                                        print('This is not the good fruit, you lose one point')
                                        new_player.decrease_point()
                                elif choice5=='1':
                                    fruit_init.first_letter()
                                    new_player.decrease_point()
                                elif choice5=='2':
                                    fruit_init.last_letter()
                                    new_player.decrease_point()
                                elif choice5=='3':
                                    fruit_init.length_word()
                                    new_player.decrease_point()
                                elif choice5=='4':
                                    fruit_init.genus_of_fruit()
                                    new_player.decrease_point()
                                elif choice5=='5':
                                    fruit_init.family_of_fruit()
                                    new_player.decrease_point()
                                elif choice5=='6':
                                    fruit_init.calories_fruit()
                                    new_player.decrease_point()
                                elif choice5=='7':
                                    fruit_init.sugar_fruit()
                                    new_player.decrease_point()
                                elif choice5 in 'xX':
                                    print(f'\nYou lose... The fruit was {fruit_init}')
                                    break
                    elif choice2 in 'Xx':
                        break
       

main()