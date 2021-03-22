# Python does not have built-in support for arrays, but python lists/tuples/strings can be used instead
# To work with arrays, one can import a library such as Numpy


# Dynamic Array Implementation:
import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0  # number of elements
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('k is out of bounds')

        return self.A[k]

    def append(self, ele):

        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

# Below are test
a = DynamicArray()
assert len(a) == 0
a.append(1)
a.append(2)
assert len(a) == 2
a.append(3)
assert a.n == 3
assert a.capacity == 4
print(a[3])  # expected: k is our of bounds
