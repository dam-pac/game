import os
import time
from Ukraine_RU import *
import random
def linies():
    print('#########################################################################################################################                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      #########################################################################################################################')
    print('#########################################################################################################################                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      #########################################################################################################################')
    print('#########################################################################################################################                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      ##                                                                                                                      #########################################################################################################################')                                                                                                                     #########################################################################################################################')

def game_title():
    print('----------------------------------------------------------------------------------')
    print('|                                    GAME                                        |')
    print('----------------------------------------------------------------------------------')
def stage_rules_1():
    a = [1,2]
    for i in a:
        os.system('cls')
        time.sleep(0.5)
        game_title()
        print(f'RULES: {rules_calc_1}')
        time.sleep(0.5)
def menu():
    import pygame
    pygame.mixer.music.load('3d20874f20174bd.mp3')
    pygame.mixer.music.play(-1)
    from colorama import Fore, Back, Style, init
    import os
    from Ukraine_RU import menu_words_1, menu_input_words_1, prog_in_text_file
    import sys
    from game_exit import game_exit
    init()
    print(Back.LIGHTGREEN_EX)
    print(Fore.LIGHTWHITE_EX)
    os.system('cls')
    print('\n\n\n\n\n\n\n\n                                        ░██████╗░░█████╗░██╗░░██╗██╗░░░██╗░█████╗░')
    print('                                        ██╔═══██╗██╔══██╗██║░░██║██║░░░██║██╔══██╗')
    print('                                        ██║██╗██║██║░░██║███████║██║░░░██║██║░░╚═╝')
    print('                                        ╚██████╔╝██║░░██║██╔══██║██║░░░██║██║░░██╗')
    print('                                        ░╚═██╔═╝░╚█████╔╝██║░░██║╚██████╔╝╚█████╔╝')
    print('                                        ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░╚═════╝░░╚════╝░')
    print(f'\n\n\n\n\n {menu_words_1}')
    choice = input(f'\n\n {menu_input_words_1}')
    save = prog_in_text_file()
    if choice == '1':
        return 1
    elif choice == '2':
        return save
    else:
        game_exit()
game2age = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
game2nameM = ['Aaron', 'Abraham', 'Adam', 'Adrian', 'Aidan', 'Alan', 'Albert', 'Alejandro', 'Alex', 'Alexander', 'Alfred', 'Andrew', 'Angel', 'Anthony', 'Antonio', 'Ashton', 'Austin', 'Benjamin', 'Bernard', 'Blake', 'Brandon', 'Brian', 'Bruce', 'Bryan', 'Cameron', 'Carl', 'Carlos', 'Charles', 'Christopher', 'Cole', 'Connor', 'Caleb', 'Carter', 'Chase', 'Christian', 'Clifford', 'Cody', 'Colin', 'Curtis', 'Cyrus', 'Daniel', 'David', 'Dennis', 'Devin', 'Diego', 'Dominic', 'Donald', 'Douglas', 'Dylan', 'Edward', 'Elijah', 'Eric', 'Ethan', 'Evan', 'Francis', 'Fred', 'Gabriel', 'Gavin', 'Geoffrey', 'George', 'Gerld', 'Gilbert', 'Gordon', 'Graham', 'Gregory', 'Harold', 'Harry', 'Hayden', 'Henry', 'Herbert', 'Horace', 'Howard', 'Hugh', 'Hunter', 'Ian', 'Isaac', 'Isaiah', 'Jack', 'Jackson', 'Jacob', 'Jaden', 'Jake', 'James', 'Jason', 'Jayden', 'Jeffery', 'Jeremiah', 'Jesse', 'Jesus', 'John', 'Jonathan', 'Jordan', 'Jose', 'Joseph', 'Joshua', 'Juan', 'Julian', 'Justin', 'Keith', 'Kevin', 'Kyle', 'Landon', 'Lawrence', 'Leonars', 'Lewis', 'Logan', 'Louis', 'Lucas', 'Luke', 'Malcolm', 'Martin', 'Mason', 'Matthew', 'Michael', 'Miguel', 'Miles', 'Morgan', 'Nathan', 'Nathaniel', 'Neil', 'Nicholas', 'Noah', 'Norman', 'Oliver', 'Oscar', 'Oswald', 'Owen', 'Patrick', 'Peter', 'Philip', 'Ralph', 'Raymond', 'Reginald', 'Richard', 'Robert', 'Rodrigo', 'Roger', 'Ronald', 'Ryan', 'Samuel', 'Sean', 'Sebastian', 'Seth', 'Simon', 'Stanley', 'Steven', 'Thomas', 'Timoth', 'Tyler', 'Wallace', 'Walter', 'William', 'Wyatt', 'Xavier', 'Zachary']
game2nameW = ['Melanie', 'Florence', 'Agatha', 'Zoe', 'Rebecca', 'Ruth', 'Barbara', 'Amanda', 'Victoria', 'Irene', 'Miranda', 'Bridget', 'Sophia', 'Margaret', 'Katherine', 'Deborah', 'Emma']
game2countries = ['China', 'Russia', 'France', 'Germany', 'GB', 'USA', 'Japan', 'Ukraine', 'Belarus', 'Belgium']
game2weight = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63 , 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74 , 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91 , 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105 ,106 ,107 ,108 ,109, 110]
game2height = [179, 178, 177, 176, 175, 180, 181, 182, 183, 184, 185, 149, 148, 147, 146, 145, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 186 ,187 ,188, 189, 190, 191, 192 , 193, 194 , 195, 196]
def ages():
    k = len(game2age)
    k -= 1
    i = random.randint(0, k)
    i = game2age[i]
    return i
def names():
    a = random.randint(1,3)
    if a == 1 or a == 2:
        k = len(game2nameM)
        k -= 1
        i = random.randint(0, k)
        i = game2nameM[i]
        return i
    elif a == 3:
        k = len(game2nameW)
        k -= 1
        i = random.randint(0, k)
        i = game2nameW[i]
        return i
def generate_users():
    def countries():
        k = len(game2countries)
        k -= 1
        i = random.randint(0, k)
        i = game2countries[i]
        return i
    def weight():
        k = len(game2weight)
        k -= 1
        i = random.randint(0, k)
        i = game2weight[i]
        return i
    def height():
        k = len(game2height)
        k -= 1
        i = random.randint(0, k)
        i = game2height[i]
        return i
    age = ages()
    name = names()
    countries = countries()
    weight = weight()
    height = height()
    user = {'age' : f"{age}", 'name' : f"{name}", 'countries' : f"{countries}", 'weight' : f"{weight}", 'height' : f"{height}"}
    return user
def game2interface(user):
    def text1():
        print(f'  |  {game2_game_name}  |  |  {game2_game_age}  |')
        pass
    def text2():
        print(f'  |  {game2_game_countries}: ', end ="")
        pass
    def text3():
        print(f'  |  {game2_game_weight}  |  |  {game2_game_height}  |')
    text1()
    print(f'  |    {user["name"]}    |  |  {user["age"]}  |')
    text2()
    print(f'{user["countries"]}')
    text3()
    print(f'  |  {user["weight"]}  |  |  {user["height"]}  |')
