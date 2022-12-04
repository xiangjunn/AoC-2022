import requests
import os
from typing import Callable
from dotenv import load_dotenv

load_dotenv()


def get_input(day: int, year=2022) -> str:
    try:
        req = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",
                           cookies={"session": os.getenv("SESSION")})
        return req.text
    except requests.exceptions.RequestException as exc:
        raise SystemExit(exc)


def solve(day: int, solver: Callable[[str], str], filename: str = None) -> str:
    if not filename:
        filename = f"day-{day}.txt"
    location = os.path.join(os.getcwd(), filename)
    if os.path.isfile(location):
        file = open(location, "r")
        data = file.read()
    else:
        file = open(location, "w")
        data = get_input(day)
        file.write(data)

    return solver(data)
