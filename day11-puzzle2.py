from common_functions import solve
from collections import deque

DAY = 11


def solver(data: str):
    curr_monkey = None
    for line in data.splitlines():
        if line.startswith("Monkey"):
            curr_monkey = Monkey()
        elif "Starting items" in line:
            items = line.split(":")[1]
            items = deque(map(int, items.split(",")))
            curr_monkey.items = items
        elif "Operation" in line:
            operation = line.split("=")[1]
            curr_monkey.operation = operation
        elif "Test" in line:
            mod = int(line.split("divisible by")[1])
            Monkey.product_of_mods *= mod
            curr_monkey.mod = mod
        elif "If true" in line:
            next_monkey = int(line.split("throw to monkey")[1])
            curr_monkey.if_true = next_monkey
        elif "If false" in line:
            next_monkey = int(line.split("throw to monkey")[1])
            curr_monkey.if_false = next_monkey

    # Starts simulation
    rounds = 10000
    Monkey.run_simulation(rounds)

    inspection_count = list(map(lambda m: m.inspected_count, Monkey.monkeys))
    inspection_count.sort()
    return inspection_count[-1] * inspection_count[-2]


class Monkey:
    monkeys = []
    product_of_mods = 1

    def __init__(self):
        Monkey.monkeys.append(self)
        self.items = []
        self.operation = None
        self.mod = None
        self.if_true = None
        self.if_false = None
        self.inspected_count = 0

    def start_inspection(self):
        while len(self.items) != 0:
            worry = self.items.popleft()
            self.inspected_count += 1
            worry = self.apply_operation(worry)
            worry %= Monkey.product_of_mods
            # throw to next monkey
            if worry % self.mod == 0:
                next_monkey = Monkey.monkeys[self.if_true]
                next_monkey.add_item(worry)
            else:
                next_monkey = Monkey.monkeys[self.if_false]
                next_monkey.add_item(worry)

    def add_item(self, worry):
        self.items.append(worry)

    def apply_operation(self, old):
        # Argument must be named as old for eval to work
        return eval(self.operation)

    @classmethod
    def run_simulation(cls, rounds):
        for _ in range(rounds):
            for monkey in Monkey.monkeys:
                monkey.start_inspection()
            inspection_count = list(
                map(lambda m: m.inspected_count, Monkey.monkeys))


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
