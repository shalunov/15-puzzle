# 15-puzzle
We implement different search algorithms to find a path from (random) start position to position, where puzzle is solved.

Three different algorithms are present:

1. Greedy search - empirically the fastest one, but it finds one of the paths from start position to end position, no guarantee that this path is optimal.
1. Dijkstra algorithm - classical distance search algorithm. Guarantees the shortest path, but require lots of resource.
1. A\* search - Guarantees shortest path, works faster and require less resource than Dijkstra.
