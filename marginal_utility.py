import graphic

class Prompt:
    product = ""
    quantity = 0
    happiness = []

    def basics(self):
        self.product = input("Please enter a product.\n")
        self.quantity = int(input("Please enter a maximum quantity.\n"))

    def defineMarginalUtility(self):
        i = 1
        while i <= self.quantity:
            self.happiness.append(input(f"For {i} {self.product} what added happiness do you get?\n"))
            i += 1

prompt = Prompt()
prompt.basics()
prompt.defineMarginalUtility()
graphic = graphic.Graphic()
graphic.drawGraphic(prompt.happiness, prompt.product, prompt.quantity)