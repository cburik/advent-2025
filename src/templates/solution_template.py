from pathlib import Path

def solve_part1(data: list[str]) -> int:
    pass

def solve_part2(data: list[str]) -> int:
    pass

def get_input_data(test = False) -> list[str]:
    data_file = Path(__file__).parent / "data" / ("test_data.txt" if test else "data.txt")
    with open(data_file) as f:
        data = f.readlines()
    return data

if __name__ == "__main__":
    data = get_input_data(test=True)
    result_part1 = solve_part1(data)
    print(f"Part 1: {result_part1}")
    result_part2 = solve_part2(data)
    print(f"Part 2: {result_part2}")