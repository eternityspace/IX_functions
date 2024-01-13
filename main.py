phone_book = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return ('\nThere is no contact with this name!\n')
        except ValueError:
            return ('\nCheck the phone number!\n')
        except IndexError:
            return ('\nCheck your input!\n')

    return inner


@input_error
def add(name):

    if name not in phone_book:
        phone_book[name.title()] = int(user_command[2])
    else:
        return '\nContact already exists!\n'


@input_error
def change(name, phone):
    if name.title() in phone_book:
        phone_book[name.title()] = int(phone)
    else:
        return '\nContact does not exist!\n'


def console_input():
    return input('> ').lower()


@input_error
def phone(name):
    return f"\n{name.title()}'s phone is: {phone_book[name.title()]}\n"


def show_all():

    result = ''
    result += f"\n{'-' * 33}\n\n"

    if not phone_book:
        result += '{:^33}'.format('Phone book is empty!\n')

    for name, phone in phone_book.items():
        result += '|{:^15}|{:^15}|\n'.format(name, phone)

    result += f"\n{'-' * 33}\n"

    return result


if __name__ == '__main__':

    print()

    while True:

        user_input = console_input()
        if user_input == 'hello':
            print(f'\nHow can I help you?\n')
            continue

        elif user_input == 'show all':
            result = show_all()
            print(result)
            continue

        elif user_input in ('good bye', 'close', 'exit'):
            break

        user_command = user_input.split()
        command = user_command[0]

        if command == 'add':

            result = add(name=user_command[1])
            if result is not None:
                print(result)

        elif command == 'change':

            result = change(name=user_command[1], phone=user_command[2])
            if result is not None:
                
                print(result)

        elif command == 'phone':
            result = phone(name=user_command[1])
            print(result)

        else:
            print(('\nCheck your input!\n'))
