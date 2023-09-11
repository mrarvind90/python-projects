from __future__ import annotations
from itertools import zip_longest


class Category:
    def __init__(self, name: str):
        self.name: str = name
        self.ledger: list[dict[str, float | str]] = []

    def __str__(self):
        formatted_entry = ""

        for entry in self.ledger:
            formatted_desc = f"{entry['description'][:23]: <30}"
            formatted_amt = f"{entry['amount']:.2f}"
            formatted_entry += f"{formatted_desc[:-len(formatted_amt)] + formatted_amt}\n"

        return (f"{self.name:*^30}\n"
                f"{formatted_entry}"
                f"Total: {self.get_balance():.2f}")

    def __repr__(self):
        return f"Category('{self.name}')"

    def deposit(self, amt: float, desc: str = "") -> None:
        self.ledger.append({"amount": amt, "description": desc})

    def withdraw(self, amt: float, desc: str = "") -> bool:
        withdrawn = False

        if self.check_funds(amt):
            self.ledger.append({"amount": -amt, "description": desc})
            withdrawn = True

        return withdrawn

    def get_balance(self) -> float:
        return sum([entry["amount"] for entry in self.ledger])

    def transfer(self, amt: float, category: Category) -> bool:
        transferred = False

        if self.check_funds(amt):
            self.withdraw(amt, f"Transfer to {category.name}")
            category.deposit(amt, f"Transfer from {self.name}")
            transferred = True

        return transferred

    def check_funds(self, amt: float) -> bool:
        return self.get_balance() >= amt


def create_spend_chart(categories: list[Category]) -> str:
    num_categories = len(categories)

    total_spent = [(category.name, sum(entry["amount"] for entry in category.ledger if entry["amount"] < 0))
                   for category in categories]
    total = sum(category_spent for _, category_spent in total_spent)
    percentage_spent = [(category_name, round((category_spent / total) * 100))
                        for category_name, category_spent in total_spent]

    formatted_y_axis = ""
    for y_axis in range(100, -10, -10):
        formatted_y_axis += f"{(str(y_axis) + '|').rjust(4)}"
        formatted_y_values = ""

        for values in percentage_spent:
            formatted_y_values += f"{'o': ^3}" if values[1] >= y_axis else f"{' ': ^3}"

        formatted_y_axis += f"{formatted_y_values} \n"

    labels = list(zip_longest(*[label for label, _ in percentage_spent]))
    formatted_x_axis = ""
    for label in labels:
        formatted_chars = ""

        for value in label:
            formatted_chars += f"{value: ^3}" if value else f"{' ': ^3}"

        formatted_x_axis += f"{formatted_chars.rjust(((num_categories * 3) + 4), ' ')} \n"

    return (f"Percentage spent by category\n"
            f"{formatted_y_axis}"
            f"{('-' * ((num_categories * 3) + 1)).rjust(((num_categories * 3) + 5), ' ')}\n"
            f"{formatted_x_axis}").rstrip()
