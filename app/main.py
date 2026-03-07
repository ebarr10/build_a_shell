import sys

commands_that_need_params = ["echo", "type"]

commands = {
    "exit": lambda: sys.exit(0),
    "echo": lambda line: sys.stdout.write(f"{line[5:]}\n"),
    "type": lambda line: command_type_check(line[5:]),
}


def command_type_check(command):
    if command in commands:
        sys.stdout.write(f"{command} is a shell builtin\n")
    else:
        sys.stdout.write(f"{command}: not found\n")


def main():
    while True:
        sys.stdout.write("$ ")
        line = input()
        for command in commands:
            if line.startswith(command):
                if command in commands_that_need_params:
                    commands[command](line)
                else:
                    commands[command]()
                break
        else:
            sys.stderr.write(f"{line}: command not found\n")


if __name__ == "__main__":
    main()
