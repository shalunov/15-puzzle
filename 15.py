#!/usr/bin/env python3
# Use A* search to solve the Game of 15. By Stanislav Shalunov, July 2017.

from queue import PriorityQueue

N=4

def moves(position):
    assert set(position) == set(range(N*N))
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

def board_str(position):
    return '\n'.join((N*'{:3}').format(*[(i+1)%(N*N) for i in position[i:]]) for i in range(0, N*N, N))

class Path:
    def __init__(self, positions):
        self.positions = positions
        self.loss = loss(self.last())
    def __lt__(self, other): return self.loss < other.loss
    def last(self): return self.positions[-1]
    def __str__(self): return '\n\n'.join([board_str(p) for p in self.positions])

path = Path([tuple((i-1)%16 for i in (2, 4, 6, 12, 1, 5, 8, 3, 9, 10, 15, 11, 13, 14, 7, 0))])
candidates = PriorityQueue()
candidates.put(path)
visited = set([path.last()])
while path.last() != tuple(range(N*N)):
    path = candidates.get()
    for k in moves(path.last()):
        if k not in visited:
            candidates.put(Path(path.positions + [k]))
            visited.add(k)
print(path)
