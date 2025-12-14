from pathlib import Path

class Dial:
    def __init__(self):
        self.position = 50
        self.zero_count = 0

    def _read_code(self, code):
        direction = code[0]
        steps = int(code[1:])
        return direction, steps

    def _turn(self, direction, steps):
        if direction == 'L':
            self.position -= steps
        elif direction == 'R':
            self.position += steps

    def turn(self, code):
        if not code:
            # incase if last line is empty
            return
        direction, steps = self._read_code(code)
        self._turn(direction, steps)
        self.reset_dial()
        if self.position == 0:
            self.zero_count += 1

    def reset_dial(self):
        if self.position < 0:
            self.position = 100 + self.position
        elif self.position > 99:
            self.position = self.position - 100

        if self.position > 99 or self.position < 0:
            self.reset_dial()

class Dial2(Dial):
    def turn(self, code):
        if not code:
            # incase if last line is empty
            return
        direction, steps = self._read_code(code)
        self._turn(direction, steps)
        self.zero_count += abs(self.position // 100)
        self.reset_dial()



def solve_part1(codes):
    dial = Dial()
    for code in codes:
        dial.turn(code.strip())
    return dial.zero_count

def solve_part2(codes):
    dial = Dial2()
    for code in codes:
        dial.turn(code.strip())
    return dial.zero_count

if __name__ == "__main__":
    data_file = Path(__file__).parent / "data" / "data.txt"
    with open(data_file) as f:
        test_data = f.readlines()

    print("Test Part 1:", solve_part1(test_data))
    print("Test Part 2:", solve_part2(test_data))