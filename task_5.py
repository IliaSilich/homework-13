from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, order):
        pass


class Database(Storage):
    def connect(self):
        print("Connecting to the database")

    def save(self, order):
        print(f"Saving order in the database: {order}")


class File(Storage):
    def save(self, order):
        with open("order.txt", "w") as file:
            file.write(f"Order details: {order}")


class Order:
    def __init__(self, items, total):
        self.items = items
        self.total = total

    def process(self, storage):
        storage.save(self)


order = Order(items=["item1", "item2"], total=100)


database_storage = Database()
order.process(database_storage)


file_storage = File()
order.process(file_storage)
