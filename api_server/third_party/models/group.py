from .lessons_per_day import LessonsPerDay


class Group:
    DAY_TITLES = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА']

    def __init__(self, name):
        self.days = []
        self.name = name

    def append(self, lesson):
        try:
            self.days[-1].append(lesson)
        except IndexError:
            lpd = LessonsPerDay()
            lpd.append(lesson)
            self.days.append(lpd)

    def to_dict(self):
        week = {Group.DAY_TITLES[i]: [*self.days[i]] for i in range(len(Group.DAY_TITLES))}
        return week
