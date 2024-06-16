# app/report.py
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import mm
from app.data.boilerplate import company_overview, tool_methodology_and_limitations, contact_table_data

def add_page_number(canvas, doc):
    """
    Add the page number to the footer of the PDF.
    """
    page_number_text = "%d" % (doc.page)
    canvas.drawRightString(200 * mm, 20 * mm, page_number_text)

def generate_pdf_report(output_path, analysis_summary, percent_complete):
    # Create the PDF document
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name='TitleStyle',
        fontSize=18,
        leading=22,
        spaceAfter=14,
        alignment=1  # Center alignment
    )
    section_title_style = styles['Heading2']
    normal_style = styles['BodyText']

    # Add title
    elements.append(Paragraph("Customer Data Completeness Report", title_style))
    elements.append(Spacer(1, 12))

    # Add Management Summary
    elements.append(Paragraph("1. Executive Summary", section_title_style))
    summary_text = f"The percentage of complete records is {percent_complete:.2f}%. This report evaluates the completeness of the customer data based on the specified criteria."
    elements.append(Paragraph(summary_text, normal_style))
    elements.append(Spacer(1, 12))

    # Add Summary Table
    elements.append(Paragraph("Summary of Completeness Criteria", section_title_style))
    table_data = [['Criterion', 'Percent Non-null', 'Number Non-null']]
    for index, row in analysis_summary.iterrows():
        table_data.append([row['Criterion'], f"{row['Percent Non-null']:.2f}%", row['Number Non-null']])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(PageBreak())

    # Add Tool Methodology and Limitations section
    elements.append(Paragraph("2. Tool Methodology and Limitations", section_title_style))
    methodology_text = tool_methodology_and_limitations
    elements.append(Paragraph(methodology_text, normal_style))
    elements.append(PageBreak())

    elements.append(Paragraph("3. Detailed Criterion Analysis", section_title_style))
    for index, row in analysis_summary.iterrows():
        criterion_title = f"{row['Criterion']}"
        criterion_summary = f"Percentage of non-null values: {row['Percent Non-null']:.2f}%<br/>Number of non-null values: {row['Number Non-null']}"
        elements.append(Paragraph(criterion_title, styles['Heading3']))
        elements.append(Paragraph(criterion_summary, normal_style))
        elements.append(Spacer(1, 12))

    # Add Company Overview and Contact Information section
    elements.append(Paragraph("4. Company Overview and Contact Information", section_title_style))
    company_overview_text = company_overview
    elements.append(Paragraph(company_overview_text, normal_style))
    elements.append(Spacer(1, 12))



    table = Table(contact_table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(PageBreak())



    # Build the PDF with page numbers
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)



if __name__=="__main__":
    # Example usage:
    # Assume `result_df` is the DataFrame containing the analysis summary and `percent_complete` is the computed percentage
    output_path = "../customer_data_completeness_report3.pdf"
    import pandas as pd

    # Fake result DataFrame
    data = {
        'Criterion': ['Name', 'Email', 'Phone Number', 'Address', 'Date of Birth', 'Subscription Status'],
        'Percent Non-null': [95.0, 80.0, 60.0, 50.0, 70.0, 90.0],
        'Number Non-null': [950, 800, 600, 500, 700, 900]
    }
    result_df = pd.DataFrame(data)

    # Fake percent complete value
    percent_complete = 75.0
    generate_pdf_report(output_path, result_df, percent_complete)
