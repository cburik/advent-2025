from pathlib import Path

class Range:
    def __init__(self, string: str):
        self.start, self.end = map(int, string.strip().split('-'))

    def __contains__(self, number: int):
        return number >= self.start and number <= self.end

    def __lt__(self, range):
        return self.start < range.start or (self.start == range.start and self.end < range.end)

    def has_overlap(self, range):
        pass

    def unite_ranges(self, range):
        pass

def parse_data(data: list[str]) -> tuple[list[Range], list[int]]:
    ranges = []
    ingredients_ids = []
    for line in data:
        if '-' in line:
            ranges.append(Range(line))
        elif line.strip():
            ingredients_ids.append(int(line.strip()))
    return ranges, ingredients_ids

def solve_part1(data: list[str]) -> int:
    ranges, iids = parse_data(data)
    count = 0
    for iid in iids:
        for range in ranges:
            if iid in range:
                count+=1
                break
    return count

def solve_part2(data: list[str]) -> int:
    ranges, _ = parse_data(data)
    ranges.sort()
    return None

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