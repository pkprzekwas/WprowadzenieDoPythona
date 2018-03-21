
class TodoList:
    def __init__(self):
        self.todo_list = list()

    def add(self, todo_content):
        new_todo = TodoItem(todo_content)
        self.todo_list.append(new_todo)
        print('Dodano nowe TODO.')

    def delete(self, todo_id):
        del self.todo_list[todo_id]
        print('Usunieto TODO nr {}'.format(todo_id+1))

    def finish(self, todo_id):
        todo_to_finish = self.todo_list[todo_id]
        todo_to_finish.is_finished = True
        self.todo_list[todo_id] = todo_to_finish

    def show(self):
        if len(self.todo_list) == 0:
            print('Twoja lista jest pusta.')
        else:
            for idx, todo in enumerate(self.todo_list):
                print('{}. {}'.format(idx+1, todo))


class TodoItem:
    def __init__(self, content):
        self.content = content
        self.is_finished = False

    def __str__(self):
        status = '[OK]' if self.is_finished else '[  ]'
        return '{} --- status: {}'.format(self.content, status)


if __name__ == '__main__':
    todo_list = TodoList()

    print(20 * '-')
    menu = 'TODO LIST APP\n'
    menu += '1. Wyświetl | 2. Dodaj | 3. Zakończ | 4. Usuń | 5. Zamknij program\n'
    print(menu)

    while True:
        choice = input('Wybierz opcję (1|2|3|4|5): ')

        if choice == '1':
            todo_list.show()

        elif choice == '2':
            todo_content = input('Podaj treść zadania: ')
            todo_list.add(todo_content)

        elif choice == '3':
            idx = input('Podaj indeks zadania do zakończenia: ')
            todo_list.finish(int(idx) - 1)

        elif choice == '4':
            idx = input('Podaj indeks zadania do usunięcia: ')
            todo_list.delete(int(idx)-1)

        elif choice == '5':
            break

        else:
            print('Coś poszło nie tak. Spróbuj jeszcze raz.')

    print(20 * '-')
    print('Koniec działania programu.')