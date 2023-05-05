from pathlib import Path


class Day:
    def __init__(self, filename: str):
        self.__filepath: Path = Path(filename)
        self.__filename: str = self.__filepath.name.split(".")[0]
        self.input_path: Path = self.__filepath.parent.joinpath(
            f"input/{self.__filename}.in"
        )


if __name__ == "__main__":
    print("Testing Day module...")
    day = Day(__file__)
    print(day.input_path)
    assert day.input_path.exists()
    print("SUCCESS\n")
