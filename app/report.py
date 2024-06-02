# app/report.py
from fpdf import FPDF

def generate_report(complete_records, incomplete_records, email):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Customer Data Analysis Report", ln=True, align='C')
    
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True, align='L')
    
    pdf.cell(200, 10, txt=f"Complete Records: {len(complete_records)}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Incomplete Records: {len(incomplete_records)}", ln=True, align='L')
    
    pdf.output(f"{email}_report.pdf")
