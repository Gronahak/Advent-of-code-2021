class PacketParser():
    def __init__(self):
        self.bits = ""
        self.read_at = 0
        self.sum_of_versions = 0

    def read(self, n=1):
        try:
            out = self.bits[self.read_at:self.read_at + n]
            self.read_at += n
            return out
        except IndexError:
            return None

    def parse(self, f):
        correspondance = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111",
        }

        for l in f.readlines():
            l = l.strip()
            for hex_char in l:
                self.bits += correspondance[hex_char]
        self.stream_length = len(self.bits)

    def parse_litteral_data(self):
        next_part = self.read(5)
        binary_repr = ""

        while next_part[0] == "1":
            binary_repr += next_part[1:]
            next_part = self.read(5)
        
        binary_repr += next_part[1:]

        return int(binary_repr, 2)

    def parse_packet(self):
        packet_version = int("0b"+self.read(3), 2)
        self.sum_of_versions += packet_version
        packet_type_id = int("0b"+self.read(3), 2)

        if packet_type_id == 4:  # litteral value packet
            literral_value = self.parse_litteral_data()
            return literral_value

        else:  # operator packet
            length_type_id = int(self.read())

            sub_packets_values = []

            if length_type_id == 0:
                total_subpackets_length = int(self.read(15), 2)
                threshold = self.read_at + total_subpackets_length
                while self.read_at < threshold:
                    sub_packets_values.append(self.parse_packet())
            elif length_type_id == 1:
                n_sub_packets = int(self.read(11), 2)
                for _ in range(n_sub_packets):
                    sub_packets_values.append(self.parse_packet())

            if packet_type_id == 0:  # sum packet
                out = 0
                for val in sub_packets_values:
                    out += val

            if packet_type_id == 1:  # product packet
                out = 1
                for val in sub_packets_values:
                    out *= val

            if packet_type_id == 2:  # minimum packet
                out = min(sub_packets_values)
            
            if packet_type_id == 3:  # maximum packet
                out = max(sub_packets_values)

            if packet_type_id == 5:  # gt packet
                out = 0
                if sub_packets_values[0] > sub_packets_values[1]:
                    out = 1
            
            if packet_type_id == 6:  # lt packet
                out = 0
                if sub_packets_values[0] < sub_packets_values[1]:
                    out = 1
            
            if packet_type_id == 7:  # eq packet
                out = 0
                if sub_packets_values[0] == sub_packets_values[1]:
                    out = 1


            return out
    def decode(self):
        while self.read_at < self.stream_length:
            # try:
                out = self.parse_packet()
                print(out)
            # except ValueError:
            #     print("error decoding packet")
            #     pass

    def show_answer_p1(self):
        self.decode()
        # print(self.sum_of_versions)