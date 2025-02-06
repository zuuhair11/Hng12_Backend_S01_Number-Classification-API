from fastapi import FastAPI, Query
import requests
from typing import Dict
from math import sqrt
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def is_perfect(n: int) -> bool:
    if n < 1:
        return False

    return sum([i for i in range(1, n) if n % i == 0]) == n


def is_armstrong(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    power = len(digits)

    return sum(d ** power for d in digits) == number


def get_fun_fact(n: int) -> str:
    response = requests.get(f'http://numbersapi.com/{ n }/math')

    if response.status_code == 200:
        return response.text

    return 'No fun fact available.'


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/api/classify-number')
def classify_number(number: int = Query(..., description='The number to classify')) -> Dict:
    try:
        properties = []

        if is_armstrong(number):
            properties.append('armstrong')

        properties.append('odd' if number % 2 else 'even')

        return {
            'number': number,
            'is_prime': is_prime(number),
            'is_perfect': is_perfect(number),
            'properties': properties,
            'digit_sum': sum(int(digit) for digit in str(number)),
            'fun_fact': get_fun_fact(number)
        }
    except Exception:
        return {
            'number': str(number),
            'error': True
        }
