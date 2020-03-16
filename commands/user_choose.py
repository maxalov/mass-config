def commands_type(path):
    value = user_input()
    if value == '1':
        config = True
        with open(path + 'config.txt') as config_file:
            return config, config_file.read()
    else:
        config = False
        with open(path + 'show.txt') as show_file:
            return config, show_file.read()


action_list = {'1': 'Configure type commands', '2': 'Show type commands'}


def user_input():
    print('\nPlease select which type of commands you want to execute:\n')
    print("#" * 57)
    for key, value in action_list.items():
        print(f'{key:>15} - {value}')
    print(f'{"#" * 57}\n')
    while True:
        user_wants = input("Please select 1 or 2: ")
        if user_wants in action_list:
            print(f'\n{"#" * 57}\n{"You select":>22} "{action_list[user_wants]}"\n{"#" * 57}\n')
            return user_wants
        else:
            continue
