class SharedMemory:
    def __init__(self):
        self.store = {}

    def add_memory(self, user_id, content):
        if user_id not in self.store:
            self.store[user_id] = []
        self.store[user_id].append(content)

    def get_history(self, user_id):
        return self.store.get(user_id, [])