from itertools import chain

def parse(raw_input):
    pathtuples = [tuple([e.strip() for e in line.split('-')]) for line in raw_input.split('\n')]
    reversed = [(b, a) for a, b in pathtuples]
    all_paths = pathtuples + reversed
    uniquepaths = {path for path, _ in all_paths}
    return {path: [v for k, v in all_paths if k == path] for path in uniquepaths}

def branchout(current, paths):
    last = current[-1]
    if last == 'end':
        return [current]
    else:
        return list(chain(*[branchout([*current, option], paths) for option in paths[current[-1]] if (option == option.upper()) or option not in current]))

def first(paths):
    return len(branchout(['start'], paths))

def branchout2(current, paths, canrepeat):
    last = current[-1]
    if last == 'end':
        return [current]
    else:
        return list(chain(*[branchout2([*current, option], paths, ((option == option.upper()) or option not in current) and canrepeat) for option in paths[current[-1]] if (option == option.upper()) or option not in current or (canrepeat and option not in ['start', 'end'])]))

def second(paths):
    return len(branchout2(['start'], paths, True))

example = '''
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''