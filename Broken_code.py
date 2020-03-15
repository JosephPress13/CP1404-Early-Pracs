"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))

if score > 100:
    print("Invalid score")
elif score > 89:
    print("Excellent")
elif score > 49:
    print("Passable")
else:
    print("Bad")