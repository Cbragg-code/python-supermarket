from supermarket_logic.customer import Customer
from supermarket_logic.register import Register


class Supermarket:
    def __init__(self, num_registers):
        self.registers = [Register(i + 1) for i in range(num_registers)]

    def simulate(self, num_customers):
        customers = [Customer() for _ in range(num_customers)]

        for customer in customers:
            shortest_queue = min(self.registers, key=lambda r: len(r.queue))
            shortest_queue.add_customer(customer)

        for _ in range(max(len(r.queue) for r in self.registers)):
            for register in self.registers:
                register.process_customer()

    def show_statistics(self):
        for register in self.registers:
            print(register)
