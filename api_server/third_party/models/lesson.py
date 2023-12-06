class Lesson:
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def get(self):
        return self.__dict__
