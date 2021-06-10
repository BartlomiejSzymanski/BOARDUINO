class Player:
    def __init__(self, name, team):
        self.__fields = []
        self.__respect = 0
        self.name = name
        self.team = team

    # def get_name(self):
    #     return self.__name

    def get_respect(self):
        return self.__respect

    def update_respect(self, value):
        self.__respect += value

    # def set_name(self, name):
    #     self.__name = name

    def add_turn(self, field, respect=0):
        self.__fields.append(field)
        if respect:
            self.update_respect(respect)

    def last_field(self):
        if len(self.__fields) >= 2:
            return self.__fields[-2]
        else:
            return 1

    def current_field(self):
        if len(self.__fields):
            return self.__fields[-1]
        else:
            return 1

    def __str__(self):
        return f'{self.name} ({self.team})'
