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
        """
        str method to return information about the KeyValue class
        """
        return f"{self._hex}   {self._binary}   {self._ascii}"

    # getters
    def get_hex(self):
        return self._hex

    def get_binary(self):
        return self._binary

    def get_ascii(self):
        return self._ascii


class HashTable:
    def __init__(self, capacity=257):
        """
        Constructor/Inititalizer
        :param capacity: the size of the data to store
        """
        # for this program, the table would never need to resize
        # load factor will always be < 50%
        self.actual_size = capacity
        self._table = [None] * self.actual_size

    def store(self, hex_, binary, ascii_):
        """
        This method stores the hex code, binary value and ascii code as type KeyValue.
        Collisions will be resolved using linear probing
        :param hex_: the hex value, also the key
        :param binary: the binary equivalent
        :param ascii_: the ascii code equivalent
        """
        index = abs(hash(hex_)) % self.actual_size
        if self._table[index] is None:  # not occupied, insert
            self._table[index] = KeyValue(hex_, binary, ascii_)
        else:  # occupied, resolve collision
            while self._table[index] is not None:
                index += 1
                index %= self.actual_size  # wrap around
            # at the end of the loop, an empty spot would have been found, insert there
            self._table[index] = KeyValue(hex_, binary, ascii_)

    def get(self, key):
        """
        To get and return the value associated with the key (hex)
        :param key: the key used for hashing. i.e hex_
        :return: A KeyValue object associated with the Key
        :raise: KeyValue exception if the key was not found
        """
        index = abs(hash(key)) % self.actual_size  # get the has code

        while self._table[index] is not None:  # start looping from the index
            curr = self._table[index]
            if curr.get_hex() == key:  # loop till the key is found
                return curr  # and return it
            index += 1
            index %= self.actual_size
        raise KeyError  # key was not found, raise KeyError

    def __str__(self):
        """
        Standard toString method
        :return: a string containing all the elements in the hash table, separated by a new line
        """
        result = ""
        for value in self._table:
            if value is not None:
                result += f"{value}\n"
        return result
