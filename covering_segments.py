# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key=attrgetter('end'))
    #print(segments)
    
    covered = False
    while len(segments)>0:
        points.append(segments[0].end)
        while (len(segments) > 0) and (segments[0].start < points[-1] + 1):
            del segments[0]
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
