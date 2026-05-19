from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.cell(200, 10, text="Hello World", new_x="LMARGIN", new_y="NEXT", align='C')
out = pdf.output()
with open("test.pdf", "wb") as f:
    f.write(out)
print(type(out))
