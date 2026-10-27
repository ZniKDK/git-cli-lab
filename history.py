history = []


def remember(line):
    history.append(line)


def show():
    for line in history:
        print(line)
