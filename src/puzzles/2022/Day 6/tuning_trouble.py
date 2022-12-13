from argparse import ArgumentParser
from os import path


class TuningTrouble:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "tuning_trouble.py"
        self.is_part1: bool = is_part1

        # Look for command-line args if no filepath provided
        if filepath is None:
            parser = ArgumentParser(
                prog=prog_name,
                usage=f"python {prog_name} -f <filepath> -p <partnumber>",
            )
            parser.add_argument("-f", "--filepath")
            parser.add_argument("-p", "--partnumber", choices=["1", "2"], default="1")
            args = parser.parse_args()
            filepath = args.filepath
            self.is_part1 = args.partnumber == "1"

        if filepath is None:
            print("ERROR: filepath not provided.")
            exit()
        elif not path.isfile(filepath):
            print('ERROR: "{filepath}" does not exist.')
            exit()
        else:
            self.__filepath: str = filepath

    def print_result(self):
        if self.is_part1:
            print(f"{self.get_start_of_packet()}")
        else:
            print(f"{self.get_start_of_message()}")

    def get_start_of_packet(self, packet_length: int = 4) -> int:
        with open(self.__filepath, "r") as read_file:
            datastream = read_file.read()

        curr_packet: str = datastream[:packet_length]
        for i, char in enumerate(datastream[packet_length:], packet_length + 1):
            if self.all_chars_unique(curr_packet):
                return i - 1
            curr_packet = f"{curr_packet[1:]}{char}"
        return -1

    def all_chars_unique(self, packet: str, is_case_sensitive: bool = False) -> bool:
        if len(packet) <= 0:
            return True
        if not is_case_sensitive:
            packet = packet.lower()

        curr_sequence: str = packet[0]
        for i, char in enumerate(packet[1:]):
            if char in curr_sequence:
                return False
            curr_sequence += char
        return True

    def get_start_of_message(self):
        return self.get_start_of_packet(14)


if __name__ == "__main__":
    TuningTrouble().print_result()
