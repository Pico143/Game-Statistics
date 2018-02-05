# Report functions
def format_text(format_me):
    '''Dzieli wczytany tekst na linie po znaku końca linii - funkcja pomocnicza'''
    lines = (format_me.split('\n')).strip()
    return lines


def count_games(file_name):
    '''Funkcja liczy, ile gier znajduje się na liście i zwraca ich ilość'''
    count = 0
    with open(file_name,'r', encoding='utf-8') as f:
        text = f.read()
        lines = format_text(text)
        for item in lines:
            count += 1
    return count

def decide(file_name, year):
    '''Funkcja sprawdza, czy na liście jest jakaś gra z danego roku i zwraca prawda/fałsz'''
    with open(file_name,'r', encoding='utf-8') as f:
        text = f.read()
        lines = format_text(text)
        if year in f.read():
            return True
        else:
            return False


def get_latest(file_name):
    '''Funkcja wyszukuje najnowszą grę z listy i zwraca jej nazwę; 
    jeśli z tego samego roku jest kilka gier, zwraca pierwszą na liście'''
    temp = 0
    with open(file_name,'r', encoding='utf-8') as f:
        text = f.read()



def count_by_genre(file_name, genre):
    pass

def get_line_number_by_title(file_name, title):
    pass