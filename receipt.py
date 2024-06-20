from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


def make_receipt(data, out_file_name):
    pdf = SimpleDocTemplate(out_file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1
    title = Paragraph("Dessert Shop Receipt", title_style)

    style = TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ])

    table = Table(data, style=style)
    pdf.build([title, table])


def main():
    DATA = [
        ["Name", "Item Cost", "Tax"],
        ["Candy Corn", "$0.38", "$0.03"],
        ["Gummy Bears", "$0.09", "$0.01"],
        ["Chocolate Chip", "$2.00", "$0.14"],
        ["Pistachio", "$1.58", "$0.11"],
        ["Vanilla", "$3.36", "$0.24"],
        ["Oatmeal Raisin", "$0.57", "$0.04"],
        ["--------------------------------------------------------"],
        ["Order Subtotals", "$7.97", "$0.58"],
        ["Order Total", "", "$8.55"],
        ["Total items in the order", "", "6"]
    ]
    make_receipt(DATA, "receipt.pdf")


if __name__ == "__main__":
    main()
