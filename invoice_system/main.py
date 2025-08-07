from models import Client, Invoice, InvoiceItem
from invoice_generator import generate_invoice_pdf
from emailer import send_invoice
from db import init_db
from auth import require_auth
import datetime

init_db()

@require_auth
def create_invoice():
    name = input("Enter client name: ")
    email = input("Enter client email: ")
    address = input("Enter client address: ")
    client = Client(name, email, address)

    items = []
    while True:
        description = input("Enter item description (or 'done' to finish): ")
        quantity = input("Enter item quantity: ")
        price = input("Enter item price: ")
        items.append(InvoiceItem(description, int(quantity), float(price)))
        more = input("Add another item? (yes/no): ")
        if more.lower() != 'yes':
            break
    
    today = datetime.date.today()
    due = today + datetime.timedelta(days=14)
    invoice = Invoice(client, items, str(today), str(due))

    filename = f"invoice_{name}_{today}.pdf"

    generate_invoice_pdf(invoice, filename)
    send_invoice(email, filename)
    print(f"Invoice created and sent to {email} as {filename}")

def main():
    print("Welcome to the Invoice System")
    create_invoice()

if __name__ == "__main__":
    main()