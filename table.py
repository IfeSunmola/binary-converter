class KeyValue:
    """
    Represents a key value pair stored in the hash table
    _hex will be used as the key
    """

    def __init__(self, hex_, binary, ascii_):
        self._hex = hex_
        self._binary = binary
        self._ascii = ascii_

    def __str__(self):
        return f"{self._hex}   {self._binary}   {self._ascii}"

    def get_hex(self):
        return self._hex

    def get_binary(self):
        return self._binary

    def get_ascii(self):
        return self._ascii


class HashTable:
    def __init__(self, capacity=257):
        # for this program, the table would never need to resize
        # load factor will always be < 50%
        self.actual_size = capacity
        self._table = [None] * self.actual_size

    def store(self, hex_, binary, ascii_):
        index = abs(hash(hex_)) % self.actual_size
        if self._table[index] is None:  # not occupied
            self._table[index] = KeyValue(hex_, binary, ascii_)
        else:  # occupied, resolve collision
            while self._table[index] is not None:
                index += 1
                index %= self.actual_size
            self._table[index] = KeyValue(hex_, binary, ascii_)

    def get(self, key):
        index = abs(hash(key)) % self.actual_size

        while self._table[index] is not None:
            curr = self._table[index]
            if curr.get_hex() == key:
                return curr
            index += 1
            index %= self.actual_size
        raise KeyError

    def __str__(self):
        result = ""
        for value in self._table:
            if value is not None:
                result += f"{value}\n"
        return result
