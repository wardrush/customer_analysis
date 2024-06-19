# customer_analysis
A UI for customer table analysis
<img width="781" alt="image" src="https://github.com/wardrush/customer_analysis/assets/24572765/85a6f9e3-8314-4efe-9f27-a45ff84f2263">


# Customer Data Analysis Tool

The Customer Analysis Tool helps Private Equity analysts and other organizations assess the completeness of customer data during due diligence. The tool allows users to upload customer data tables in CSV format and analyze them based on user-defined criteria.

## Features

- **CSV Upload**: Upload customer data in CSV format.
- **Data Analysis**: Evaluate the completeness of records based on user-defined criteria.
- **Report Generation**: Generate detailed PDF reports of the analysis.
- **Email Capture**: Capture user email addresses to send analysis reports.

## Future Enhancements

- Integration with CRM systems like Hubspot.
- Support for additional data formats (JSON, API).
- Enhanced analysis metrics and visualizations.

## Getting Started

There are two ways to use this tool. 
1. The main procedure is to use the [hosted version here](https://customeranalysis-wardr.streamlit.app/)
2. If you'd like to host your own version, follow the procedure below. 


### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (`venv` or `virtualenv`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/wardrush/customer_analysis.git
    cd customer_analysis
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
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

2. Open your web browser and navigate to the provided URL (typically `http://localhost:8501`).

3. Upload your CSV file, define the criteria for complete records, and enter your email to receive the analysis report.

## Project Structure

```
project_root/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routes.py
│   ├── models.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── api_service.py
│   │   ├── data_model_validation_service.py
│   │   ├── email_validation_service.py
│   │   ├── phone_validation_service.py
│   │   ├── data_enrichment_service.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_utils.py
│   │   ├── data_transformations.py
│   │   ├── validation_utils.py
│   │
│   ├── templates/
│   │   └── report_template.html
│   │
│   └── static/
│       └── css/
│           └── styles.css
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_services/
│   │   ├── __init__.py
│   │   ├── test_api_service.py
│   │   ├── test_data_model_validation_service.py
│   │   ├── test_email_validation_service.py
│   │   ├── test_phone_validation_service.py
│   │   ├── test_data_enrichment_service.py
│
├── requirements.txt
├── README.md
└── Dockerfile

```

### Detailed Structure

- **app/\_\_init\_\_.py**: Initializes the app module.
- **app/analysis.py**: Functions for reading and analyzing customer data.
- **app/email.py**: Functions for handling email operations.
- **app/models.py**: Defines the `CustomerData` class.
- **app/report.py**: Functions for generating PDF reports.
- **app/utils.py**: Utility functions used across the application.
- **assets/sample_data.csv**: Sample data for testing the application.
- **main.py**: Main entry point for the Streamlit application.

## License

This project is licensed under the MIT License.

---
