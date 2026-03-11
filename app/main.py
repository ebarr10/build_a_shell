import sys
import os
import subprocess

commands_that_need_params = ["echo", "type", "cd"]

commands = {
    "exit": lambda: sys.exit(0),
    "echo": lambda line: print(f"{line[5:].replace('\'', '')}"),
    "type": lambda line: command_type_check(line[5:]),
    "pwd": lambda: print(os.getcwd()),
    "cd": lambda line: cd_command(line),
}


def cd_command(line):
    path = line[3:]
    try:
        if path == "~":
            os.chdir(os.path.expanduser("~"))
        else:
            os.chdir(path)
    except FileNotFoundError:
        print(f"cd: {path}: No such file or directory")


def execution_check(command, print_version="type"):
    # get PATH and split into paths by delimiter
    path = os.getenv("PATH")
    paths = path.split(os.pathsep)
    execution_command, *execution_args = command.split(" ")

    # Test is executable
    for dir in paths:
        location = os.path.join(dir, execution_command)
        if os.access(location, os.X_OK):
            if print_version == "type":
                print(f"{execution_command} is {location}")
            elif print_version == "execution":
                subprocess.run([execution_command] + execution_args)
            return True
    return False


def command_type_check(command):
    if command in commands:
        print(f"{command} is a shell builtin")
    else:
        found_execution = execution_check(command)
        if not found_execution:
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
            found_execution = execution_check(line, print_version="execution")
            if not found_execution:
                print(f"{line}: command not found")


if __name__ == "__main__":
    main()
