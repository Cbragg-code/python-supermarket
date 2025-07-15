from supermarket_logic.supermarket import Supermarket


def run_terminal_simulation():
    print("Starting Supermarket Terminal Simulation...")
    num_registers = 3
    num_customers = 15

    market = Supermarket(num_registers)
    market.simulate(num_customers)
    print("\nSimulation Complete. Final Statistics:")
    market.show_statistics()


if __name__ == "__main__":
    run_terminal_simulation()
