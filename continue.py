#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# this program asks the user for the amount of numbers they want to add
# together then asks the user what numbers they want to add together,
# then adds them


def main():
    # this program asks the user for the amount of numbers they want to add
    # together then asks the user what numbers they want to add together,
    # then adds them

    # this is to keep track of how many times you go through the loop
    loop_counter = 0
    sum_of_numbers = 0
    amount_number = 0
    amount_string = ""
    user_number = 0
    sum_of_numbers = 0

    # input
    amount_string = input("Enter the amount of numbers you would like to add: ")

    # process and output

    try:
        amount_number = int(amount_string)
        for loop_counter in range(amount_number):
            user_string = input("Enter a number: ")
            user_number = int(user_string)
            if user_number < 0:
                print("invalid input")
                continue
            else:
                sum_of_numbers = sum_of_numbers + user_number
    except Exception as e:
        print("invalid input {} ".format(e))
    else:
        print("The sum of the positive numbers is {0}".format(sum_of_numbers))
    print("\nDone.")


if __name__ == "__main__":
    main()
