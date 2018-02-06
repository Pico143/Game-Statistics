# Printing functions

import reports
import os
import datetime


def list_of_functions():
    print("This is a list of available reports.\n")
    print("1.How many games are in the file?")
    print("2.Is there a game from a given year?")
    print("3.Which was the latest game?")
    print("4.How many games do we have by genre?")
    print("5.What is the line number of the given game (by title)?")
    print("6.What is the alphabetical ordered list of the titles?")
    print("7.What are the genres?")
    print("8.What is the release date of the top sold \"First-person shooter\" game?\n")


def print_decide(file_name):
    current_year = (datetime.datetime.now()).year
    os.system('clear')
    print('You wanted to know if there is a game in our file from a certain year.')
    while True:
        year = input('Type in which year interest you:')
        try:
            year = int(year)
            if year > current_year:
                raise ValueError
        except ValueError:
            print("Wrong year provided! It cannot be in the future and must contain only numbers.")
            continue
        break
    answer = reports.decide(file_name, year)
    if answer is True:
        print("Yes, there is a game in the file that was made in year {}.\n".format(year))
    else:
        print("No, there is not a single game in the file that was made in year {}.\n".format(year))



def print_count_by_genre(file_name):
    os.system('clear')
    print("You wanted to know how many games there are from a certain genre.")
    genre = input("Please provide a genre you wanted. ")
    count = reports.count_by_genre(file_name, genre)
    print("There are {} games in the file that represent {} genre.\n".format(count, genre))



def print_line_number(file_name):
    os.system('clear')
    print("You wanted to know the position of a certain game in the file.")
    title = input("Please type in the name of the game you are interested in. ")
    try:
        line = reports.get_line_number_by_title(file_name, title)
    except ValueError:
        print("This game is not in the file!\n")
    else:
        print("This game is in line number {} of the file.\n".format(line))



def print_sort_abc(file_name):
    os.system('clear')
    games_sorted = reports.sort_abc(file_name)
    print("Here's a sorted list of games in the file that you wanted.")
    for item in games_sorted:
        print(item)
    print("\n")

def print_get_genres(file_name):
    genres = reports.get_genres(file_name)
    print ("Here's a list of all the genres appearing in the file. ")
    for item in genres:
        print (item)
    print ("\n")


def print_top_fps(file_name):
    try:
        top_sold = reports.when_was_top_sold_fps(file_name)
    except:
        print ("There is no First-person shooter game in the file!\n")
    else:
        print("The top sold First-person shooter game in the file is from year {}.\n".format(top_sold))


def main():
    while True:
        file_name = "game_stat.txt"
        print("Please type in number corresponding to report type you need.")
        print("Type \"help\" to see available reports and their numbers.")
        print("Type \"exit\" to quit.")
        choice = input('Your input: ')
        os.system('clear')
        if choice.lower() == 'help':
            list_of_functions()
            continue
        elif choice == "1":
            amount = str(reports.count_games(file_name))
            print("There are {} games in the file.\n".format(amount))
            continue
        elif choice == "2":
            print_decide(file_name)
            continue
        elif choice == "3":
            latest = reports.get_latest(file_name)
            print("The newest game in the file is {} .\n".format(latest))
            continue
        elif choice == "4":
            print_count_by_genre(file_name)
            continue
        elif choice == "5":
            print_line_number(file_name)
            continue
        elif choice == "6":
            print_sort_abc(file_name)
            continue
        elif choice == "7":
            print_get_genres(file_name)
            continue
        elif choice == "8":
            print_top_fps(file_name)
            continue
        elif choice.lower() == "exit":
            exit(0)
        else:
            print("Wrong input was provided. Try again.\n")


if __name__ == "__main__":
    main()
