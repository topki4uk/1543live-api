class LessonsPerDay:

    def __init__(self):
        self.lessons = []

    def append(self, item):
        if len(self.lessons) >= 8:
            raise IndexError

        self.lessons.append(item)

    def __getitem__(self, item):
        return self.lessons[item]

    def __iter__(self):
        return iter([lesson.get() for lesson in self.lessons])
