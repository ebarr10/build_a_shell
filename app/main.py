import os
import subprocess

builtins = {"echo", "exit", "type", "pwd", "cd"}


def get_executable_path(command):
    path_env = os.getenv("PATH")
    paths = path_env.split(os.pathsep)

    for path_dir in paths:
        if not path_dir:
            continue
        full_path = os.path.join(path_dir, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None


def parse_command(command):
    tokens = []
    in_single_quote = False
    current_token = []
    in_word = False

    for char in command:
        if char == "'":
            in_single_quote = not in_single_quote
            in_word = True
        elif char.isspace() and not in_single_quote:
            if in_word:
                tokens.append("".join(current_token))
                current_token = []
                in_word = False
        else:
            current_token.append(char)
            in_word = True

    if in_word:
        tokens.append("".join(current_token))


def main():
    while True:
        print("$ ", end="")
        try:
            line = input()
        except EOFError:
            print()
            break

        tokens = parse_command(line)
        if not tokens:
            continue

        cmd_name = tokens[0]
        args = tokens[1:]

        if cmd_name == "exit":
            break

        elif cmd_name == "echo":
            print(" ".join(args))

        elif cmd_name == "type":
            if not args:
                continue
            target_cmd = args[0]

            if target_cmd in builtins:
                print(f"{target_cmd} is a shell builtin")
            else:
                exec_path = get_executable_path(target_cmd)
                if exec_path:
                    print(f"{target_cmd} is {exec_path}")
                else:
                    print(f"{target_cmd}: not found")

        elif cmd_name == "pwd":
            print(os.getcwd())

        elif cmd_name == "cd":
            if not args:
                continue
            target_dir = args[0]

            if target_dir == "~":
                target_dir = os.path.expanduser("~")

            try:
                os.chdir(target_dir)
            except FileNotFoundError:
                print(f"cd: {target_dir}: No such file or directory")
        else:
            exec_path = get_executable_path(cmd_name)
            if exec_path:
                subprocess.run([exec_path] + args)
            else:
                print(f"{cmd_name}: command not found")


if __name__ == "__main__":
    main()
