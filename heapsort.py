class Heap:
    def __init__(self, keys=None):
        if keys is None:
            self.keys = []
            self.size = 0
            self.height = 0
        else:
            self.keys = keys
            self.size = len(self.keys)
            self.height = self.calculate_height()

    def calculate_height(self):
        i = 0
        while self.size > (2 ** i) - 1:
            i += 1
        self.height = i

    def sift_up(self, index):
        pass

    def target_index(self, a, b):
        pass

    def sift_down(self, index):
        pass

    def pop(self):
        if self.size > 0:
            self.keys[0], self.keys[self.size -
                                    1] = self.keys[self.size-1], self.keys[0]
            self.size -= 1
            self.sift_down(0)

    def sort(self):
        while (self.size > 0):
            self.pop()

    def add(self, keys):
        self.keys.append(keys)
        self.size += 1
        self.calculate()
        self.sift_up()

    def heapify(self, keys=None):
        if keys is not None:
            self.keys = keys
            self.size = len(self.keys)
            self.calculate_height()

        for i in range(self.size-1, -1, -1):
            self.sift_down(i)


class Max_Heap(Heap):
    def __init__(self, keys=None):
        super().__init__(keys)

    def sift_up(self, index):
        if index == 0:
            return
        target = index // 2 - 1
        if self.keys[index - 1] >= self.keys[target]:
            self.keys[index -
                      1], self.keys[target] = self.keys[target], self.keys[index - 1]
            return self.sift_up(target)
        return

    def target_index(self, a, b):
        return a if self.keys[a-1] >= self.keys[b-1] else b

    def sift_down(self, index):
        i = index + 1
        if i * 2 > self.size:
            return
        elif i * 2 == self.size:
            target_index = i * 2 - 1
        else:
            target_index = self.target_index(i*2, i*2+1)-1
        if self.keys[i-1] < self.keys[target_index]:
            self.keys[i-1], self.keys[target_index] = self.keys[target_index], self.keys[i-1]
            i = target_index - 1
            return self.sift_down(i)
        return


class Min_Heap(Heap):
    def __init__(self, keys=None):
        super().__init__(keys)

    def sift_up(self, index):
        if index == 0:
            return
        target = index // 2 - 1
        if self.keys[index - 1] < self.keys[target]:
            self.keys[index -
                      1], self.keys[target] = self.keys[target], self.keys[index - 1]
            return self.sift_up(target)
        return

    def target_index(self, a, b):
        return a if self.keys[a-1] <= self.keys[b-1] else b

    def sift_down(self, index):
        i = index + 1
        if i * 2 > self.size:
            return
        elif i * 2 == self.size:
            target_index = i * 2 - 1
        else:
            target_index = self.target_index(i*2, i*2+1)-1
        if self.keys[i-1] > self.keys[target_index]:
            self.keys[i-1], self.keys[target_index] = self.keys[target_index], self.keys[i-1]
            i = target_index - 1
            return self.sift_down(i)
        return


def heapsort_asc(arr):
    heap = Max_Heap(arr)
    heap.heapify()
    heap.sort()
    return heap.keys


def heapsort_desc(arr):
    heap = Min_Heap(arr)
    heap.heapify()
    heap.sort()
    return heap.keys


arr = [44, 5, 1, 57, 4, 5]
arr = heapsort_desc(arr)
print(arr)
