# blackjack game

from random import *

# gretting

print("welcome to 21 game ")
# money
player_money = 1000
player_bet = 0
bet_check = 0
# main function
def StartGame():
    # veriables

    # computer veriables
    computer_cards_sum = 0
    computer_cards1 = 0
    computer_cards2 = 0
    computer_cards3 = 0
    computer_cards4 = 0
    computer_cards5 = 0

    # player veriables

    player_cards_sum = 0
    player_cards1 = 0
    player_cards2 = 0
    player_cards3 = 0
    player_cards4 = 0
    player_cards5 = 0
    global player_bet, player_money, bet_check

    gemes_satatus = ""

    game_over21 = True

    game_satatus_check = ""

    while game_over21:
        if player_money > 0:
            print(f"currently money {player_money}")
            try :
                bet_check = int(input("enter your bet"))
            except :
                print("Enter your bet as number")
                StartGame()
            if bet_check <= player_money:
                player_bet = bet_check
            else:
                print("you dont have enaough money")
                StartGame()
                break

            games_satatus = input("the rules is basic may  you  want start , type y \n--> ")

            if games_satatus == "y":
                computer_cards1 = randint(2, 10)
                computer_cards_sum = computer_cards1
                computer_cards2 = randint(2, 10)
                print(f"computers cards : [ * , {computer_cards1} ] computer score {computer_cards_sum} ")

                player_cards1 = randint(2, 10)
                player_cards2 = randint(2, 10)
                player_cards_sum = player_cards1 + player_cards2
                print(f"your cards : [ {player_cards1} , {player_cards2} ] current score {player_cards_sum}")

                games_satatus = ""
                games_satatus = input("type y and get new card type n to pass \n--> ")

                if games_satatus == "y":
                    computer_cards3 = randint(2, 10)
                    computer_cards_sum = computer_cards3 + computer_cards1
                    print(
                        f"computer cards [ * , {computer_cards1} , {computer_cards3} ] computer score {computer_cards_sum}")

                    player_cards3 = randint(2, 10)
                    player_cards_sum = player_cards1 + player_cards2 + player_cards3
                    print(
                        f"your cards [ {player_cards1} , {player_cards2} , {player_cards3} ] currently score {player_cards_sum} ")

                    if player_cards_sum > 21:
                        print(" you lose , your score over 21 ")
                        player_money -= player_bet
                        print(f"currently money {player_money}")
                        game_satatus_check = input("do you want more time ? type y or n \n-->")

                        if game_satatus_check == "y":
                            StartGame()
                        elif game_satatus_check == "n":
                            game_over21 = False
                            break
                        else:
                            game_over21 = False
                            break

                    games_satatus = ""
                    games_satatus = input("type y and get new card type n to pass \n--> ")

                    if games_satatus == "y":
                        computer_cards4 = randint(2, 10)
                        computer_cards_sum = computer_cards3 + computer_cards1 + computer_cards4
                        print(
                            f"computer cards [ * , {computer_cards1} , {computer_cards3} , {computer_cards4} ] computer score {computer_cards_sum}")

                        player_cards4 = randint(2, 10)
                        player_cards_sum = player_cards1 + player_cards2 + player_cards3 + player_cards4
                        print(
                            f"your cards [ {player_cards1} , {player_cards2} , {player_cards3} , {player_cards4} ] currently score {player_cards_sum} ")
                        if player_cards_sum > 21:
                            print(" you lose , your score over 21 ")
                            player_money -= player_bet
                            print(f"currently money {player_money}")
                            game_satatus_check = input("do you want more time ? type y or n \n-->")

                            if game_satatus_check == "y":
                                StartGame()
                            elif game_satatus_check == "n":
                                game_over21 = False
                                break

                            else:
                                game_over21 = False
                                break

                        games_satatus = ""
                        games_satatus = input("type y and get new card type n to pass \n--> ")

                        if games_satatus == "y":
                            computer_cards5 = randint(2, 10)
                            computer_cards_sum = computer_cards3 + computer_cards1 + computer_cards4 + computer_cards5
                            player_cards_sum = player_cards1 + player_cards2 + player_cards3 + player_cards4 + player_cards5
                            print(
                                f"computer cards [ * , {computer_cards1} , {computer_cards3} , {computer_cards4} , {computer_cards5} ] computer score {computer_cards_sum}")

                            player_cards5 = randint(2, 10)
                            player_cards_sum = player_cards1 + player_cards2 + player_cards3 + player_cards4 + player_cards5
                            player_cards_sum = player_cards1 + player_cards2 + player_cards3 + player_cards4 + player_cards5
                            print(
                                f"your cards [ {player_cards1} , {player_cards2} , {player_cards3} , {player_cards4} , {computer_cards5}] currently score {player_cards_sum} ")

                            if player_cards_sum > 21:
                                print(" you lose , your score over 21 ")
                                player_money -= player_bet
                                print(f"currently money {player_money}")
                                game_satatus_check = input("do you want more time ? type y or n \n-->")

                                if game_satatus_check == "y":
                                    StartGame()
                                elif game_satatus_check == "n":
                                    game_over21 = False
                                    break
                                else:
                                    game_over21 = False
                                    break

                        elif games_satatus == "n":
                            computer_cards_sum = computer_cards1 + computer_cards2 + computer_cards3 + computer_cards4 + computer_cards5
                            player_cards_sum = player_cards1 + player_cards2 + player_cards3 + player_cards4 + player_cards5
                            if computer_cards_sum < player_cards_sum:
                                print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                                print("congrats you win")
                                player_money += (player_bet) * 2
                                print(f"currently money {player_money}")
                                game_satatus_check = input("do you want more time ? type y or n \n-->")

                                if game_satatus_check == "y":
                                    StartGame()
                                elif game_satatus_check == "n":
                                    game_over21 = False
                                    break
                                else:
                                    game_over21 = False
                                    break

                            elif computer_cards_sum > player_cards_sum:
                                print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                                print("you lose")
                                player_money -= player_bet
                                print(f"currently money {player_money}")
                                game_satatus_check = input("do you want more time ? type y or n \n-->")

                                if game_satatus_check == "y":
                                    StartGame()
                                elif game_satatus_check == "n":
                                    game_over21 = False
                                    break
                                else:
                                    game_over21 = False
                                    break
                            else:
                                print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                                print("draw")
                                print(f"currently money {player_money}")
                                game_satatus_check = input("do you want more time ? type y or n \n-->")

                                if game_satatus_check == "y":
                                    StartGame()
                                elif game_satatus_check == "n":
                                    game_over21 = False
                                    break
                                else:
                                    game_over21 = False
                                    break
                        else:
                            games_satatus = input("Plese type y or n \n--> ")
                            if games_satatus == "y":
                                StartGame()
                            else:
                                break

                    elif games_satatus == "n":
                        computer_cards_sum = computer_cards1 + computer_cards2 + computer_cards3 + computer_cards4 + computer_cards5
                        player_cards_sum = player_cards1 + player_cards2 + player_cards3 + player_cards4 + player_cards5
                        if computer_cards_sum < player_cards_sum:
                            print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                            print("congrats you win")
                            player_money += (player_bet) * 2
                            print(f"currently money {player_money}")

                            game_satatus_check = input("do you want more time ? type y or n \n-->")

                            if game_satatus_check == "y":
                                StartGame()
                            elif game_satatus_check == "n":
                                game_over21 = False
                                break
                            else:
                                game_over21 = False
                                break

                        elif computer_cards_sum > player_cards_sum:
                            print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                            print("you lose")
                            player_money -= player_bet
                            print(f"currently money {player_money}")
                            game_satatus_check = input("do you want more time ? type y or n \n-->")

                            if game_satatus_check == "y":
                                StartGame()
                            elif game_satatus_check == "n":
                                game_over21 = False
                                break
                            else:
                                game_over21 = False
                                break

                        else:
                            print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                            print("draw")
                            print(f"currently money {player_money}")
                            game_satatus_check = input("do you want more time ? type y or n \n-->")

                            if game_satatus_check == "y":
                                StartGame()
                            elif game_satatus_check == "n":
                                game_over21 = False
                                break
                            else:
                                game_over21 = False
                                break
                    else:
                        games_satatus = input("Plese type y or n \n--> ")
                        if games_satatus == "y":
                            StartGame()
                        else:
                            break

                elif games_satatus == "n":
                    computer_cards_sum = computer_cards1 + computer_cards2 + computer_cards3 + computer_cards4 + computer_cards5
                    player_cards_sum = player_cards1 + player_cards2 + player_cards3 + player_cards4 + player_cards5
                    if computer_cards_sum < player_cards_sum:
                        print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                        print("congrats you win")
                        player_money += (player_bet) * 2
                        print(f"currently money {player_money}")
                        game_satatus_check = input("do you want more time ? type y or n \n-->")

                        if game_satatus_check == "y":
                            StartGame()
                        elif game_satatus_check == "n":
                            game_over21 = False
                            break
                        else:
                            game_over21 = False
                            break

                    elif computer_cards_sum > player_cards_sum:
                        print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                        print("you lose")
                        player_money -= player_bet
                        print(f"currently money {player_money}")
                        game_satatus_check = input("do you want more time ? type y or n \n-->")

                        if game_satatus_check == "y":
                            StartGame()
                        elif game_satatus_check == "n":
                            game_over21 = False
                            break
                        else:
                            game_over21 = False
                            break

                    else:
                        print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                        print("draw")
                        print(f"currently money {player_money}")
                        game_satatus_check = input("do you want more time ? type y or n \n-->")

                        if game_satatus_check == "y":
                            StartGame()
                        elif game_satatus_check == "n":
                            game_over21 = False
                            break
                        else:
                            game_over21 = False
                            break
                else:
                    games_satatus = input("Plese type y or n \n--> ")
                    if games_satatus == "y":
                        StartGame()
                    else:
                        break



            elif games_satatus == "n":
                computer_cards_sum = computer_cards1 + computer_cards2 + computer_cards3 + computer_cards4 + computer_cards5
                player_cards_sum = player_cards1 + player_cards2 + player_cards3 + player_cards4 + player_cards5

                if computer_cards_sum < player_cards_sum:
                    print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                    print("congrats you win")
                    player_money += (player_bet) * 2
                    print(f"currently money {player_money}")
                    game_satatus_check = input("do you want more time ? type y or n \n-->")

                    if game_satatus_check == "y":
                        StartGame()
                    elif game_satatus_check == "n":
                        game_over21 = False
                        break
                    else:
                        game_over21 = False
                        break

                elif computer_cards_sum > player_cards_sum:
                    print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                    print("you lose")
                    player_money -= player_bet
                    print(f"currently money {player_money}")
                    game_satatus_check = input("do you want more time ? type y or n \n-->")

                    if game_satatus_check == "y":
                        StartGame()
                    elif game_satatus_check == "n":
                        game_over21 = False
                        break
                    else:
                        game_over21 = False
                        break

                else:
                    print(f"computer score : {computer_cards_sum} your score : {player_cards_sum}")
                    print("draw")
                    print(f"currently money {player_money}")
                    game_satatus_check = input("do you want more time ? type y or n \n-->")

                    if game_satatus_check == "y":
                        StartGame()
                    elif game_satatus_check == "n":
                        game_over21 = False
                        break
                    else:
                        game_over21 = False
                        break



            else:
                games_satatus = input("Plese type y or n \n--> ")
                if games_satatus == "y":
                    StartGame()
                else :
                    break
        else :
            print("you are bankrupt")
            game_satatus_check = input("do you want more time ? type y or n \n-->")
            if game_satatus_check == "y":
                player_money = 1000
                StartGame()
            elif game_satatus_check == "n":
                game_over21 = False
                break
            else :
                game_over21 = False
                break

StartGame()






