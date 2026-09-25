class Allocator:
    def __init__(self, n: int):
        self.mem = [None] * n
        self.mp = {}  # mID -> list of (start, size)

    def allocate(self, size: int, mID: int) -> int:
        curr = 0

        for i in range(len(self.mem)):
            if self.mem[i] is None:
                curr += 1
            else:
                curr = 0

            if curr == size:
                start = i - size + 1

                for j in range(start, start + size):
                    self.mem[j] = mID

                self.mp.setdefault(mID, []).append((start, size))
                return start

        return -1

    def freeMemory(self, mID: int) -> int:
        blocks = self.mp.pop(mID, None)

        if blocks is None:
            return 0

        freed = 0

        for start, size in blocks:
            for i in range(start, start + size):
                self.mem[i] = None
                freed += 1

        return freed