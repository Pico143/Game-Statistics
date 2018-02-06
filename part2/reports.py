# Report functions


def get_genres(file_name):  # importowane z pierwszego zadania jako funkcja pomocnicza
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        games = split(text)
        genres = [item[3] for item in games]  # 4 pole to gatunek
        genres = list(set(genres))
        genres = insertion_sort(genres)
        return genres


def count_by_genre(file_name, genre):  # importowane z pierwszego zadania jako funkcja pomocnicza
    counter = 0  # licznik gier znajdujących się na liście należących do gatunku
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        games = split(text)
        for line in games:
            if genre in line:
                counter += 1
    return counter


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


def insertion_sort_year(games):
    for n in range(len(games)):  # insertion sort
        if n == 0:  # zakładamy, że lista jednoelementowa jest posortowana
            continue
        else:
            while n > 0:
                if games[n][1] > games[n-1][1]:
                    games[n], games[n-1] = games[n-1], games[n]
                elif games[n][1] == games[n-1][1]:  # jeżeli rok jest ten sam, przechodzimy do sortowania alfabetycznego
                    temp = min(len(games[n]), len(games[n-1]))
                    for i in range(temp):  # algorytm z poprzedniego zadania
                        if ord(games[n][0][i].lower()) < ord(games[n-1][0][i].lower()):
                            games[n], games[n-1] = games[n-1], games[n]
                            break
                        elif ord(games[n][0][i].lower()) > ord(games[n-1][0][i].lower()):
                            break
                        if i == temp - 1 and len(games[n]) < len(games[n-1]):
                            games[n], games[n-1] = games[n-1], games[n]
                n -= 1
    return games


def split(format_me):  # funkcja pomocnicza rozbijająca zawartość pliku na linie, a te na pola
    lines = (format_me.strip('\n').split('\n'))
    for index, line in enumerate(lines):
        lines[index] = line.split("\t")
    return lines


def get_most_played(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    games = split(text)
    most_played = ('', 0)
    for game in games:
        if float(game[1]) > most_played[1]:
            most_played = (game[0], float(game[1]))
    return most_played[0]


def sum_sold(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    games = split(text)
    total = 0.0
    for game in games:
        total += float(game[1])
    return total


def get_selling_avg(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    games = split(text)
    average = 0.0
    for game in games:
        average += float(game[1])
    average /= len(games)
    return average


def count_longest_title(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    games = split(text)
    max_length = 0
    for game in games:
        if len(game[0]) > max_length:
            max_length = len(game[0])
    return max_length


def get_date_avg(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    games = split(text)
    average = 0
    for game in games:
        average += int(game[2])
    average = int(average / len(games)) + int(average % len(games) > 0)
    return average


def get_game(file_name, title):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    games = split(text)
    title = title.lower()
    game = []
    for item in games:
        if item[0].lower() == title:
            game = item
    if game == []:
        raise ValueError("This game is not in the file!")
    game[1] = float(game[1])
    game[2] = int(game[2])
    return game


def count_grouped_by_genre(file_name):
    group = get_genres(file_name)
    for i in range(len(group)):
        group[i] = [group[i], count_by_genre(file_name, group[i])]
    group = dict(group)
    return group


def get_date_ordered(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    games = split(text)
    for i in range(len(games)):
        games[i] = (games[i][0], games[i][2])
    games = insertion_sort_year(games)
    for i in range(len(games)):
        games[i] = games[i][0]
    return games
