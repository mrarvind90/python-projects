import operator


def formatter(problems: list[str], result: bool = False) -> str:
    ops: dict = {"+": operator.add, "-": operator.sub}

    fst_operands: str = ""
    ops_and_sec_operands: str = ""
    eq_operators: str = ""
    results: str = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for idx, problem in enumerate(problems):
        [first_operand, op, second_operand] = problem.split(" ")

        if not (first_operand.isnumeric()) or not (second_operand.isnumeric()):
            return "Error: Numbers must only contain digits."

        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_len: int = max(len(first_operand), len(second_operand))
        fst_operands += f"{first_operand.rjust(max_len + 2, ' ')}{' ' * 4}"
        ops_and_sec_operands += f"{op + second_operand.rjust(max_len + 2, ' ')[1:]}{' ' * 4}"
        eq_operators += f"{'-'.rjust(max_len + 2, '-')}{' ' * 4}"

        if result:
            ans = str(ops[op](int(first_operand), int(second_operand)))
            results += f"{ans.rjust(max_len + 2, ' ')}{' ' * 4}"

    return (f"{fst_operands.rstrip()}\n"
            f"{ops_and_sec_operands.rstrip()}\n"
            f"{eq_operators.rstrip()}\n"
            f"{results.rstrip()}").rstrip()
