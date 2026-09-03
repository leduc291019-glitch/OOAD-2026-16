class ThuNgan:
    def __init__(self, name):
        self.name = name

    def process_payment(self, amount):
        print(f"{self.name} is processing a payment of {amount}.")

    def generate_receipt(self, amount):
        print(f"Receipt: {self.name} has processed a payment of {amount}.")