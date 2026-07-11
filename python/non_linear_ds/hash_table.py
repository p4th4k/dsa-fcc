'''

'''

class HashTable:
    def __init__(self):
        self.collection = dict()
    
    ''' hash of key is the sum of unicode of all char in a string (in this implementation )'''

    def hash(self, strparam):
        hashedValue = 0
        for char in strparam:
            hashedValue += ord(char)

        return hashedValue

    def add(self, key, value):
        hashOfKey = self.hash(key)
        if hashOfKey in self.collection:
            self.collection[hashOfKey][key] = value
        else:
            self.collection[hashOfKey] = {key: value}

    def remove(self, key):
        hashOfKey = self.hash(key)
        if hashOfKey in self.collection:
            if key in self.collection[hashOfKey]:
                if len(self.collection[hashOfKey]) > 1:
                    del self.collection[hashOfKey][key]
                else:
                    del self.collection[hashOfKey]
    
    def lookup(self, key):
        hashOfKey = self.hash(key)
        if hashOfKey in self.collection:
            if key in self.collection[hashOfKey]:
                return self.collection[hashOfKey][key]
        else:
            return None

    def printTable(self):
        print(self.collection)

if __name__ == "__main__":
    table = HashTable()
    table.add('name', 'Kohli')
    table.add('sport', 'Cricket')
    table.printTable()
