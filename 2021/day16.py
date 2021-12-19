from bitstruct import unpack_from
from binascii import unhexlify
from itertools import count
from math import prod

with open("day16.txt") as f:
    packet = unhexlify(f.read().strip())


def parse(cursor):
    version, type_id = unpack_from("u3u3", packet, cursor)
    cursor += 6

    if type_id == 4:
        literal = 0
        for num in count(0):
            fivvle = unpack_from("u5", packet, cursor)[0]
            cursor += 5
            literal <<= 4
            literal += fivvle & 0b1111
            if not ((fivvle & 16) >> 4):
                return cursor, version, literal
    else:
        length_type_id = unpack_from("u1", packet, cursor)[0]
        cursor += 1
        if length_type_id:
            subpacket_count = unpack_from("u11", packet, cursor)[0]
            cursor += 11
            subpackets = []
            for _ in range(subpacket_count):
                cursor, subversion, literal = parse(cursor)
                version += subversion
                subpackets.append(literal)
        else:
            subpacket_bits = unpack_from("u15", packet, cursor)[0]
            cursor += 15
            subpackets = []
            until = cursor + subpacket_bits
            while cursor < until:
                cursor, subversion, literal = parse(cursor)
                version += subversion
                subpackets.append(literal)

        if type_id == 0:
            return cursor, version, sum(subpackets)
        elif type_id == 1:
            return cursor, version, prod(subpackets)
        elif type_id == 2:
            return cursor, version, min(subpackets)
        elif type_id == 3:
            return cursor, version, max(subpackets)
        elif type_id == 5:
            return cursor, version, int(subpackets[0] > subpackets[1])
        elif type_id == 6:
            return cursor, version, int(subpackets[0] < subpackets[1])
        elif type_id == 7:
            return cursor, version, int(subpackets[0] == subpackets[1])
        else:
            raise ValueError(version)


_, version_total, result = parse(0)
print(version_total)
print(result)
