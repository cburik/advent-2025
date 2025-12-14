from pathlib import Path


class Diagram:
    paper_marker = '@'
    empty_marker = '.'
    accessible_marker = 'x'

    def __init__(self, diagram: list[str]):
        self.diagram = diagram
        self.row_count = len(diagram)
        self.column_count = len(diagram[-1])
        self.solved_diagram = diagram.copy()

    def has_paper(self, row: int, column: int) -> bool:
        return self.diagram[row][column] == self.paper_marker

    def surrounding_paper_count(self, row: int, column: int) -> bool:
        count = 0
        for r in range(row-1, row+2):
            for c in range(column-1, column+2):
                if r < 0 or r >= self.row_count:
                    continue
                if c < 0 or c >= self.column_count:
                    continue
                if r == row and c == column:
                    continue
                if self.has_paper(r,c):
                    count+=1
        return count

    def is_accessible(self, row: int, column: int) -> bool:
        return self.surrounding_paper_count(row, column) < 4

    def mark_solved(self, row: int, column: int) -> None:
        row_str = self.solved_diagram[row]
        self.solved_diagram[row] = row_str[:column] + self.accessible_marker + row_str[column+1:]

    def accessible_count(self) -> int:
        count = 0
        for r in range(self.row_count):
            for c in range(self.column_count):
                if self.has_paper(r, c) and self.is_accessible(r,c):
                    count+=1
                    self.mark_solved(r,c)
        return count


class Diagram2(Diagram):
    def mark_solved(self, row: int, column: int) -> None:
        row_str = self.diagram[row]
        self.diagram[row] = row_str[:column] + self.accessible_marker + row_str[column+1:]


def solve_part1(data: list[str]) -> int:
    diagram = Diagram(data)
    return diagram.accessible_count()


def solve_part2(data: list[str]) -> int:
    diagram = Diagram2(data)
    count = 1
    max_it = 100
    i = 0
    removed = 0
    while count > 0 and i < max_it:
        i +=1
        count = diagram.accessible_count()
        removed += count
    if i == max_it:
        print("MAX ITERATIONS REACHED!")
    return removed


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