from dairy import Diary
from entry import Entry


class Dairies:
    def __init__(self):
        self.dairies = []

    def add(self, title, body):
        my_dairy = Diary(title, body)
        self.dairies.append(my_dairy)

    def find_by_user_name(self, user_name) -> Diary:
        for item in self.dairies:
            if item == user_name:
                return item

    def delete(self, user_name, password):
        entry = Diary(user_name, password)
        for item in self.dairies:
            if item == entry:
                self.dairies.remove(entry)
