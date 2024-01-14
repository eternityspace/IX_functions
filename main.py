phone_book = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return ('\n  There is no contact with this name!\n')
        except ValueError:
            return ('\n  Check the phone number!\n')
        except IndexError:
            return ('\n  Check your input!\n')

    return inner


@input_error
def add(user_command):

    name = user_command[1]
    phone = user_command[2]

    if name.title() not in phone_book:
        phone_book[name.title()] = int(phone)
    else:
        return '\n  Contact already exists!\n'


@input_error
def change(user_command):

    name = user_command[1]
    phone = user_command[2]

    if name.title() in phone_book:
        phone_book[name.title()] = int(phone)
    else:
        return '\n  Contact does not exist!\n'


def console_input():
    return input('> ').lower()


def main():

    print()

    while True:

        user_input = console_input()

        if not user_input:
            continue

        if user_input == 'hello':
            print(f'\n  How can I help you?\n')
            continue

        elif user_input == 'show all':
            result = show_all()
            print(result)
            continue

        elif user_input in ('good bye', 'close', 'exit'):
            break

        user_command = user_input.split()

        if user_command != []:
            command = user_command[0]
        else:
            continue

        if command == 'add':

            result = add(user_command)
            if result is not None:
                print(result)

        elif command == 'change':

            result = change(user_command)
            if result is not None:
                print(result)

        elif command == 'phone':

            result = phone(user_command)
            print(result)

        else:
            print('\n  Check your input!\n')


@input_error
def phone(user_command):

    name = user_command[1]
    return f"\n  {name.title()}'s phone is: {phone_book[name.title()]}\n"


def show_all():

    result = f"\n  {'-' * 33}\n\n"

    if not phone_book:
        result += '{:^33}'.format('Phone book is empty!\n')

    for name, phone in phone_book.items():
        result += '  |{:^15}|{:^15}|\n'.format(name, phone)

    result += f"\n  {'-' * 33}\n"

    return result


if __name__ == '__main__':

    main()
