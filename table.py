class KeyValue:
    def __init__(self, hex_, binary, ascii_):
        self.hex = hex_
        self.binary = binary
        self.ascii = ascii_  # key

    def __str__(self):
        return f"{self.hex}   {self.binary}   {self.ascii}"

    def __eq__(self, other):
        result = False
        if other is not None:
            result = self.hex == other.hex and self.binary == other.binary and self.ascii == other.ascii
        return result


class Table:
    def __init__(self, capacity=128):
        capacity = 2 * capacity
        self.actual_size = self.find_prime(capacity)
        self.table = [None] * self.actual_size
        self.num_entries = 0

    def store(self, hex_, binary, ascii_):
        index = abs(hash(ascii_)) % self.actual_size
        if self.table[index] is None:  # not occupied
            self.table[index] = KeyValue(hex_, binary, ascii_)
            self.num_entries += 1
        else:  # occupied
            while self.table[index] is not None:
                index += 1
                index %= self.actual_size
            self.table[index] = KeyValue(hex_, binary, ascii_)
            self.num_entries += 1

        if self.load() >= 2 / 3:
            self.re_hash()

    def get(self, key):
        if key == " ":
            key = "Space"
        index = abs(hash(key)) % self.actual_size
        while self.table[index] is not None:
            if self.table[index].ascii == key:
                return self.table[index]
            index += 1
            index %= self.actual_size
        raise KeyError

    def re_hash(self):  # there's enough space, this should never run
        print("---------REHASH IS RUNNING---------")
        temp_actual_size = self.find_prime(self.actual_size * 1.5 * 2)
        temp_table = [None] * temp_actual_size

        for key_value in self.table:
            if key_value is not None:
                index = abs(hash(key_value.ascii_)) % temp_actual_size
                while temp_table[index] is not None:
                    index += 1
                    index %= temp_actual_size
                temp_table[index] = key_value

        self.table = temp_table.copy()
        self.actual_size = temp_actual_size

    def __str__(self):
        result = ""
        for value in self.table:
            if value is not None:
                result += f"{value}\n"
        return result

    def keys(self):
        result = set()
        for key_value in self.table:
            if key_value is not None:
                if key_value.ascii is not None:
                    result.add(key_value.ascii)
        return result

    def load(self):
        return self.num_entries / self.actual_size

    def __len__(self):
        return self.num_entries

    def is_prime(self, num_to_check):
        self
        is_prime = True
        i = 2
        while (i * i) <= num_to_check:
            if num_to_check % i == 0:
                is_prime = False
            i += 1
        return is_prime

    def find_prime(self, start):
        start = int(start)
        while not self.is_prime(start):
            start += 1
        return start
