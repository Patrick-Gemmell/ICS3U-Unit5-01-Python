#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: November 2019
# This program shows functions


def conversion():

    temperature_celcius = int(input("Enter a temperature in Celcius here: "))

    temperature_farenheit = (9/5)*temperature_celcius+32

    print("{0}°C is {1}° in Farenheit".format
          (temperature_celcius, temperature_farenheit))


def main():
    conversion()


if __name__ == "__main__":
    main()
