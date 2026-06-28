def read_path(filename):
    path = []

    infile = open(filename, "r")

    first_line = infile.readline().strip()
    parts = first_line.split()
    rows = int(parts[0])
    cols = int(parts[1])

    for line in infile:
        parts = line.strip().split()
        row = int(parts[0])
        col = int(parts[1])
        path.append((row, col))

    infile.close()

    return rows, cols, path


def clean_message(message):
    result = ""

    for ch in message.upper():
        if ch.isalpha():
            result += ch

    return result


def make_grid(message, rows, cols):
    while len(message) < rows * cols:
        message += "X"

    grid = []
    index = 0

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(message[index])
            index += 1
        grid.append(row)

    return grid


def encode(message, rows, cols, path):
    message = clean_message(message)
    grid = make_grid(message, rows, cols)

    cipher = ""

    for location in path:
        r, c = location
        cipher += grid[r][c]

    return cipher


def decode(cipher, rows, cols, path):
    cipher = clean_message(cipher)

    grid = []

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("")
        grid.append(row)

    index = 0

    for location in path:
        r, c = location
        grid[r][c] = cipher[index]
        index += 1

    message = ""

    for r in range(rows):
        for c in range(cols):
            message += grid[r][c]

    return message


def main():
    path_file = input("Enter the path file name: ")

    rows, cols, path = read_path(path_file)

    choice = input("Encode or decode? ")

    if choice.lower() == "encode":
        message = input("Enter the message: ")
        print("Ciphertext:", encode(message, rows, cols, path))
    else:
        cipher = input("Enter the ciphertext: ")
        print("Message:", decode(cipher, rows, cols, path))


main()
