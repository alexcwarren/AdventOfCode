from math import prod


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
    operationIDs = {
        0: 'sum',
        1: 'product',
        2: 'minimum',
        3: 'maximum',
        4: 'literal',
        5: 'greater_than',
        6: 'less_than',
        7: 'equal_to'
    }
    
    operations = {
        'sum': (lambda x : sum(x)),
        'product': (lambda x : prod(x)),
        'minimum': (lambda x : min(x)),
        'maximum': (lambda x : max(x)),
        'greater_than': (lambda x : 1 if x[0] > x[1] else 0),
        'less_than': (lambda x : 1 if x[0] < x[1] else 0),
        'equal_to': (lambda x : 1 if x[0] == x[1] else 0)
    }

    def __init__(self, packet_str, is_hex=False):
        self.hex = None
        if is_hex:
            self.hex = packet_str
            self.binary = self.to_binary(packet_str)
        else:
            self.binary = packet_str
        self.init_binary = self.binary
        self.length = 0
        self.version = int(self.extract_bits(3), 2)
        self.typeID = int(self.extract_bits(3), 2)
        self.operationID = BITS_Packet.operationIDs[self.typeID]
        self.lengthID = None
        self.contents = list()

        if self.operationID == 'literal':
            self.contents.append(self.parse_literal())
        else:
            self.lengthID = self.extract_bits(1)
            if self.lengthID == '0':
                length_subpackets = int(self.extract_bits(15), 2)
                while length_subpackets > 0:
                    subpacket = self.parse_subpacket()
                    length_subpackets -= subpacket.length
                    self.contents.append(subpacket)
            else:
                num_subpackets = int(self.extract_bits(11), 2)
                while len(self.contents) < num_subpackets:
                    subpacket = self.parse_subpacket()
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
    
    def parse_subpacket(self):
        sub_packet = BITS_Packet(self.extract_bits())
        self.binary = sub_packet.binary
        self.length += sub_packet.length
        return sub_packet
    
    def get_version_sum(self):
        version_sum = self.version
        for c in (c for c in self.contents if isinstance(c, BITS_Packet)):
            version_sum += c.get_version_sum()
        return version_sum
    
    def evaluate(self):
        print(self)
        return 0
        # operands = list()
        # print('evaluating...')
        # print(repr(self))
        # for c in self.contents:
        #     if isinstance(c, BITS_Packet):
        #         if c.operationID == 'literal':
        #             return c.contents
        #             # operands.extend(('literal', c.contents))
        #         else:
        #             operands.append(c.evaluate())
        #     else:
        #         return c
        #         # operands.append(c)
        # print(operands)
        # return (self.operationID, operands)
    
    def __repr__(self):
        string = ''
        if self.hex is not None:
            string += f'{self.hex}\n'
        else:
            string += f'{self.init_binary}\n'
        string += f'  length={self.length}\n'
        string += f'  version={self.version}\n'
        string += f'  typeID={self.typeID}\n'
        string += f'  operation={self.operationID}\n'
        string += f'  lengthID={self.lengthID}\n'
        string +=  '  contents=['
        for i,c in enumerate(self.contents):
            if i > 0:
                string += ', '
            string += f'{str(c)}'
        string += ']\n'
        return string

    def __str__(self):
        string = ''
        if self.operationID != 'literal':
            string = f'{self.operationID}('
        for i,c in enumerate(self.contents):
            if i > 0:
                string += ', '
            string += str(c)
        if self.operationID != 'literal':
            string += ')'
        return string


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
    expected_results = [
        6,  # D2FE28
        9,  # 38006F45291200
        14, # EE00D40C823060
        16, # 8A004A801A8002F478
        12, # 620080001611562C8802118E34
        23, # C0015000016115A2E0802F182340
        31  # A0016C880162017C3686B18A3D4780
    ]
    
    for i,hex_packet in enumerate(packets):
        packet = BITS_Packet(hex_packet, is_hex=True)
        result = packet.evaluate()
        
        # if using_sample:
        #     verify_sample(result, expected_results[i])
        
        print(f'  {hex_packet} result = {result}\n')


if __name__ == '__main__':
    filename = 'sample.in'
    packets = parse(filename)

    # part_one(packets, filename == 'sample.in')

    part_two(packets, filename == 'sample.in')