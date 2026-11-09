"""
マッチ棒クイズの解法
入力形式: x [+-*] y = z
入力条件: x, y, z は、0以上99以下の整数とする。
処理前提: x, y, z の整数、及び+,-, = の演算子はマッチ棒で表現される加算、減算、及び等号である。
          演算子 * は、マッチ棒2本で×を表現する乗算の演算子である。
          7と4は、マッチ棒2本を移動して11に変形できるものとする。
処理概要: 入力された式をマッチ棒で表現する。
          入力された式が数学的に誤っている場合は、マッチ棒を1本だけ移動して
          数学的に正しくなる式を探す。
          入力された式が数学的に正しい場合は、その式を解とする問題式を探す。
出力形式: u [+-*] v = w (u, v, w, +, -, * は変形後のマッチ棒が表現する数及び演算子)
"""

import re   # 正規表現を使用するためにインポート

DIGITS = {
    "0": frozenset("abcdef"),
    "1": frozenset("bc"),
    "2": frozenset("abdeg"),
    "3": frozenset("abcdg"),
    "4": frozenset("bcfg"),
    "5": frozenset("acdfg"),
    "6": frozenset("acdefg"),
    "7": frozenset("abcf"),
    "8": frozenset("abcdefg"),
    "9": frozenset("abcdfg"),
}
OPERATORS = {
    "+": frozenset(("horizontal", "vertical")),
    "-": frozenset(("horizontal",)),
    "*": frozenset(("diagonal_left", "diagonal_right")),
}
EQUALS = frozenset(("equal_upper", "equal_lower"))
INPUT_PATTERN = re.compile(r"^\s*(\d+)\s*([+\-*])\s*(\d+)\s*=\s*(\d+)\s*$")
SPECIAL_TRANSFORMATIONS = frozenset(((7, 11), (4, 11)))
MAX_NUMBER = 99


def matchsticks_for_number(number: int) -> frozenset[tuple[int, str]]:
    """Return the labelled matchsticks used to display a number."""
    return frozenset(
        (digit_index, segment)
        for digit_index, digit in enumerate(str(number))
        for segment in DIGITS[digit]
    )


def matchsticks_for_expression(
    left: int, operator: str, right: int, result: int
) -> frozenset[tuple[str, object]]:
    """Return labelled matchsticks for all positions in an expression."""
    sticks: set[tuple[str, object]] = set()
    for position, number in (("left", left), ("right", right), ("result", result)):
        sticks.update((position, stick) for stick in matchsticks_for_number(number))
    sticks.update(("operator", stick) for stick in OPERATORS[operator])
    sticks.update(("equals", stick) for stick in EQUALS)
    return frozenset(sticks)


def is_correct_equation(left: int, operator: str, right: int, result: int) -> bool:
    return (
        (operator == "+" and left + right == result)
        or (operator == "-" and left - right == result)
        or (operator == "*" and left * right == result)
    )


def is_two_move_special_transformation(
    left: int,
    operator: str,
    right: int,
    result: int,
    new_left: int,
    new_operator: str,
    new_right: int,
    new_result: int,
) -> bool:
    """Return whether a 7-or-4 to 11 transformation uses two moves."""
    if not is_correct_equation(new_left, new_operator, new_right, new_result):
        return False
    if (new_operator, new_result) != (operator, result):
        return False
    if (left, new_left) in SPECIAL_TRANSFORMATIONS and right == new_right:
        return True
    if (right, new_right) in SPECIAL_TRANSFORMATIONS and left == new_left:
        return True
    return False


def is_reordered_equation(
    left: int, operator: str, right: int, result: int
) -> bool:
    """Return whether moving the operator and equals sign makes a valid equation."""
    return (
        operator == "-"
        and left == right - result
    )


