"""
This is a simple script to make CLI requests to a Math related API.
The API called has some free features and some under subscription. This script
only calls the free features, as of 24 September 2024.
"""

import requests
import urllib.parse
import sys

BASE_URI = "https://api.math.tools"

def number_of_the_day():
    """
    Calls the API to retrieve the number of the day
    and possibly some facts about it.
    """
    # combining the endpoint with the request for the number of the day
    nod_url = urllib.parse.urljoin(BASE_URI, "/numbers/nod")

    # getting the response
    response = requests.get(nod_url)

    # checking the response and parsing its result
    if response.status_code == 200:
        nod = response.json()
        print("Number of the day:", nod["contents"]["nod"]["numbers"]["number"])

        return nod
    else:
        print(f"Failed to fetch number of the day. Status code:{response.status_code}")
        return None


def digits_of_pi(digits):
    """
    Calls the API to retrieve the user-specified first digits of π.
    """
    # combining the endpoint with the request for the digits of π
    dopi_url = urllib.parse.urljoin(BASE_URI, "/numbers/pi")

    # getting the response
    response = requests.get(dopi_url, params={"digits": digits})

    # checking the response and parsing its result
    if response.status_code == 200:
        dopi = response.json()
        print(f"The first {digits} digits of π are:", dopi["contents"]["result"])

        return dopi
    else:
        print(f"Failed to fetch digits of π. Status code:{response.status_code}")
        return None


def decimal_to_binary(number):
    """
    Calls the API to turn the input decimal number into its binary form.
    """
    # combining the endpoint with the request for the transformation to binary
    dtp_url = urllib.parse.urljoin(BASE_URI, "/numbers/base/binary")

    # getting the response
    response = requests.get(dtp_url, params = {"number": number})

    # checking the response and parsing its result
    if response.status_code == 200:
        dtp = response.json()
        print(f"{number}'s binary form is:", dtp["contents"]["answer"])

        return dtp
    else:
        print(f"Failed to fetch binary form. Status code:{response.status_code}")
        return None

# creating a user choice tree
if __name__ == '__main__':
    print("This script makes a call to the MathTOOLS API. The supported actions include:")
    query = int(input("1. Number of the day\n2. Digits of π\n3. Decimal to binary\n(type index)"))
    if query == 1:
        try:
            number_of_the_day()
        except KeyboardInterrupt:
            print('\nGoodbye!')
            sys.exit(0)
    elif query == 2:
        inp = int(input("How many digits of π would you like to see?\n(type number of digits)\n"))
        try:
            digits_of_pi(inp)
        except KeyboardInterrupt:
            print('\nGoodbye!')
            sys.exit(0)
    elif query == 3:
        inp = int(input("What number would you like to transform? \ntype number)\n"))
        try:
            decimal_to_binary(inp)
        except KeyboardInterrupt:
            print('\nGoodbye!')
            sys.exit(0)
