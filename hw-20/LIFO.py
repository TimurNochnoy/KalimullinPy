class LIFO:

    def __init__(self):
        self.storage = []

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        self.storage.pop(-1)

    def info(self):
        print(self.storage)


class TaskManager():

    def __init__(self):
        self.storage = {}

    def new_task(self, item: str, priority: int):
        if priority not in self.storage:
            self.storage[priority] = [item]
        else:
            self.storage[priority].append(item)
        lst_keys = list(self.storage.keys())
        lst_keys.sort()
        dct = {}
        for key in lst_keys:
            if key not in dct:
                dct[key] = self.storage[key]
            else:
                dct[key].append(self.storage[key])
        self.storage = dct

    def delete_task(self, item: str, priority: int):
        if len(self.storage[priority]) == 1:
            del self.storage[priority]
        else:
            for i in range(len(self.storage[priority])):
                if self.storage[priority][i] == item:
                    index = i
            del self.storage[priority][index]

    def info(self):
        for key in self.storage:
            print(key, end=' ')
            if len(self.storage[key]) == 1:
                print(self.storage[key][0])
            else:
                for i in range(len(self.storage[key]) - 1):
                    print(self.storage[key][i], end='; ')
                print(self.storage[key][len(self.storage[key]) - 1])
