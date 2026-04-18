"""
Halit module: representing purity and simplicity.
"""

class Halit:
    def __init__(self, purity=0.99):
        self.purity = purity

    def preserve(self, value):
        return f"{value} is preserved."

    def dissolve(self):
        return "Returning to simplicity."

if __name__ == "__main__":
    h = Halit()
    print(h.preserve("truth"))
