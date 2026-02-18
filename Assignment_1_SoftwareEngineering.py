"""
Title: Assignment 1 for Software Engineering
File: Assignment_1_SoftwareEngineering.py

External Files Required:
No external files are required for this code

External Files Created:
No external files are created for this code

Programmer:
Dylan Cuatecontzi

Email:
Dylanscuatecontzi@lewisu.edu

Course:
CPSC 44000 – Section LT1

Date:
February 17, 2026

Description:
The purpose of this code is to apply brute force to the Fermat Equation to locate near misses, and then once all near misses are located, the smallest will be displayed to the user.
"""

def get_valid_n():
    """Gather user input for variable n and verify that it is valid."""
    n = int(input("Enter n (2 < n < 12): "))
    while n <= 2 or n >= 12:
        print("Invalid input.")
        n = int(input("Enter n (2 < n < 12): "))
    return n


def get_valid_k():
    """Gather bound for variable k."""
    k = int(input("Enter k (k >= 10): "))
    while k < 10:
        print("Invalid input.")
        k = int(input("Enter k (k >= 10): "))
    return k


def compute_near_miss(n, k):
    """Searches all combinations for x,y and prints out improvements."""

    smallest = float("inf")

    for x in range(10, k + 1):
        for y in range(10, k + 1):

            value = (x ** n) + (y ** n)

            z = int(value ** (1 / n))

            # bracket correction
            while (z + 1) ** n <= value:
                z += 1
            while z ** n > value:
                z -= 1

            lower = z ** n
            upper = (z + 1) ** n

            miss = min(abs(value - lower), abs(upper - value))
            relative = miss / value

            if relative < smallest:
                smallest = relative

                print("\nNew smallest relative miss:")
                print(f"x={x}, y={y}, z={z}")
                print(f"miss={miss}")
                print(f"relative miss={relative}")
                print("--------------------------------")

    return smallest


def main():
    n = get_valid_n()
    k = get_valid_k()

    result = compute_near_miss(n, k)

    print("\nSearch complete.")
    print("Final smallest relative miss:", result)


main()
input("\nPress Enter to exit...")
