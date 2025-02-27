import random


class Article:
    def __init__(self, name, category):
        self.name = name
        self.category = category

        self.price = None

    def setPrice(self, price):
        self.price = price


class Supermarket:
    def __init__(self, supermarket_name):
        self.supermarket_name = supermarket_name

        self.articles = {}

    def addArticle(self, article, quantity):
        self.articles[article] = quantity

    def discountAktion(self, discount, category):
        for article in self.articles.keys():
            if article.category == category:
                article.price = article.price * (1-discount)

    def __str__(self):
        article_list = [f"{article.name} ({article.category}) - ${article.price:.2f}, Quantity: {quantity}"
                        for article, quantity in self.articles.items()]
        return f"Supermarket: {self.supermarket_name}\nArticles:\n" + "\n".join(article_list)


a1 = Article("Fresh Soap 200g", "hygiene")
a2 = Article("Rose Shampoo 200 ml", "hygiene")
a3 = Article("Coal Toothpaste 50g", "hygiene")
a4 = Article("Mango 1 Pc", "fruits")
a5 = Article("Orange 1 Kg", "fruits")
a6 = Article("Apple 1 Kg", "fruits")

mk = Supermarket("Happymarket")

for a in (a1, a2, a3, a4, a5, a6):
    a.setPrice(random.randint(1, 320))
    mk.addArticle(a, random.randint(1, 40))

print(mk)  # prints all items in supermarket

mk.discountAktion(0.25, "fruits")  # 25% discount on fruits

print(mk)  # prints all items in supermarket