from graphics import *


def count_letters(filename):
    counts = [0] * 26
    total = 0

    infile = open(filename, "r", encoding="utf-8", errors="ignore")

    for line in infile:
        line = line.upper()

        for ch in line:
            if "A" <= ch <= "Z":
                counts[ord(ch) - ord("A")] += 1
                total += 1

    infile.close()

    return counts, total


def draw_graph(counts, total):
    win = GraphWin("Letter Frequency Analysis", 800, 500)
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

    title = Text(Point(13, 0.95), "Letter Frequency Analysis")
    title.draw(win)

    win.getMouse()
    win.close()


def main():
    filename = input("Enter the text file name: ")

    counts, total = count_letters(filename)

    draw_graph(counts, total)


main()
