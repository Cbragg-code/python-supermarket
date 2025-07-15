import tkinter as tk
from supermarket_logic.supermarket import Supermarket
from supermarket_logic.customer import Customer


class SupermarketGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Simulator (Animated)")

        self.title_label = tk.Label(root, text="Supermarket Simulator", 
                                    font=("Arial", 20))
        self.title_label.pack(pady=10)

        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        tk.Label(control_frame, 
                 text="Number of Registers:").grid(row=0, column=0)
        self.registers_entry = tk.Entry(control_frame)
        self.registers_entry.insert(0, "3")
        self.registers_entry.grid(row=0, column=1)

        tk.Label(control_frame, 
                 text="Number of Customers:").grid(row=1, column=0)
        self.customers_entry = tk.Entry(control_frame)
        self.customers_entry.insert(0, "15")
        self.customers_entry.grid(row=1, column=1)

        self.start_button = tk.Button(control_frame, 
                                      text="Start Simulation", 
                                      command=self.run_simulation)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Visual frame for registers
        self.visual_frame = tk.Frame(root)
        self.visual_frame.pack(pady=10)

        self.stats_label = tk.Label(root, text="", font=("Arial", 12))
        self.stats_label.pack(pady=10)

    def clear_visuals(self):
        for widget in self.visual_frame.winfo_children():
            widget.destroy()

    def setup_register_visuals(self, num_registers):
        self.register_frames = []
        for i in range(num_registers):
            frame = tk.Frame(self.visual_frame, bd=2, relief=tk.SUNKEN)
            frame.pack(side=tk.LEFT, padx=10)
            label = tk.Label(frame, text=f"Register {i+1}", font=("Arial", 14))
            label.pack()
            queue_frame = tk.Frame(frame)
            queue_frame.pack()
            self.register_frames.append((frame, queue_frame))

    def update_visuals(self, register_queues):
        for idx, (_, queue_frame) in enumerate(self.register_frames):
            for widget in queue_frame.winfo_children():
                widget.destroy()
            for customer in register_queues[idx]:
                customer_label = tk.Label(queue_frame,
                                          text=f"C{customer.id}",
                                          bg="lightblue", width=5)
                customer_label.pack(pady=2)

    def run_simulation(self):
        try:
            num_registers = int(self.registers_entry.get())
            num_customers = int(self.customers_entry.get())
        except ValueError:
            return

        self.clear_visuals()
        self.setup_register_visuals(num_registers)

        self.market = Supermarket(num_registers)
        customers = [Customer() for _ in range(num_customers)]

        for customer in customers:
            shortest = min(self.market.registers, key=lambda r: len(r.queue))
            shortest.add_customer(customer)
            self.update_visuals([r.queue for r in self.market.registers])
            self.root.update()
            self.root.after(300)

        # Processing customers visually
        max_queue = max(len(r.queue) for r in self.market.registers)
        for _ in range(max_queue):
            for r in self.market.registers:
                if r.queue:
                    r.process_customer()
            self.update_visuals([r.queue for r in self.market.registers])
            self.root.update()
            self.root.after(500)

        stats = "\nFinal Statistics:\n"
        for register in self.market.registers:
            stats += (f"Register {register.id}: {register.customers_served} "
                      f"served, ${register.total_sales:.2f} total sales\n")
        self.stats_label.config(text=stats)


if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketGUI(root)
    root.mainloop()
