class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]  # Store cumulative products, starting with 1

    def add(self, num: int) -> None:

        if num == 0:
            self.prefix = [1]  # Reset because products cannot cross zero

        else:
            self.prefix.append(self.prefix[-1] * num)  # Multiply with previous prefix product

    def getProduct(self, k: int) -> int:

        if k >= len(self.prefix):
            return 0  # A zero exists within the last k numbers

        return self.prefix[-1] // self.prefix[-k - 1]  # Calculate product of last k numbers