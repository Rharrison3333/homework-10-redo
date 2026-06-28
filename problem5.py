import urllib.request
from graphics import *


def count_letters(url):
    counts = [0] * 26

    response = urllib.request.urlopen(url)

    for line in response:
        line = line.decode("utf-8", errors="ignore").upper()

        for ch in line:
            if "A" <= ch <= "Z":
                counts[ord(ch) - ord("A")] += 1

    return counts


def draw_graph(counts):
    total = sum(counts)

    win = GraphWin("Online Frequency Analysis", 800, 500)
    win.setCoords(0, 0, 26, 1)

    for i in range(26):
        if total == 0:
            frequency = 0
        else:
            frequency = counts[i] / total

        bar = Rectangle(Point(i, 0), Point(i + 0.8, frequency))
        bar.draw(win)

        label = Text(Point(i + 0.4, -0.03), chr(ord("A") + i))
        label.draw(win)

    title = Text(Point(13, 0.95), "Online Letter Frequency")
    title.draw(win)

    win.getMouse()
    win.close()


def save_counts(filename, counts):
    outfile = open(filename, "w")

    for i in range(26):
        letter = chr(ord("A") + i)
        outfile.write(letter + " " + str(counts[i]) + "\n")

    outfile.close()


def main():
    print("1. Shakespeare")
    print("2. King James Bible")

    choice = input("Choose a book (1 or 2): ")

    if choice == "1":
        url = "https://gutenberg.org/cache/epub/100/pg100.txt"
    else:
        url = "https://gutenberg.org/cache/epub/10/pg10.txt"

    counts = count_letters(url)

    draw_graph(counts)

    filename = input("Enter the output file name: ")

    save_counts(filename, counts)

    print("Letter counts saved to", filename)


main()
