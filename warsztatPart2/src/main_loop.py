from todo import Todo
from todo_list import TodoList

print('''
1. Wyswietl liste.
2. Dodaj zadanie.
3. Usun zadanie.
4. Wyjdz.
''')

todo_list = TodoList()

while True:
    option = input('Wybierz czynnosc: (1|2|3|4): ')

    if option == '1':
        todo_list.show()

    if option == '2':
        content = input('Podaj tresc zadania: ')
        new_todo = Todo(content)
        todo_list.add(todo=new_todo)

    if option == '3':
        idx = int(input('Podaj indeks zadania do usuniecia: '))
        todo_list.remove(idx)

    if option == '4':
        break

print('Koniec dzialania progrmu.')