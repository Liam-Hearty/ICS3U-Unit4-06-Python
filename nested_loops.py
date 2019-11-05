#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program uses a loop inside another loop.


def main():
    # this function uses a nested loop

    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(255+1):
        for green in range(255+1):
            for blue in range(255+1):
                print("RGB {0}, {1}, {2}".format(red, green, blue))


if __name__ == "__main__":
    main()
