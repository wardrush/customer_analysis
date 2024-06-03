# customer_analysis
A UI for customer table analysis

# Customer Data Analysis Tool

## Overview

The Customer Data Analysis Tool allows users to upload customer data tables in CSV format and analyze the data to estimate the number of 'complete records.' This tool is primarily designed for Private Equity analysts performing due diligence, but it can be used by any organization that needs to analyze customer data quality.

## Features

1. **CSV Upload**: Users can upload customer data in CSV format. NOTE: Currently must be true CSV with UTF-8 Encoding
2. **Records Analysis**: Analyzes the uploaded data based on user-defined criteria for 'complete records.'
3. **Report Generation**: Generates a detailed PDF report of the analysis results.
4. **Email Capture**: Captures the user's email address to send the report.

## Future Enhancements

- Integration with Hubspot and other CRM systems.
- Enhanced data upload options (e.g., JSON, direct API integration).
- Additional analysis metrics and visualizations.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer-data-analysis.git
   cd customer-data-analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`).

3. Upload your CSV file, specify the criteria for complete records, and enter your email to receive the analysis report.

## Project Structure

```
customer_analysis/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── analysis.py
│   ├── report.py
│   └── email.py
│
├── main.py
├── requirements.txt
└── README.md
```

### app/models.py

Defines the `CustomerData` class, which represents the customer data model.

### app/analysis.py

Contains functions for reading CSV files and analyzing customer data based on specified criteria.

### app/report.py

Contains functions for generating PDF reports based on the analysis results.

### main.py

The main entry point for the Streamlit application, tying together file upload, data analysis, and report generation.



## License

This project is licensed under the MIT License.
