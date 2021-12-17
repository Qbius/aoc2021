from math import prod
from inspect import signature
import operator

def parse(raw_input):
    return ''.join(map(lambda c: f'{bin(int(c, 16))[2:]:0>4}', raw_input))

def decimal(string):
    return int(string, 2) if string else 0

registered = []
def match_bitstring(f):
    global registered
    params = [param for param_name, param in signature(f).parameters.items() if param_name != 'feed']
    sections = {param.name: {'index': sum([p.annotation for p in params][:i]), 'length': param.annotation, 'match': param.default} for i, param in enumerate(params)}
    lookup = lambda string, section: decimal(string[section['index']:section['index'] + section['length']])
    test_f = lambda string: all(section['match'] is any or section['match'] == lookup(string, section) for section in sections.values())
    parse_f = lambda string: ({name: lookup(string, section) for name, section in sections.items()} | {'feed': string[sum(p.annotation for p in params):]})
    registered.append((test_f, lambda feed: f(**parse_f(feed))))

def next_packet(feed):
    global registered
    parse_f = next(parse_f for test_f, parse_f in registered if test_f(feed))
    return parse_f(feed)

def exhaust_for_subpackets(feed, subpackets, n=None):
    packet, feed = next_packet(feed)
    subpackets.append(packet)
    return (subpackets, feed) if feed == '' or n == 1 else exhaust_for_subpackets(feed, subpackets, n if n is None else (n - 1))

@match_bitstring
def _(version:3 = any, typeid:3 = 4, feed = ''):
    length = (len(feed[0::5].split('0')[0]) + 1) * 5
    raw_number, feed = feed[:length], feed[length:]
    return {'version': version, 'typeid': typeid, 'value': decimal(''.join(raw_number[i * 5 + 1:i * 5 + 5] for i in range(length // 5)))}, feed

@match_bitstring
def _(version:3 = any, typeid:3 = any, lengthid:1 = 0, subpackets_bits:15 = any, feed = ''):
    subpackets_feed, feed = feed[:subpackets_bits], feed[subpackets_bits:]
    subpackets, _ = exhaust_for_subpackets(subpackets_feed, [])
    return {'version': version, 'typeid': typeid, 'subpackets': subpackets}, feed

@match_bitstring
def _(version:3 = any, typeid:3 = any, lengthid:1 = 1, subpackets_count:11 = any, feed = ''):
    subpackets, feed = exhaust_for_subpackets(feed, [], subpackets_count)
    return {'version': version, 'typeid': typeid, 'subpackets': subpackets}, feed



def sum_versions(tree):
    return tree['version'] + sum(map(sum_versions, tree.get('subpackets', [])))

def first(transmission):
    tree, _ = next_packet(transmission)
    return sum_versions(tree)

def evaluate(tree):
    unpacked = lambda f: lambda subs: f(*subs)
    functions = [sum, prod, min, max, None, unpacked(operator.gt), unpacked(operator.lt), unpacked(operator.eq)]
    return tree['value'] if 'value' in tree else int(functions[tree['typeid']](list(map(evaluate, tree['subpackets']))))

def second(transmission):
    tree, _ = next_packet(transmission)
    return evaluate(tree)

example = '9C0141080250320F1802104A08'