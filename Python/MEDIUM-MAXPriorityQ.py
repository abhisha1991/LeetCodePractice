import sys
class MaxPriorityQ(object):
    def __init__(self, cap):
        self.size = 0
        self.q = [sys.maxsize]
        self.cap = cap

    def findMax(self):
        return self.q[1]

    def insert(self, element):
        self.q.append(element)
        self.size += 1
        if self.size is 1:
            print("inserted element", element)
            return
        idx = self.size
        parent = int(idx/2)
        while self.q[idx] > self.q[parent]:
            self.swap(idx, parent)
            idx = parent
            parent = int(idx/2)
            if idx == 1:
                break

        print("inserted element", element)

        if self.size > self.cap:
            print("capacity is reached! Deleting max ", self.findMax())
            self.deleteMax()

    def deleteMax(self):
        self.swap(1, self.size)
        element = self.q[self.size]
        print("deleting max element ", element)
        self.size -= 1
        if self.size < 2:
            self.print()
            return
        # bubble up largest element to the top
        # the element who is at q[1] may not be the largest any more
        parent = 1
        left = self.getLeftidx(parent)
        right = self.getRightidx(parent)
        leftsmaller = self.q[parent] > self.q[left]
        if self.size == 2:
            if leftsmaller:
                pass
            else:
                self.swap(1, 2)
            self.print()
            return

        rightsmaller = self.q[parent] > self.q[right]
        while leftsmaller is False or rightsmaller is False:
            leftbiggest = True
            if (leftsmaller or rightsmaller) is False:
                # both are bigger than parent
                leftbiggest = self.q[left] > self.q[right]

            if leftbiggest and leftsmaller is False:
                self.swap(parent, left)
                parent = left
                left = self.getLeftidx(parent)
                if left > self.size:
                    break
                leftsmaller = self.q[parent] > self.q[left]
            else:
                self.swap(parent, right)
                parent = right
                right = self.getRightidx(parent)
                if right > self.size:
                    break
                rightsmaller = self.q[parent] > self.q[right]

        self.print()

    def getLeftidx(self, parent):
        return 2 * parent

    def getRightidx(self, parent):
        return 2 * parent + 1

    def size(self):
        return self.size

    def swap(self, i, j):
        temp = self.q[i]
        self.q[i] = self.q[j]
        self.q[j] = temp

    def print(self):
        print("Heap is")
        for i in range(1, self.size + 1):
            print(self.q[i])

s = MaxPriorityQ(5)
s.insert(4)
s.insert(4)
s.insert(8)
s.print()
s.insert(9)
s.print()
s.insert(19)
s.print()
s.insert(119)
s.deleteMax()
s.deleteMax()
s.deleteMax()
s.deleteMax()