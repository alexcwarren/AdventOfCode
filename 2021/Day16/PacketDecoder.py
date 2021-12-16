import pdb


def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return data.split('\n')


def verify_sample(actual_vals, expected_vals):
    if isinstance(actual_vals, list):
        if len(actual_vals) != len(expected_vals):
            print('ERROR: Count of actual values != count of expected values:', end=' ')
            print(f'len(actual_vals)={len(actual_vals)}, len(expected_vals)={len(expected_vals)}')
            return False
    else:
        actual_vals = [actual_vals]
        expected_vals = [expected_vals]
    
    for a,e in zip(actual_vals, expected_vals):
        if a != e:
            print(f'FAILED: Expected {e} got {a}')
            return False
    
    print('SUCCESS')
    return True


class BITS_Packet:
    Literal_ID = 4

    def __init__(self, bin_str):
        self.binary = bin_str
        breakpoint()
        # Get 1st three bits for version
        self.version = int(self.extract_bits(3), 2)
        # Get next three bits for type ID
        self.typeID = int(self.extract_bits(3), 2)
        self.contains_packets = False
        self.lengthID = None
        self.contents = list()

        # If type ID = 4
        if self.typeID == BITS_Packet.Literal_ID:
            # Parse remaining bits for literals
            self.contents = self.parse_literals()
        # Else
        else:
            # Pass remaining bits for analysis
            self.contains_packets = True
            self.lengthID = self.extract_bits(1)
            if self.lengthID == '0':
                length_subpackets = int(self.extract_bits(15), 2)
                breakpoint()
                self.contents.append(BITS_Packet(self.extract_bits(length_subpackets)))
            else:
                num_subpackets = int(self.extract_bits(11), 2)
                for __ in range(num_subpackets):
                    breakpoint()
                    self.contents.append(BITS_Packet(self.extract_bits(11)))
        
        if len(self.binary) >= 11:
            self.contents.append(BITS_Packet(self.binary))
    
    def extract_bits(self, stop):
        binary = self.binary[:stop]
        self.binary = self.binary[stop:]
        return binary

    def parse_literals(self):
        contents = list()
        len_binary = len(self.binary)
        for i in range(0, len_binary, 5):
            first_bit = self.extract_bits(1)
            contents.append(int(self.extract_bits(4), 2))
            # bin_str[i + 1 : i + 5]
            if first_bit == '0':
                break
        return contents
    
    def __repr__(self):
        string = f'{str(self)}:'
        string += f'{self.contents}'
        return string

    def __str__(self):
        return f'{self.version} {self.typeID}'


def part_one(packets, using_sample=False):
    print(f'Running Part 1:')
    
    for hex_packet in packets:
        print(hex_packet)
        # Convert packet from HEX to BIN
        binary = str(bin(int(hex_packet, 16)))[2:]
        packet = BITS_Packet(binary)
        print(repr(packet))
        print()

    # TODO
    # if using_sample:
    #     verify_sample()
    
    print(f'  \n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'sample.in'
    packets = parse(filename)

    part_one(packets, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')