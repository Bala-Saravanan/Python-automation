import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")

BASE_URL = f"{URL}{API_KEY}"


CURRENCIES = ["USD", "CAD", "INR", "EUR", "AUD"]
currencies = ",".join(CURRENCIES)


def know_currency_value(base):
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None


def currency_convertor(base, value):
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()["data"]
        for key, val in data.items():
            print(f"{key}: {val["value"]*value}")

    except Exception as e:
        print(e)
        return None


def main():
    import time

    print("\t\t\t\tCURRENCY CONVERTOR")
    while True:
        wish = input("Would you like to continue? ('n' for no): ")
        if wish == "n":
            print("Thank You!")
            break
        print(
            "Press 1 to know the values.\nPress 2 to use conversion.\nPress 0 to exit\n"
        )
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        match (choice):
            case 1:
                base = input("Enter Base Currency: ").upper()
                print(f"The other currency value for 1 {base} is: \n")
                data = know_currency_value(base)
                del data[base]
                for key, value in data.items():
                    print(f"{key}: {value["value"]}")
                print("\n")
                time.sleep(2)
            case 2:
                base = input("Enter Base Currency: ").upper()
                value = int(input("Enter Value to be converted: "))
                print(f"The other currency value for {value} {base} is: \n")
                currency_convertor(base, value)
                print("\n")
                time.sleep(2)
            case _:
                print("Invalid Choice!")


main()
