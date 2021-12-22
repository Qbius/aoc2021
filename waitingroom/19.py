from itertools import chain, permutations, pairwise
from collections import Counter
from time import time

prmindcs = list(permutations((0, 1, 2), 3))
binconfs = [[1 if c == '0' else -1 for c in binnum] for binnum in [f'{bin(i)[2:]:0>3}' for i in range(8)]]
class scanner(object):
    def __init__(self, points):
        self.points = points
        self.regenerate_diffs()
        self.pathto0 = []
        self.relativeto0 = None

    def adjust(self, permindices, rotation):
        (ai, bi, ci), (aconf, bconf, cconf) = permindices, rotation
        self.points = [(aconf * p[ai], bconf * p[bi], cconf * p[ci]) for p in self.points]
        self.regenerate_diffs()

    def move(self, relative):
        ra, rb, rc = relative
        self.points = [(a + ra, b + rb, c + rc) for a, b, c in self.points]
        self.regenerate_diffs()

    def adjusted_copy(self, permindices, rotation):
        (ai, bi, ci), (aconf, bconf, cconf) = permindices, rotation
        adj_points = [(aconf * p[ai], bconf * p[bi], cconf * p[ci]) for p in self.points]
        return scanner(adj_points)

    def regenerate_diffs(self):
        self.diffind = [((a1 - a2, b1 - b2, c1 - c2), (i, j)) for i, (a1, b1, c1) in enumerate(self.points) for j, (a2, b2, c2) in enumerate(self.points) if i != j]
        self.diffpoints = [points for points, _ in self.diffind]
        self.diffindics = dict(self.diffind)
        self.alldiff = {(p[ai] * aconf, p[bi] * bconf, p[ci] * cconf): ((ai, bi, ci), (aconf, bconf, cconf)) for p in self.diffpoints for ai, bi, ci in prmindcs for aconf, bconf, cconf in binconfs}

def parse(raw_input):
    return [scanner([tuple(int(n) for n in line.strip().split(',')) for line in section.split('\n')[1:]]) for section in raw_input.split('\n\n')]

def find_common_points(s1, s2):
    match next((s2.alldiff[s1p] for s1p in s1.diffpoints if s1p in s2.alldiff), None):
        case (permindices, rotation):
            s2adjusted = s2.adjusted_copy(permindices, rotation)
            pairs = [(s1.diffindics[a], s2adjusted.diffindics[b]) for a in s1.diffpoints for b in s2adjusted.diffpoints if a == b]
            s1inter = set(chain(*[[a1, a2] for (a1, a2), _ in pairs]))
            common = [(a, Counter(chain(*[[b1, b2] for (a1, a2), (b1, b2) in pairs if a == a1 or a == a2])).most_common(1)[0][0]) for a in s1inter]
            [(s1fcommon, s2fcommon), *_] = common
            relative = tuple((t1 + t2) for t1, t2 in zip(s1.points[s1fcommon], s2adjusted.points[s2fcommon]))
            return {'common': common, 'relative': relative, 'permindices': permindices, 'rotation': rotation} if len(common) >= 12 else None
        case _:
            return None

def common_points_map(scanners):
    scanner_pairs = [((i, s1), (j, s2)) for i, s1 in enumerate(scanners) for j, s2 in enumerate(scanners) if i != j]
    return {(i, j): find_common_points(s1, s2) if any(s1p in s2.alldiff for s1p in s1.diffpoints) else None for (i, s1), (j, s2) in scanner_pairs}

def build_paths_to_0(scanners, common_map, root, found_parent, path):  
    children = [i for i in range(1, len(scanners)) if i != root and i not in found_parent and common_map[root, i] is not None]
    for child in children:
        scanners[child].pathto0 = [*path, root]
        found_parent.add(child)
        build_paths_to_0(scanners, common_map, child, found_parent, path + [root])

def first(scanners):
    start = time()
    common_map = common_points_map(scanners)
    build_paths_to_0(scanners, common_map, 0, set(), [])
    points = set(chain(*[s.points for s in scanners]))
    print()
    for i, s in enumerate(scanners):
        if not s.pathto0: continue
        [firstpair, *restpair] = list(pairwise([*s.pathto0, i]))
        res = common_map[firstpair]['relative']
        to_prm = common_map[firstpair]['permindices']
        to_rot = common_map[firstpair]['rotation']
        for crr, nxt in restpair:
            ia, ib, ic = to_prm
            rta, rtb, rtc = to_rot
            ra, rb, rc = res
            relative = common_map[crr, nxt]['relative']
            res = [relative[ia] - ra * rta, relative[ib] - rb * rtb, relative[ic] - rc * rtc]
            to_prm = common_map[crr, nxt]['permindices']
            to_rot = common_map[crr, nxt]['rotation']
        s.relativeto0 = tuple(res)
        print(i, s.relativeto0, to_rot)


    return len(points)
    end = time()
    print(end - start)
    # populate_parents(scanners)
    # for i, s in enumerate(scanners):
    #     print(i, s.parents)
    # print(set(chain(*[s.parents for s in scanners])))


def second(values):
    pass

{'relative': (68, -1246, -43), 'permindices': (0, 1, 2), 'rotation': (1, -1, 1)}
{'relative': (88, 113, -1104), 'permindices': (1, 2, 0), 'rotation': (-1, 1, 1)}
-20,-1133,1061 

{(68, -1246, -43), (0, 1, 2), (1, -1, 1)}
{(88, 113, -1104), (1, 2, 0), (-1, 1, 1)}
{(168, -1125, 72), (1, 0, 2), (1, 1, -1)}

-20,-1133,1061 
168, -1125, 72

1105,-1205,1229

example = '''
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
'''

(0, 1, 2), (1, 1, 1)

(1, 0, 2), (-1, 1, 1)

(0, 2, 1), (1, )