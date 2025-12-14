from pathlib import Path

def get_range_bounds(range: str) -> tuple[int,int]:
    start, end = map(int, range.split('-'))
    return start, end

def is_valid_pid(pid: int) -> bool:
    pid = str(pid)
    middle = int(len(pid) / 2)
    p1 = pid[0:middle]
    p2 = pid[middle:]
    return p1 != p2

def solve_part1(data: list[str]) -> int:
    count = 0
    for range_ in data:
        start, end = get_range_bounds(range_)
        for pid in range(start, end+1):
            if not is_valid_pid(pid):
                count += pid
    return count

def split_in_equal_parts(str_: str, num_char: int) -> list[str]:
    parts = []
    while str_:
        new_part, str_ = str_[0:num_char], str_[num_char:]
        parts.append(new_part)
    return parts

def is_repeating_string(str_: str, num_char: int) -> bool:
    if len(str_) % num_char != 0:
        return False
    parts = split_in_equal_parts(str_, num_char)

    part1 = parts[0]
    for p in parts:
        if p != part1:
            return False
    return True

def is_valid_pid2(pid: int) -> bool:
    pid = str(pid)
    for i in range(1,len(pid)//2 +1):
        if is_repeating_string(pid, i):
            return False
    return True

def solve_part2(data: list[str]) -> int:
    count = 0
    for range_ in data:
        start, end = get_range_bounds(range_)
        for pid in range(start, end+1):
            if not is_valid_pid2(pid):
                count += pid
    return count


if __name__ == "__main__":
    test_data_file = Path(__file__).parent / "data" / "test_data.txt"
    with open(test_data_file) as f:
        test_data = f.read().split(',')

    data_file = Path(__file__).parent / "data" / "data.txt"
    with open(data_file) as f:
        data = f.read().split(',')

    print('==== part 1 ====')
    print("Test:", solve_part1(test_data))
    print("Solution:", solve_part1(data))

    print('\n==== part 2 ====')
    print("Test:", solve_part2(test_data))
    print("Solution:", solve_part2(data))
