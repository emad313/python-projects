from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from utils import paginate

def generate_invoice_pdf(invoice, filename):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(f"Invoice for {invoice.client.name}", styles['Title']))
    story.append(Paragraph(f"Email: {invoice.client.email}", styles['Normal']))
    story.append(Paragraph(f"Date: {invoice.date}, Due: {invoice.due_date}", styles['Normal']))
    story.append(Spacer(1, 12))

    for chunk in paginate(invoice.items):
        for item in chunk:
            line = f"{item.description}: {item.quantity} x ${item.price:.2f} = ${item.quantity * item.price:.2f}"

            story.append(Paragraph(line, styles['Normal']))
        story.append(Spacer(1, 12))

    story.append(Paragraph(f"Total: ${invoice.total:.2f}", styles['Normal']))

    doc.build(story)