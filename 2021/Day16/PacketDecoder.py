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

    def __init__(self, packet_str, is_hex=False):
        self.binary = self.to_binary(packet_str) if is_hex else packet_str
        self.length = 0
        self.version = int(self.extract_bits(3), 2)
        self.typeID = int(self.extract_bits(3), 2)
        self.contains_packets = False
        self.lengthID = None
        self.contents = list()

        if self.typeID == BITS_Packet.Literal_ID:
            self.contents.append(self.parse_literal())
        else:
            self.contains_packets = True
            self.lengthID = self.extract_bits(1)
            if self.lengthID == '0':
                length_subpackets = int(self.extract_bits(15), 2)
                subpackets = list()
                while length_subpackets > 0:
                    if self.binary == '': input('EMPTY')
                    subpacket = BITS_Packet(self.extract_bits())
                    self.binary = subpacket.binary
                    self.length += subpacket.length
                    length_subpackets -= subpacket.length
                    subpackets.append(subpacket)
                self.contents= subpackets
            else:
                num_subpackets = int(self.extract_bits(11), 2)
                while len(self.contents) < num_subpackets:
                    if self.binary == '': input('EMPTY')
                    subpacket = BITS_Packet(self.extract_bits())
                    self.binary = subpacket.binary
                    self.length += subpacket.length
                    self.contents.append(subpacket)
    
    def to_binary(self, hex_str):
        hex_to_bin = {hex(n)[2:].upper() : bin(n)[2:].zfill(4) for n in range(16)}
        
        binary = ''
        for h in hex_str:
            binary += hex_to_bin[h]
        return binary

    def extract_bits(self, stop=None):
        inc_length = True
        if stop is None:
            stop = len(self.binary)
            inc_length = False
        elif stop > len(self.binary):
            return ''
        
        binary = self.binary[:stop]
        self.binary = self.binary[stop:]

        if inc_length:
            self.length += len(binary)

        return binary

    def parse_literal(self):
        bin_literal = ''
        len_binary = len(self.binary)
        for i in range(0, len_binary, 5):
            first_bit = self.extract_bits(1)
            bin_literal += self.extract_bits(4)
            if first_bit == '0':
                break
        return int(bin_literal, 2)
    
    def get_version_sum(self):
        version_sum = self.version
        for c in (c for c in self.contents if isinstance(c, BITS_Packet)):
            version_sum += c.get_version_sum()
        return version_sum
    
    def __repr__(self):
        string = f'{self.get_version_sum()} --> {str(self)}:'
        string += f'{self.contents}'
        return string

    def __str__(self):
        return f'{self.version}-{self.typeID}'


def part_one(packets, using_sample=False):
    expected_version_sums = [
        6, # D2FE28
        9, # 38006F45291200
        14, # EE00D40C823060
        16, # 8A004A801A8002F478
        12, # 620080001611562C8802118E34
        23, # C0015000016115A2E0802F182340
        31  # A0016C880162017C3686B18A3D4780
    ]
    
    bits_packets = dict()
    actual_version_sums = list()
    for i,hex_packet in enumerate(packets):
        packet = BITS_Packet(hex_packet, is_hex=True)
        bits_packets[hex_packet] = packet
        actual_version_sums.append(packet.get_version_sum())
        
        if using_sample:
            verify_sample(packet.get_version_sum(), expected_version_sums[i])

    for h,bp in bits_packets.items():
        print(f'  {h} version sum = {bp.get_version_sum()}\n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'input.in'
    packets = parse(filename)

    part_one(packets, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')