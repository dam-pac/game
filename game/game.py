f = open("logs", "w")
f.close()
import ctypes
import os
from Ukraine_RU import *
from game_resources import *
import sys
import random
import pygame
import time
from colorama import Fore, Back, Style, init
time.sleep(2)
init()
pygame.init()

success_sound = pygame.mixer.Sound('556c49a24bb675c.mp3')
accept_sound = pygame.mixer.Sound('3bd3287f1db401a.mp3')
success_sound.play()
print(admin_check_message_success)
time.sleep(1)
from rules import *
check_rules()
accept_sound.play()
start_options = menu()
time.sleep(2)
exit_exit_exit = False
reserv_s_opt = prog_in_text_file()
while exit_exit_exit == False:
    if start_options == 1 and reserv_s_opt == 1:
        continue_game = 'yes'
        pygame.mixer.music.load('48bb90af8e1e401.mp3')
        pygame.mixer.music.play(-1)
        count = 0
        game_over = 0
        sound_incorrect = pygame.mixer.Sound('jg-032316-sfx-feedback-incorrect-6.mp3')
        sound_correct = pygame.mixer.Sound('line_open.mp3')
        game_over_sound = pygame.mixer.Sound('1afb121d14c2b36.mp3')
        while continue_game == 'yes':
            if count >= 10:
                continue_game = 'no'
                f = open('save', 'w+')
                f.write('2')
                f.close()
                print('SAVING...')
                start_options = 2
                time.sleep(1)
            else:
                print(Fore.YELLOW)
                print(Back.CYAN)
                print(Style.BRIGHT)
                os.system('cls')
                a = random.randrange(10, 99)
                b = random.randrange(10, 99)
                c = a + b
                game_title()
                print(f'Count: {count}')
                if count < 0:
                    continue_game = 'no'
                    game_over = 1
                    pygame.mixer.music.stop()
                    game_over_sound.play()
                    time.sleep(1)
                    from game_exit import *
                    exit = exit_with_game_over_stage_1()
                    pygame.mixer.music.stop()
                    exit_choice(exit)
                elif count > 5:
                    a = random.randrange(10,99)
                    b = random.randrange(10,99)
                    c = random.randrange(1,10)
                    d = (a+b)*c
                    print(f'RULES: {rules_calc_1}')
                    stage_rules_1()
                    print(f'Count: {count}')
                    if d == int(input(f'   ({a} + {b}) * {c} = ')):
                        print(Back.GREEN)
                        print('YEA!')
                        count += 1
                        sound_correct.play()
                        time.sleep(1)
                    else:
                        print(Back.RED)
                        print('WRONG!')
                        count -= 1
                        sound_incorrect.play()
                        time.sleep(1)
                elif count >= 0 <= 5:
                    print(f'RULES: {rules_calc}')
                    if c == int(input(f'  {a}  +  {b}  =  ')):
                        print(Fore.GREEN)
                        print('Yea!')
                        count += 1
                        sound_correct.play()
                        time.sleep(1)
                    else:
                        print(Fore.RED)
                        print('WRONG!')
                        count -= 1
                        sound_incorrect.play()
                        time.sleep(1)
        pygame.mixer.music.stop()
    elif start_options == 2 or reserv_s_opt == 2:
        pygame.mixer.music.stop()
        sound_mess = pygame.mixer.Sound('eac678556f1275c.mp3')
        EBSFJBLCSJ = pygame.mixer.Sound('8Vnxv5Xg.mp3')
        continue_game = 'yes'
        print(Back.BLACK)
        os.system('CLS')
        time.sleep(3)
        while continue_game == 'yes':
            print(Back.LIGHTYELLOW_EX)
            print(Style.DIM)
            print(Fore.BLACK)
            os.system('CLS')
            sound_mess.play()
            print(f'\n\n\n\n\n\n\n\n\n\n\n                              {game_2_words_1}', end=' ')
            time.sleep(2)
            sound_mess.play()
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_2}', end=' ')
            time.sleep(2)
            print(Back.LIGHTYELLOW_EX, end=' ')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(Back.LIGHTYELLOW_EX, end=' ')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(game_2_words_3, end=' ')
            time.sleep(1)
            print(f'{game_2_words_4}')
            sound_mess.play()
            print(f'\n                {game_2_words_5}', end=' ')
            time.sleep(1)
            sound_mess.play()
            print(Back.RED, end='')
            print(Fore.LIGHTWHITE_EX, end='')
            print(f'{game_2_words_6}', end='')
            time.sleep(1)
            sound_mess.play()
            print(Back.LIGHTYELLOW_EX, end=' ')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'{game_2_words_7}')
            time.sleep(4)
            os.system('CLS')
            sound_mess.play()
            print(f'\n\n\n\n\n\n\n\n\n\n\n                              {game_2_words_8}',end=' ')
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_9}', end=' ')
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'{game_2_words_10}')
            print(f'                                            {game_2_words_11}')
            os.system('cls')
            print(f'\n\n\n\n\n\n\n\n\n\n\n                    {game_2_words_12}')
            print(f'                       {game_2_words_13}')
            print(f'                       {game_2_words_14}')
            print(f'                       {game_2_words_15}')
            print(f'                       {game_2_words_16}')
            time.sleep(4)
            sound_mess.play()
            os.system('cls')
            pygame.mixer.music.load('f2758e2b277d486.mp3')
            pygame.mixer.music.play(-1)
            print(f'\n\n\n\n\n\n\n\n\n\n\n                       {game_2_words_17}', end=" ")
            print(f'{game_2_words_18}', end=" ")
            print(f'{game_2_words_19}')
            time.sleep(4)
            sound_mess.play()
            os.system('cls')
            print(f'\n\n\n\n\n\n\n\n\n\n\n                       {game_2_words_20}', end=" ")
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_21}', end=" ")
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'{game_2_words_22}')
            time.sleep(4)
            sound_mess.play()
            print(f'                       {game_2_words_23}', end=" ")
            print(f'{game_2_words_24}')
            time.sleep(3)
            sound_mess.play()
            print(f'                           {game_2_words_25}')
            time.sleep(1)
            sound_mess.play()
            print(f'                       {game_2_words_26}')
            time.sleep(4)
            sound_mess.play()
            os.system('cls')
            print(f'\n\n\n\n\n\n\n\n\n\n\n                       {game_2_words_27}', end=" ")
            print(f'{game_2_words_28}', end=" ")
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_29}', end=" ")
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'{game_2_words_30}')
            time.sleep(4)
            sound_mess.play()
            os.system('cls')
            print('\n\n\n\n\n\n\n\n\n\n\n                       ', end="")
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_31}', end=" ")
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'{game_2_words_32}')
            time.sleep(3)
            sound_mess.play()
            print(f'                           {game_2_words_33}')
            time.sleep(2)
            sound_mess.play()
            os.system('cls')
            print(f'\n\n\n\n\n\n\n\n\n\n\n                           ', end="")
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_34}')
            time.sleep(2)
            sound_mess.play()
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'                             ', end="")
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_35}')
            time.sleep(2)
            sound_mess.play()
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'                               ', end="")
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_36}')
            time.sleep(2)
            sound_mess.play()
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'                                ', end="")
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_37}')
            time.sleep(4)
            sound_mess.play()
            pygame.mixer.music.stop()
            os.system('cls')
            print(f'\n\n\n\n\n\n\n\n\n\n\n                           ', end="")
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'{game_2_words_38}')
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            time.sleep(2)
            EBSFJBLCSJ.play()
            print(f'\n\n                           {game_2_words_39}')
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end="")
            print(Fore.BLACK)
            time.sleep(3)
            os.system('CLS')
            user1 = generate_users()
            user2 = generate_users()
            user3 = generate_users()
            user4 = generate_users()
            user5 = generate_users()
            user6 = generate_users()
            user7 = generate_users()
            user8 = generate_users()
            user9 = generate_users()
            user10 = generate_users()
            user11 = generate_users()
            user12 = generate_users()
            user13 = generate_users()
            user14 = generate_users()
            user15 = generate_users()
            def check1(user):
                if int(user['age']) > 30:
                    check_user = 'y'
                    return check_user
                else:
                    check_user = 'n'
                    return check_user
            check_user1 = check1(user1)
            check_user2 = check1(user2)
            check_user3 = check1(user3)
            check_user4 = check1(user4)
            check_user5 = check1(user5)
            def check2(user):
                if int(user['weight']) < 65:
                    k = user['name']
                    if len(k) < 7:
                        check_user = 'y'
                        return check_user
                    else:
                        check_user = 'n'
                        return check_user
                else:
                    check_user = 'n'
                    return check_user
            check_user6 = check2(user6)
            check_user7 = check2(user7)
            check_user8 = check2(user8)
            check_user9 = check2(user9)
            check_user10 = check2(user10)
            def check3(user):
                if user['countries'] == 'China' or user['countries'] =='France' or user['countries'] == 'Ukraine' or user['countries'] == 'GB':
                    check_user = 'y'
                    return check_user
                else:
                    check_user = 'n'
                    return check_user
            check_user11 = check3(user11)
            check_user12 = check3(user12)
            check_user13 = check3(user13)
            check_user14 = check3(user14)
            check_user15 = check3(user15)
            sound_correct = pygame.mixer.Sound('04074e9d884d65b.mp3')
            game_over_sound = pygame.mixer.Sound('d1f1942fc5ee7a4.mp3')
            pygame.mixer.music.load('f53d60999306760.mp3')
            print(f'{game_2_rules_1}')
            input(f'{game2_ready}')
            pygame.mixer.music.play(-1)
            os.system('CLS')
            continue_game1 = 'yes'
            const = 0
            while continue_game1 == 'yes':
                os.system('CLS')
                if const == 0:
                    print(f'{game_2_rules_1}')
                    game2interface(user1)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user1 and end <= 10:
                        const += 1
                    else:
                        continue_game1 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 1:
                    print(f'{game_2_rules_1}')
                    game2interface(user2)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user2 and end <= 10:
                        const += 1
                    else:
                        continue_game1 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 2:
                    print(f'{game_2_rules_1}')
                    game2interface(user3)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user3 and end <= 10:
                        const += 1
                    else:
                        continue_game1 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 3:
                    print(f'{game_2_rules_1}')
                    game2interface(user4)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user4 and end <= 10:
                        const += 1
                    else:
                        continue_game1 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 4:
                    print(f'{game_2_rules_1}')
                    game2interface(user5)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user5 and end <= 10:
                        const += 1
                    else:
                        continue_game1 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 5:
                    pygame.mixer.music.stop()
                    continue_game1 = 'no'
                    continue_game2 = 'yes'
            pygame.mixer.music.load('3932c33f1c69fdf.mp3')
            print(f'{game_2_rules_2}')
            input(f'{game2_ready}')
            pygame.mixer.music.play(-1)
            while continue_game2 == 'yes':
                os.system('CLS')
                if const == 5:
                    print(f'{game_2_rules_2}')
                    game2interface(user6)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user6 and end <= 12:
                        const += 1
                    else:
                        continue_game2 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 6:
                    print(f'{game_2_rules_2}')
                    game2interface(user7)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user7 and end <= 12:
                        const += 1
                    else:
                        continue_game2 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 7:
                    print(f'{game_2_rules_2}')
                    game2interface(user8)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user8 and end <= 12:
                        const += 1
                    else:
                        continue_game2 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 8:
                    print(f'{game_2_rules_2}')
                    game2interface(user9)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user9 and end <= 12:
                        const += 1
                    else:
                        continue_game2 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 9:
                    print(f'{game_2_rules_2}')
                    game2interface(user10)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user10 and end <= 12:
                        const += 1
                    else:
                        continue_game2 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 10:
                    continue_game2 = 'no'
                    continue_game3 = 'yes'
                    pygame.mixer.music.stop()
            pygame.mixer.music.load('20f52df178205f2.mp3')
            print(f'{game_2_rules_3}')
            input(f'{game2_ready}')
            pygame.mixer.music.play(-1)
            while continue_game3 == 'yes':
                os.system('CLS')
                if const == 10:
                    print(f'{game_2_rules_3}')
                    game2interface(user11)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user11 and end <= 5:
                        const += 1
                    else:
                        continue_game3 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 11:
                    print(f'{game_2_rules_3}')
                    game2interface(user12)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user12 and end <= 5:
                        const += 1
                    else:
                        continue_game3 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 12:
                    print(f'{game_2_rules_3}')
                    game2interface(user13)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user13 and end <= 5:
                        const += 1
                    else:
                        continue_game3 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 13:
                    print(f'{game_2_rules_3}')
                    game2interface(user14)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user14 and end <= 5:
                        const += 1
                    else:
                        continue_game3 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 14:
                    print(f'{game_2_rules_3}')
                    game2interface(user15)
                    start = time.time()
                    answer = input(f'{game2_answer}')
                    end = time.time() - start
                    if answer == check_user15 and end <= 5:
                        const += 1
                    else:
                        continue_game3 = 'no'
                        game_over = 1
                        pygame.mixer.music.stop()
                        game_over_sound.play()
                        time.sleep(1)
                        from game_exit import *
                        exit = exit_with_game_over_stage_2()
                        pygame.mixer.music.stop()
                        exit_choice(exit)
                elif const == 15:
                    pygame.mixer.music.stop()
                    continue_game3 = 'no'
                    continue_game = 'no'
                    f = open('save', 'w+')
                    f.write('3')
                    f.close()
                    print('SAVING...')
                    time.sleep(3)
                    start_options = 3
                    reserv_s_opt = 3
    elif start_options == 3 or reserv_s_opt == 3:
        print('You WON! Beta has ended. Goodbay!')
        input('exit')
        time.sleep(5)
        break
            #RULES: Разрешать только тому, кому больше 16 лет и имеется нормальная или 1 проблема в психике, в течении 10 секунд
            #RULES: Разрешать за 12 секунд только тому, у кого вес менее 50 кг, и только тому, у кого имя и фамилия имеют количество букв менее 12
            #RULES: Разрешать за 5 секунд только тем, у кого iq выше твоего (0+10)
    else:
        input('')
