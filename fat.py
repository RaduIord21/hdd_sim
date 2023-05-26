#disk_size = 4096 UA
#allocation unit size = 16 (2B)

import root

class fat_table:

    def __init__(self):
        self.fat = []
        self.root = []
        for each in range(4096):
            self.fat.append(0)
        for each in range(512):
            self.fat[each] = 1
        for each in range(self.fat.index(0), self.fat.index(0) + 64):
            self.fat[each] = 2

    def add_to_root(self):
        pass


    def create_file(self, size):
        for each in range(size - 1):
            last_index = self.fat.index(0)
            self.fat[last_index] = -1
            current_index = self.fat.index(0)
            self.fat[last_index] = current_index
        self.fat[self.fat.index(0)] = 3
        print(self.fat)


obj = fat_table()

obj.create_file(5)

