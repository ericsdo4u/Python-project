class Entry:
    def __init__(self, entry_id, title, body):
        self.entry_id = entry_id
        self.title = title
        self.body = body

    def get_entry_id(self):
        return self.entry_id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def update_body(self, body):
        self.body = body

    def update_title(self, title):
        self.title = title
