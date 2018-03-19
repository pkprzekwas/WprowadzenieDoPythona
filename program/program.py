print(20 * '-')

def print_menu():

    menu = '1. Wyslwietl liste\n2. Dodaj zadanie\n3. Wyjdz z programu'

    print(menu)
    print(20 * '-')


def main_loop(task_list_):

    is_program_on = True

    while is_program_on:

        user_input = int(input('Wybierz opcje: '))
        print(20 * '-' + '\n')

        if user_input == 1:

            for task in task_list_:
                print('- {}'.format(task))

        elif user_input == 2:

            task = input('Podaj nazwe zadania: ')
            task_list_.append(task)

        elif user_input == 3:
            is_program_on = False

        else:
            print('WFT!?')

        print(20 * '-' + '\n')

    print('Koniec dzialania programu')


task_list = ['Wynies smieci', 'Posprzataj pokoj']
print_menu()
main_loop(task_list)
