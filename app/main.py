import sys

commands = {
    "exit": lambda line: sys.exit(0),
    "echo": lambda line: sys.stdout.write(f"{line.replace('echo ', '')}\n"),
}


def main():
    while True:
        sys.stdout.write("$ ")
        line = input()
        for command in commands:
            if line.startswith(command):
                commands[command](line)
                break
        else:
            sys.stderr.write(f"{line}: command not found\n")


if __name__ == "__main__":
    main()
