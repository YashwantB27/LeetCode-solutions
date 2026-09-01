from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find start and give each litter an index
        litter = {}
        sr = sc = 0
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = k
                    k += 1

        # All litter collected
        target = (1 << k) - 1

        # BFS state:
        # (row, col, remaining_energy, mask)
        q = deque([(sr, sc, energy, 0)])

        visited = set()
        visited.add((sr, sc, energy, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                # All litter collected
                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Cannot move without energy
                    if e == 0:
                        continue

                    new_e = e - 1
                    new_mask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        bit = litter[(nr, nc)]
                        new_mask |= (1 << bit)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_e = energy

                    state = (nr, nc, new_e, new_mask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1