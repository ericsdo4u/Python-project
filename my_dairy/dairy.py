from entry import Entry


class Diary:
    # global id

    def __init__(self, user_name, password):
        self.number_of_entry = 0
        self.user_name = user_name
        self.password = password
        self.islocked = False
        self.entries = []
        self.entry_id = 0

    def get_password(self):
        return self.password

    def is_locked(self):
        return self.islocked

    def get_id_number(self) -> int:
        self.entry_id += 1
        return self.entry_id

    def get_number_of_entry(self) -> int:
        return len(self.entries)

    def create_entry(self, title, body):
        if self.islocked:
            raise ValueError("Dairy is locked, unlock diary to create entry")
        if not self.islocked:
            entry_id = self.get_id_number()
            new_entry = Entry(entry_id, title, body)
            self.entries.append(new_entry)

    def find_entry_by_id(self, entry_id) -> Entry:
        for item in self.entries:
            if item.get_entry_id() == entry_id:
                return item

    def delete_entry(self, entry_id):
        for item in self.entries:
            if item.get_entry_id() == entry_id:
                self.entries.remove(item)

    def update_entry(self, entry_id, title, body):
        entry = self.find_entry_by_id(entry_id)
        for entry1 in self.entries:
            if entry == entry1:
                entry1.update_body(body)
                entry1.update_title(title)

    def lock_dairy(self):
        self.islocked = True

    def unlock_dairy(self, password):
        if self.get_password() == password:
            self.islocked = False
