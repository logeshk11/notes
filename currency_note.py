# calculates the least number of coins and rupee note to give for any value in INR
import math

notes = [1, 2, 5, 10, 20, 50, 100, 200, 2000, 500]


def minimum_notes(money):
    for a in range(len(notes) - 1, 0, -1):
        cal = money / notes[a]
        if cal >= 1:
            no_of_note = math.floor(cal)
            money -= (no_of_note * notes[a])
            print(f"You need {no_of_note} note in {notes[a]}")


money=int(input("Enter the value:"))

notes.sort()
(minimum_notes(money))
