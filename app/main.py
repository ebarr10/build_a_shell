import sys

commands = {
    "exit": lambda: sys.exit(0),
}


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command in commands:
            commands[command]()
        else:
            sys.stderr.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
