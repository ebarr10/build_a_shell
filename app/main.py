import sys
import os

commands_that_need_params = ["echo", "type"]

commands = {
    "exit": lambda: sys.exit(0),
    "echo": lambda line: print(f"{line[5:]}"),
    "type": lambda line: command_type_check(line[5:]),
}


def command_type_check(command):
    if command in commands:
        print(f"{command} is a shell builtin")
    else:
        # get PATH and split into paths by delimiter
        path = os.getenv("PATH")
        paths = path.split(os.pathsep)
        found = False

        # Test is executable
        for dir in paths:
            location = os.path.join(dir, command)
            if os.access(location, os.X_OK):
                print(f"{command} is {location}")
                found = True
                continue
        if not found:
            print(f"{command}: not found")


def main():
    while True:
        print("$ ", end="")
        line = input()
        for command in commands:
            if line.startswith(command):
                if command in commands_that_need_params:
                    commands[command](line)
                else:
                    commands[command]()
                break
        else:
            print(f"{line}: command not found")


if __name__ == "__main__":
    main()
