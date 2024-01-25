class Hero_inventory():
    def __init__(self):
        self.items = []

    def add_times(self, item):
        self.items.append(item)

    def remove_items(self, item):
        if item in self.items:
            self.items.remove(item)