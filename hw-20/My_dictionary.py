class MyDict(dict):
    def get(self, key, absence = 0):
        return super().get(key, absence)
