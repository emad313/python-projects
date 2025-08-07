import smtplib
from email.message import EmailMessage

def send_invoice(recipient_email, pdf_path):
    msg = EmailMessage()
    msg['Subject'] = 'Your Invoice'
    msg['From'] = 'no-reply@invoice_system.com'
    msg['To'] = recipient_email
    msg.set_content('Please find attached your invoice.')

    with open(pdf_path, 'rb') as file:
        file_data = file.read()
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename='invoice.pdf')

    try:
        with smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525) as server:
            server.starttls()  # TLS encryption
            server.login('002759d9ba7e99', 'be1dac40ce235a')  # Your Mailtrap credentials
            server.send_message(msg)
        print("✅ Invoice sent successfully to", recipient_email)
    except Exception as e:
        print("❌ Failed to send invoice:", e)