import os
from graphics import *


def count_letters_in_file(filename, counts):
    infile = open(filename, "r", encoding="utf-8", errors="ignore")

    for line in infile:
        line = line.upper()

        for ch in line:
            if "A" <= ch <= "Z":
                counts[ord(ch) - ord("A")] += 1

    infile.close()


def draw_graph(counts):
    total = sum(counts)

    win = GraphWin("Python Code Frequency Analysis", 800, 500)
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

    title = Text(Point(13, 0.95), "Frequency Analysis of Python Files")
    title.draw(win)

    win.getMouse()
    win.close()


def main():
    folder = input("Enter the folder name: ")

    counts = [0] * 26

    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            full_path = os.path.join(folder, filename)
            count_letters_in_file(full_path, counts)

    draw_graph(counts)


main()
