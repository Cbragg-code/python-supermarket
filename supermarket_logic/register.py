class Register:
    def __init__(self, id):
        self.id = id
        self.queue = []
        self.customers_served = 0
        self.total_sales = 0.0

    def add_customer(self, customer):
        self.queue.append(customer)

    def process_customer(self):
        if self.queue:
            customer = self.queue.pop(0)
            self.customers_served += 1
            self.total_sales += customer.checkout_total()
            print(f"Register {self.id}: Processed {customer}")

    def __repr__(self):
        return (f"Register {self.id}: {self.customers_served} "
                f"customers served, "
                f"Total sales: ${self.total_sales:.2f}")