def find_solutions(left: int, operator: str, right: int, result: int) -> list[str]:
    """Find valid equations reachable by the supported matchstick moves."""
    original = matchsticks_for_expression(left, operator, right, result)
    solutions: list[str] = []

    if is_reordered_equation(left, operator, right, result):
        solutions.append(f"{left} = {right} {operator} {result}")

    for new_left in range(MAX_NUMBER + 1):
        for new_right in range(MAX_NUMBER + 1):
            for new_result in range(MAX_NUMBER + 1):
                for new_operator in OPERATORS:
                    is_valid = is_correct_equation(
                        new_left, new_operator, new_right, new_result
                    )
                    is_special = is_two_move_special_transformation(
                        left,
                        operator,
                        right,
                        result,
                        new_left,
                        new_operator,
                        new_right,
                        new_result,
                    )
                    if not is_valid and not is_special:
                        continue

                    candidate = matchsticks_for_expression(
                        new_left, new_operator, new_right, new_result
                    )
                    removed = original - candidate
                    added = candidate - original
                    one_move = len(removed) == 1 and len(added) == 1
                    two_moves = len(removed) == 2 and len(added) == 2
                    if one_move or (is_special and two_moves):
                        expression = f"{new_left} {new_operator} {new_right} = {new_result}"
                        if expression not in solutions:
                            solutions.append(expression)
    return solutions


def find_problems(left: int, operator: str, right: int, result: int) -> list[str]:
    """Find incorrect equations that can be solved to the given equation."""
    target = matchsticks_for_expression(left, operator, right, result)
    problems: list[str] = []

    def number_options(position: str, target_number: int) -> list[int]:
        target_sticks = {
            (position, stick)
            for stick in matchsticks_for_number(target_number)
        }
        return [
            number
            for number in range(MAX_NUMBER + 1)
            if len(target_sticks - {
                (position, stick) for stick in matchsticks_for_number(number)
            }) <= 2
            and len({
                (position, stick) for stick in matchsticks_for_number(number)
            } - target_sticks) <= 2
        ]

    left_options = number_options("left", left)
    right_options = number_options("right", right)
    result_options = number_options("result", result)

    for problem_left in left_options:
        for problem_right in right_options:
            for problem_result in result_options:
                for problem_operator in OPERATORS:
                    if is_correct_equation(
                        problem_left,
                        problem_operator,
                        problem_right,
                        problem_result,
                    ):
                        continue

                    problem = matchsticks_for_expression(
                        problem_left,
                        problem_operator,
                        problem_right,
                        problem_result,
                    )
                    removed = problem - target
                    added = target - problem
                    one_move = len(removed) == 1 and len(added) == 1
                    two_moves = len(removed) == 2 and len(added) == 2
                    is_special = is_two_move_special_transformation(
                        problem_left,
                        problem_operator,
                        problem_right,
                        problem_result,
                        left,
                        operator,
                        right,
                        result,
                    )
                    if one_move or (is_special and two_moves):
                        problems.append(
                            f"{problem_left} {problem_operator} "
                            f"{problem_right} = {problem_result}"
                        )
    return problems


def parse_expression(expression: str) -> tuple[int, str, int, int]:
    """Validate and parse the expression entered at the terminal."""
    match = INPUT_PATTERN.fullmatch(expression)
    if match is None:
        raise ValueError("入力形式は x [+-*] y = z です。")

    left, operator, right, result = match.groups()
    values = tuple(map(int, (left, right, result)))
    if any(value > MAX_NUMBER for value in values):
        raise ValueError(
            f"x, y, z は 0以上{MAX_NUMBER}以下の整数にしてください。"
        )
    return values[0], operator, values[1], values[2]


def main() -> None:
    while True:
        try:
            expression = input(
                "式を入力してください (例: 1 + 2 = 4、終了: q または end): "
            ).strip()
            if expression.lower() in {"q", "end"}:
                print("終了します。")
                return
            left, operator, right, result = parse_expression(expression)
        except (EOFError, KeyboardInterrupt):
            print("\n終了します。")
            return
        except ValueError as error:
            print(f"入力エラー: {error}")
            continue

        if is_correct_equation(left, operator, right, result):
            problems = find_problems(left, operator, right, result)
            if problems:
                print("この式を解とする問題式:")
                for problem in problems:
                    print(problem)
            else:
                print("この式を解とする問題式はありません。")
        else:
            solutions = find_solutions(left, operator, right, result)
            if solutions:
                print("解:")
                for solution in solutions:
                    print(solution)
            else:
                print("1本のマッチ棒を移動して成立する式はありません。")


if __name__ == "__main__":
    main()
