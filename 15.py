#!/usr/bin/env python3
# Use A* search to solve the Game of 15. By Stanislav Shalunov, M.Andreev July 2017.

from queue import PriorityQueue
from random import shuffle

N=4

def moves(position):
    blank = position.index(N*N-1)
    i, j = divmod(blank, N)
    offsets = []
    if i>0: offsets.append(-N)  # Down
    if i<N-1: offsets.append(N) # Up
    if j>0: offsets.append(-1)  # Right
    if j<N-1: offsets.append(1) # Left
    for offset in offsets:
        swap = blank + offset
        yield tuple(position[swap] if x==blank else position[blank] if x==swap else position[x] for x in range(N*N))

def loss(position):
    return sum(abs(i//N - position[i]//N) + abs(i%N - position[i]%N) for i in range(N*N))

def parity(permutation):
    assert set(permutation) == set(range(N*N))
    #return sum(x<y and px>py for (x, px) in enumerate(permutation) for (y, py) in enumerate(permutation))%2
    seen, cycles = set(), 0
    for i in permutation:
        if i not in seen:
            cycles += 1
            while i not in seen:
                seen.add(i)
                i = permutation[i]
    return (cycles+len(permutation)) % 2

class Position: # For PriorityQueue, to make "<" do the right thing.
    def __init__(self, position, start_distance):
        self.position = position
        self.loss = loss(position)
        self.start_distance = start_distance
    def __lt__(self, other): return self.loss + self.start_distance < other.loss + other.start_distance # All we want, really.
    def __str__(self): return '\n'.join((N*'{:3}').format(*[(i+1)%(N*N) for i in self.position[i:]]) for i in range(0, N*N, N))

start = list(range(N*N-1))
shuffle(start)
start += [N*N-1]
start = tuple(start)
assert parity(start) == 0
p = Position(start, 0)
candidates = PriorityQueue()
candidates.put(p)
visited = set([p]) # Tuples rather than lists so they go into a set.
came_from = {p.position: None}

while p.position != tuple(range(N*N)):
    p = candidates.get()
    for k in moves(p.position):
        if k not in visited:
            candidates.put(Position(k,p.start_distance+1))
            came_from[k] = p
            visited.add(k)

while p.position != start:
    print(p, "\n")
    p = came_from[p.position]

import resource
print((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss), 'RAM')
