
class TodoList:
    def __init__(self):
        self.todo_list = list()

    def add(self, todo):
        print('Adding {}'.format(todo))
        self.todo_list.append(todo)

    def remove(self, idx):
        del self.todo_list[idx-1]
        print('Zadanie zostalo usuniete.')

    def show(self):
        if len(self.todo_list) == 0:
            print('Twoja list jest pusta')

        for idx, todo in enumerate(self.todo_list):
            print('{}. {}'.format(idx+1, todo))

