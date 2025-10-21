from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("Analytical_Mechanics.pdf")
writer = PdfWriter()

for page_num in range(229, 285):
    writer.add_page(reader.pages[page_num])

with open("6단원.pdf", "wb") as output_file:
    writer.write(output_file)