from pathlib import Path
import numpy as np

def solve_part1(data: list[str]) -> int:
    total_joltage = 0
    for bank_ in data:
        bank = [int(b.strip()) for b in bank_ if b.strip()]
        b1_value = max(bank[0:-1])
        b1_loc = int(np.argmax(bank[0:-1]))
        b2_value = max(bank[b1_loc+1:])
        joltage = b1_value*10 + b2_value
        total_joltage += joltage
    return total_joltage

def get_largest_digit_with_loc(digits: list[int]) -> tuple[int,int]:
    return max(digits), np.argmax(digits)

def get_biggest_battery(digits: list[int], n_digits: list[int]):
    if n_digits == 1:
        return max(digits)

    leading_digit_value, leading_digit_location = get_largest_digit_with_loc(digits[0:-(n_digits-1)])
    remaining_digits = digits[leading_digit_location+1:]
    return leading_digit_value * 10 ** (n_digits-1) + get_biggest_battery(remaining_digits, n_digits-1)

def solve_part2(data: list[str]) -> int:
    total_joltage = 0
    for bank_ in data:
        bank = [int(b.strip()) for b in bank_ if b.strip()]
        total_joltage += get_biggest_battery(bank, 12)
    return total_joltage

def get_input_data(test = False) -> list[str]:
    data_file = Path(__file__).parent / "data" / ("test_data.txt" if test else "data.txt")
    with open(data_file) as f:
        data = f.readlines()
    return data

if __name__ == "__main__":
    data = get_input_data(test=False)
    result_part1 = solve_part1(data)
    print(f"Part 1: {result_part1}")
    result_part2 = solve_part2(data)
    print(f"Part 2: {result_part2}")