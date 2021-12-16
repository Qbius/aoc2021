from math import prod
import operator

def parse(raw_input):
    mapped = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    for frm, to in mapped.items():
        raw_input = raw_input.replace(frm, to)
    return raw_input

def parse_packet(feed):
    version, typeid = int(feed[:3], 2), int(feed[3:6], 2)
    if typeid == 4:
        feed = feed[6:]
        number = ''
        while True:
            number += feed[1:5]
            first = feed[0]
            feed = feed[5:]
            if first == '0':
                break
        number = int(number, 2)
        return {'version': version, 'typeid': typeid, 'value': number}, feed
    else:
        length_id = feed[6]
        feed = feed[7:]
        subpackets = []
        if length_id == '0':
            subpacketbits = int(feed[:15], 2)
            feed = feed[15:]
            subpackets_feed = feed[:subpacketbits]
            feed = feed[subpacketbits:]
            while subpackets_feed:
                subpacket, subpackets_feed = parse_packet(subpackets_feed)  
                subpackets.append(subpacket)
        else:
            subpacketcount = int(feed[:11], 2) if feed[:11] != '' else 0
            feed = feed[11:]
            for _ in range(subpacketcount):
                subpacket, feed = parse_packet(feed)
                subpackets.append(subpacket)
        return {'version': version, 'typeid': typeid, 'subpackets': subpackets}, feed

def add_versions(tree):
    return tree['version'] + sum(map(add_versions, tree.get('subpackets', [])))

def first(transmission):
    tree, _ = parse_packet(transmission)
    return add_versions(tree)

def evaluate(tree):
    if 'value' in tree:
        return tree['value']
    else:
        repack = lambda f: lambda *subs: f(subs)
        functions = [repack(sum), repack(prod), repack(min), repack(max), None, operator.gt, operator.lt, operator.eq]
        f = functions[tree['typeid']]
        evaluated = list(map(evaluate, tree['subpackets']))
        return int(f(*evaluated))

def second(transmission):
    tree, _ = parse_packet(transmission)
    return evaluate(tree)

example = '9C0141080250320F1802104A08'