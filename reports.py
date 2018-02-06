# Report functions
import string


def insertion_sort(games):
    for n in range(len(games)):  # insertion sort
        if n == 0:  # zakładamy, że lista jednoelementowa jest posortowana
            continue
        else:
            while n > 0:
                # znajdujemy krótszy tytuł, aby sprawdzić tyle liter ile ma ten krótszy
                temp = min(len(games[n]), len(games[n-1]))
                for i in range(temp):  # dzięki pętli jeżeli pierwsze litery będą takie same, sprawdzane będą kolejne
                    if ord(games[n][i].lower()) < ord(games[n-1][i].lower()):
                        games[n], games[n-1] = games[n-1], games[n]
                        break
                    elif ord(games[n][i].lower()) > ord(games[n-1][i].lower()):
                        break
                    # jeżeli tytuły są te same, dłuższy idzie dalej
                    if i == temp - 1 and len(games[n]) < len(games[n-1]):
                        games[n], games[n-1] = games[n-1], games[n]
                n -= 1
    return games


def split(format_me):  # funkcja pomocnicza rozbijająca zawartość pliku na linie, a te na pola
    lines = (format_me.strip('\n').split('\n'))
    for index, line in enumerate(lines):
        lines[index] = line.split("\t")
    return lines


def count_games(file_name):
    '''Funkcja liczy, ile gier znajduje się na liście i zwraca ich ilość'''
    count = 0
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        lines = (text.strip('\n').split('\n'))
        for item in lines:
            count += 1
    return count


def decide(file_name, year):
    '''Funkcja sprawdza, czy na liście jest jakaś gra z danego roku i zwraca prawda/fałsz'''
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        fields = text.split("\t")
        if str(year) in fields:
            return True
        else:
            return False


def get_latest(file_name):
    '''Funkcja wyszukuje najnowszą grę z listy i zwraca jej nazwę; 
    jeśli z tego samego roku jest kilka gier, zwraca pierwszą na liście'''
    temp = ('None', 0)  # przechowuje nazwę i rok produkcji najnowszej gry dotychczas znalezionej na liście
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        games = split(text)
        for line in games:  # dla każdej gry sprawdzamy, czy jest nowsza niż obecnie znaleziona najdłuższa
            try:
                int(line[2])
            except ValueError:
                print("Data in file is corrupted or does not meet required standard!")
                exit(1)
            if int(line[2]) > temp[1]:
                temp = (line[0], int(line[2]))
    return temp[0]


def count_by_genre(file_name, genre):
    counter = 0  # licznik gier znajdujących się na liście należących do gatunku
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        games = split(text)
        for line in games:
            if genre in line:
                counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        games = split(text)
        for index, line in enumerate(games):
            if title.lower() == line[0].lower():
                return index+1
        raise ValueError


def sort_abc(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        games = split(text)
        games = [item[0] for item in games]  # tworzenie listy samych tytułów
        games = insertion_sort(games)
        return games


def get_genres(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        games = split(text)
        genres = [item[3] for item in games]  # 4 pole to gatunek
        genres = list(set(genres))
        genres = insertion_sort(genres)
        return genres


def when_was_top_sold_fps(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        games = split(text)
        most_sold = (0, 0)
        for game in games:
            if game[3] == 'First-person shooter':
                if float(game[1]) > float(most_sold[0]):
                    most_sold = (game[1], game[2])
        if most_sold == (0, 0):
            raise ValueError
        else:
            return int(most_sold[1])
