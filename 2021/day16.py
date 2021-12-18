# Part 1
from collections import namedtuple

bits = ''.join(bin(int(char, 16))[2:].zfill(4) for char in text)

def parse(offset):
    version = int(bits[offset:(offset + 3)], 2)
    type_id = int(bits[(offset + 3):(offset + 6)], 2)
    if type_id == 4:
        offset += 6
        parts = []
        while True:
            group = bits[offset:(offset + 5)]
            parts.append(group[1:])
            offset += 5
            if group[0] == '0':
                break
        num = int(''.join(parts), 2)
        return offset, (version, type_id, num)
    else:
        length_type_id = bits[offset + 6]
        if length_type_id == '0':
            total_length = int(bits[(offset + 7):(offset + 22)], 2)
            offset += 22
            end_offset = offset + total_length
            packets = []
            while offset < end_offset:
                offset, packet = parse(offset)
                packets.append(packet)
            return offset, (version, type_id, packets)
        else:
            assert length_type_id == '1'
            sub_packets = int(bits[(offset + 7):(offset + 18)], 2)
            offset += 18
            packets = []
            for _ in range(sub_packets):
                offset, packet = parse(offset)
                packets.append(packet)
            return offset, (version, type_id, packets)

_, packet = parse(0)

def add(packet):
    version, _, value = packet
    if isinstance(value, int):
        return version
    else:
        return version + sum(map(add, value))

print(add(packet))

# Part 2
import math

def evaluate(packet):
    version, type_id, value = packet
    if type_id == 0:
        return sum(map(evaluate, value))
    elif type_id == 1:
        return math.prod(map(evaluate, value))
    elif type_id == 2:
        return min(map(evaluate, value))
    elif type_id == 3:
        return max(map(evaluate, value))
    elif type_id == 4:
        return value
    elif type_id == 5:
        packet_a, packet_b = map(evaluate, value)
        return int(packet_a > packet_b)
    elif type_id == 6:
        packet_a, packet_b = map(evaluate, value)
        return int(packet_a < packet_b)
    else:
        assert type_id == 7
        packet_a, packet_b = map(evaluate, value)
        return int(packet_a == packet_b)

print(evaluate(packet))
