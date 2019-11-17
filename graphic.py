import matplotlib.pyplot as plt

class Graphic:
    def drawGraphic(self, happiness, title, quantity):
        i = 0
        values = []
        while i < quantity:
            values.append(i)
            i += 1
        plt.scatter(values, happiness, marker="*")
        plt.title('Marginal utility of ' + title)
        plt.xlabel('quantity')
        plt.ylabel('happiness')
        plt.show()