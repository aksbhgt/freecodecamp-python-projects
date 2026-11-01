class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        index = self.hash(key)

        if index not in self.collection:
            self.collection[index] = {}

        self.collection[index][key] = value

    def remove(self, key):
        index = self.hash(key)

        if index in self.collection and key in self.collection[index]:
            del self.collection[index][key]

            if not self.collection[index]:
                del self.collection[index]

    def lookup(self, key):
        index = self.hash(key)

        if index in self.collection:
            return self.collection[index].get(key)

        return None