#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: Mar 25 2025
# This program is to ask users tp input an integer and find out if it is positive, negative or zero.


def main():
    integer = int(input("please input an integer: "))

    if integer == 0:
        print("{} is just a zero".format(integer))

    elif integer > 0:
        print("{} is a positive integer".format(integer))

    elif integer < 0:
        print("{} is a negative integer".format(integer))

    print("")
    print("Done!")


if __name__ == "__main__":
    main()
