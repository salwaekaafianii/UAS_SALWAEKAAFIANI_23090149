class Restoran:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def display_queue(self):
        if self.queue:
            print('Antrian saat ini:')
            for order in self.queue:
                print('-', order)
        else:
            print('Antrian kosong')

