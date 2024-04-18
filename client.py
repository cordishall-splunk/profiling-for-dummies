import requests
import time
import random


def make_request(path):
    try:
        response = requests.get("http://localhost:5000/"+path)
        print("Response:", response.text)
    except requests.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    while True:
        # Generate a random number between 1 and 3
        x = random.randint(1, 3)
        # Check the value of x using if statements
        if x == 1:
            make_request("low")
        elif x == 2:
            n = random.randint(1,20)
            make_request("high/"+str(n))
        else:
            make_request("medium")
        time.sleep(1)
