import sys


def main():
    sys.stdout.write("$ ")
    command = input()
    sys.stderr.write(f"{command}: command not found")
    pass


if __name__ == "__main__":
    main()
