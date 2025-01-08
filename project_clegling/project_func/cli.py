import prompt


def unk_cmd():
    print("Неизвестная команда")


def show_help():
    print("Project 0.1.0.")
    print("\t<command> exit - выйти из программы")
    print("\t<command> help - справочная информация")


def parse_cmd():
    while True:
        cmd = prompt.string("Введите команду: ")
        # cmd = input("Введите команду: ")

        match cmd:
            case "exit":
                return
            case "help":
                show_help()
            case _:
                unk_cmd()
                show_help()
