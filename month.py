#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 30, 2025
# The program asks the user for the month as a number.
# It then displays the name of the month associated with the number.


def main():
    # Ask the user for the month number
    month_number = int(input("Enter the number for a month: "))

    # Match number with the respective month
    # and display the result.
    match (month_number):
        case 1:
            print("1 represents January.")
        case 2:
            print("2 represents February.")
        case 3:
            print("3 represents March.")
        case 4:
            print("4 represents April.")
        case 5:
            print("5 represents May.")
        case 6:
            print("6 represents June.")
        case 7:
            print("7 represents July.")
        case 8:
            print("8 represents August.")
        case 9:
            print("9 represents September.")
        case 10:
            print("10 represents October.")
        case 11:
            print("11 represents November.")
        case 12:
            print("12 represents December.")
        case _:
            print(f"{month_number} does not represent a month.")


if __name__ == "__main__":
    main()
