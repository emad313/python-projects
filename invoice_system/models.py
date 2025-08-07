class Client:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class InvoiceItem:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price

class Invoice:
    def __init__(self, client, items, date, due_date):
        self.client = client
        self.items = items
        self.date = date
        self.due_date = due_date
        self.total = sum(item.quantity * item.price for item in items)
