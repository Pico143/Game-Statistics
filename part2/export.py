import reports
import os


def list_of_functions():
    print("This is a list of available reports.\n")
    print("1.What is the title of the most played game (i.e. sold the most copies)?")
    print("2.How many copies have been sold total?")
    print("3.What is the average selling?")
    print("4.How many characters long is the longest title?")
    print("5.What is the average of the release dates?")
    print("6.What is the average of the release dates?")
    print("7.How many games are there grouped by genre?")
    print("8.What is the date ordered list of the games?\n")


def print_properties(file_name, export):
    os.system('clear')
    print("You wanted to know properties of a certain game.")
    title = input("Please type what game you want to know more about: ")
    try:
        game = reports.get_game(file_name, title)
    except ValueError as err:
        print("This game is not in the file!")
        with open(export, mode='a', encoding='utf-8') as f:
            f.write("{}\n".format(err))
    else:
        print("Name: {}".format(game[0]))
        print("Sold copies: {} million".format(game[1]))
        print("Year of production: {}".format(game[2]))
        print("Genre: {}".format(game[3]))
        print("Developer: {}\n".format(game[4]))
        with open(export, mode='a', encoding='utf-8') as f:
            f.write("{}\n".format(title))


def print_get_date_ordered(file_name, export):
    os.system('clear')
    ordered_list = reports.get_date_ordered(file_name)
    print("Here's a list of games in chronological order, starting from newest.")
    for game in ordered_list:
        print(game)
    print("\n")
    with open(export, mode='a', encoding='utf-8') as f:
        f.write("{}\n".format(ordered_list))


def print_grouped_by_genre(file_name, export):
    os.system('clear')
    group = reports.count_grouped_by_genre(file_name)
    for genre, game in group.items():
        print("{} : {} game(s) in the file.".format(genre, game))
    with open(export, mode='a', encoding='utf-8') as f:
        f.write("{}\n".format(group))
    print("\n")


def main():
    file_name = "game_stat.txt"
    export = 'export.txt'
    f = open(export, mode='w', encoding='utf-8')  # tworzenie czystego pliku do eksportu
    f.close()
    while True:
        print("Please type in number corresponding to report type you need.")
        print("Type \"help\" to see available reports and their numbers.")
        print("Type \"exit\" to quit.")
        choice = input('Your input: ')
        os.system('clear')
        if choice.lower() == 'help':
            os.system('clear')
            list_of_functions()
            continue
        elif choice == "1":
            os.system('clear')
            most_played = reports.get_most_played(file_name)
            print("The most played game is {} .\n".format(most_played))
            with open(export, mode='a', encoding='utf-8') as f:
                f.write("{}\n".format(most_played))
            continue
        elif choice == "2":
            os.system('clear')
            total = str(reports.sum_sold(file_name))
            print("The sum of sales of all games in the file is {} .\n".format(total))
            with open(export, mode='a', encoding='utf-8') as f:
                f.write("{}\n".format(total))
            continue
        elif choice == "3":
            os.system('clear')
            average = str(reports.get_selling_avg(file_name))
            print("The average sales for a game in the file is {} million copies.\n".format(average))
            with open(export, mode='a', encoding='utf-8') as f:
                f.write("{}\n".format(average))
            continue
        elif choice == "4":
            os.system('clear')
            longest = str(reports.count_longest_title(file_name))
            print("The longest name of a game in the file has {} characters.\n".format(longest))
            with open(export, mode='a', encoding='utf-8') as f:
                f.write("{}\n".format(longest))
            continue
        elif choice == "5":
            os.system('clear')
            average = str(reports.get_date_avg(file_name))
            print("The average release date for a game in the file is year {}.\n".format(average))
            with open(export, mode='a', encoding='utf-8') as f:
                f.write("{}\n".format(average))
            continue
        elif choice == "6":
            print_properties(file_name, export)
            continue
        elif choice == "7":
            print_grouped_by_genre(file_name, export)
            continue
        elif choice == "8":
            print_get_date_ordered(file_name, export)
            continue
        elif choice.lower() == "exit":
            exit(0)
        else:
            os.system('clear')
            print("Wrong input was provided. Try again.\n")
            continue


if __name__ == "__main__":
    main()
# Export functions
