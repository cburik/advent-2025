from argparse import ArgumentParser, Namespace
from pathlib import Path
from subprocess import Popen

BASE_DIR = Path(__file__).resolve().parents[1] / "solutions"
TEMPLATE_PATH = Path(__file__).resolve().parents[1] / "templates" / "solution_template.py"

def parse_args() -> Namespace:
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-y", type=int, help="year", required=True)
    arg_parser.add_argument("-d", type=int, help="day", required=True)
    args = arg_parser.parse_args()
    if args.y < 100:
        args.y += 2000
    return args

def create_files(year:int, day:int):
    basepath = BASE_DIR / str(year) / f"{day:02d}"
    solution_file = basepath / "solution.py"
    test_data_file = basepath / "data" / "test_data.txt"
    data_file = basepath / "data" / "data.txt"

    data_file.parent.mkdir(parents=True, exist_ok=True)
    if not solution_file.exists():
        if TEMPLATE_PATH.exists():
            with open(TEMPLATE_PATH) as template_f:
                template_content = template_f.read()
        else:
            template_content = "# Write your solution here\n"
        with open(solution_file, "w") as f:
            f.write(template_content)
    if not test_data_file.exists():
        with open(test_data_file, "w") as f:
            f.write("")
    if not data_file.exists():
        with open(data_file, "w") as f:
            f.write("")

def open_files(year:int, day:int):
    basepath = BASE_DIR / str(year) / f"{day:02d}"
    solution_file = basepath / "solution.py"
    test_data_file = basepath / "data" / "test_data.txt"
    data_file = basepath / "data" / "data.txt"

    Popen(["code", str(solution_file), str(test_data_file), str(data_file)])

def main():
    args = parse_args()
    create_files(args.y, args.d)
    open_files(args.y, args.d)

