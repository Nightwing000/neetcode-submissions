class MyHashMap:

    def __init__(self):
        self.size=1000
        self.table = [[]for _ in range (self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        ind = self._hash(key)
        for i in self.table[ind]:
            if i[0] == key:
                i[1] = value
                return
        self.table[ind].append([key,value])

    def get(self, key: int) -> int:
        ind = self._hash(key)
        for i in self.table[ind]:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        ind = self._hash(key)
        for i in self.table[ind]:
            if i[0] == key:
                self.table[ind].remove(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)