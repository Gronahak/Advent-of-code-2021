import requests
from pathlib import Path
from template import get_code_template
from shutil import rmtree

url = "https://adventofcode.com/2021/"

cookies = {
    "_ga":"GA1.2.1045025226.1641376382",
    "_gid":"GA1.2.1220838300.1641376382",
    "session":"53616c7465645f5f3f17bdd6894620fb035df72082c41b8b39c43008cd38686a82976b9e7bd5475ff7d4c163a6d1e248"    
}


def get_input(day_n: int) -> str:
    resp = requests.post("https://adventofcode.com/2021/day/"+str(day_n)+"/input", cookies=cookies)
    return resp.text

def write_to_file(text: str, file_path: str)->None:
    with open(file_path, 'w') as f:
        f.write(text)

def create_and_populate_folder(day_n: int):
    current = Path('.')

    name = f"day_{day_n}"

    folder = current / name.upper()
    folder.mkdir()

    main_code = (folder / name).with_suffix(".py")
    _input = (folder / "input").with_suffix(".txt")
    _input_debug1 = (folder / "input_debug_part1").with_suffix(".txt")
    _input_debug2 = (folder / "input_debug_part2").with_suffix(".txt")
    
    code_files = [main_code]
    text_files = [_input, _input_debug1, _input_debug2 ]


    for file in [*code_files, *text_files]:
        file.touch()

    main_code.write_text(get_code_template(name.upper()))
    _input.write_text(get_input(day_n))

def delete_dir(day_):
    current = Path('.')

    folder = current / "DAY_3"
    rmtree(folder)


if __name__ == '__main__':
    create_and_populate_folder(19)