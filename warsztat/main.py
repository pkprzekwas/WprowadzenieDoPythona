# coding=utf-8

DISPLAY = 1
ADD = 2
DELETE = 3
CLOSE = 4


def show_menu():
    print('''
    Dostępne opcje to:\n
    1. Wyswietl listę zadań.\n
    2. Dodaj zadanie.\n
    3. Usuń zadanie.\n
    4. Zamknij program.\n
    ''')


def display_todo_list(todo_list):
    print('\n')
    if len(todo_list) < 1:
        print('Twoja lista zadań jest pusta.')

    for idx, todo in enumerate(todo_list):
        print('{}: {}'.format(idx+1, todo))


def add_todo(todo_list):
    print('Dodaję zadanie do listy.')
    new_todo = input('Podaj treść zadania: ')
    todo_list.append(new_todo)
    print('Poprawnie dodano zadanie.')
    return todo_list


def delete_todo(todo_list):
    idx = input('Podaj id zadania do usunięcia: ')
    del todo_list[idx-1]
    return todo_list


if __name__ == '__main__':
    todos = list()
    show_menu()

    while True:
        option = input('\nWybierz opcję: ')

        if option == DISPLAY:
            display_todo_list(todos)

        elif option == ADD:
            todos = add_todo(todos)

        elif option == DELETE:
            todos = delete_todo(todos)

        elif option == CLOSE:
            break

        else:
            print('Nie rozpoznano polecenia.')

    print('Koniec działania programu.')
