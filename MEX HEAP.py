import sys

class MaxHeap:
    def __init__(self):
        self.heap = [0]  # Index 0 is unused

    def push(self, k):
        self.heap.append(k)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        while i > 1:
            parent = i // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def pop(self):
        if len(self.heap) <= 1:
            return None
        max_val = self.heap[1]
        last = self.heap.pop()
        if len(self.heap) > 1:
            self.heap[1] = last
            self._sift_down(1)
        return max_val

    def _sift_down(self, i):
        size = len(self.heap)
        while True:
            left = 2 * i
            right = 2 * i + 1
            largest = i
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

def main():
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    heap = MaxHeap()
    line = 1
    for a in range(N):
        op = data[line].split()
        line += 1
        if op[0] == 'push':
            k = int(op[1])
            heap.push(k)
        elif op[0] == 'peek':
            res = heap.peek()
            print(res if res is not None else 'null')
        elif op[0] == 'pop':
            res = heap.pop()
            print(res if res is not None else 'null')

if __name__ == "__main__":
    main()