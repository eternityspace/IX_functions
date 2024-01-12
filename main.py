

if __name__ == '__main__':

    phone_book = {}

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (KeyError, ValueError, IndexError, ZeroDivisionError) as e:
                if isinstance(e, KeyError):
                    return ('\nThere is no contact with this name!\n')
                if isinstance(e, ValueError):
                    return ('\nCheck the phone number!\n')
                if isinstance(e, IndexError):
                    return ('Check your input!')

        return inner

    def console_input():
        return input('> ').lower()

    @input_error
    def handler(user_input):

        user_command = user_input.split()

        command = user_command[0]

        if command == 'add':
            name = user_command[1]
            if name not in phone_book:
                phone_book[name] = int(user_command[2])
            else:
                return 'Contact already exists!'

        elif command == 'change':
            name = user_command[1]
            if name in phone_book:
                phone_book[name] = int(user_command[2])
            else:
                return 'Contact does not exist!'

        elif command == 'phone':
            return f"{user_command[1]}'s phone is: {phone_book[user_command[1]]}"
        else:
            return ('Check your input!')

    while True:

        user_input = console_input()

        if user_input == 'hello':
            print(f'How can I help you?')

        elif user_input == 'show all':

            print(f"{'-' * 33}")

            if not phone_book:
                print('{:^33}'.format('Phone book is empty!'))

            for name, phone in phone_book.items():
                print('|{:^15}|{:^15}|'.format(name, phone))

            print(f"{'-' * 33}")

        elif user_input in ('good bye', 'close', 'exit'):
            break

        else:

            result = handler(user_input)

            if result is not None:
                print(f'{result}')
