#app/report/boilerplate.py
# This file holds the boilerplate strings

headers_how_to_use_this_tool ="""
                    **Purpose:**

                    The Completeness Check Tool helps you evaluate the quality of your customer data by analyzing how many records meet specific completeness criteria. This can be invaluable during due diligence or data quality assessments.

                    **How It Works:**

                    Upload your customer CRM dataset and specify the columns that are required for a record to be considered complete (e.g., email and phone).
                        """


headers_how_to_use_this_tool_info="""
                    **Expected Outputs:**

                    1. **Percentage of Complete Records:** The tool calculates the percentage of records that have non-null values for all specified criteria.
                    2. **Summary Table:** The table provides a detailed breakdown of:
                       - Percentage and number of records with non-null values for each individual criterion.
                       - Overall percentage and number of records that meet all the specified criteria.
                """

headers_example_use_cases_and_tips="""
                    **Example Use Case:**

                    Imagine you need to assess the quality of your contact data before merging databases. You want to ensure that each contact has both an email and a phone number. Here's how you would use this tool: Upload your dataset, define your criteria, and run the tool to get the results.

                    **Why Use This Tool?**

                    - **Quick Assessment:** Instantly see the quality of your data based on your defined criteria.
                    - **Informed Decisions:** Use the summary table to understand where your data might be lacking and make informed decisions on data cleaning or enhancement.
                    - **Flexible and Customizable:** Define any number of criteria to suit your specific needs.
                    """

headers_example_use_cases_and_tips_info="""
                **Tips:**

                - **Regular Usage:** Keep this tool handy during data migration, integration projects, or regular data quality checks.
                - **Feedback Welcome:** If you have suggestions for improving this tool, please reach out directly or open an issue on our GitHub page. Your feedback helps keep this tool accurate and useful.
                """


company_overview = """Customer Health Check is dedicated to providing Private Equity firms with precise and actionable insights into the health of customer databases. Our proprietary AI-enabled tool streamlines the due diligence process by identifying the completeness of customer records, ensuring that you have a clear understanding of the customer base before making critical acquisition decisions.
                
                Our mission is to empower your due diligence efforts with reliable data analysis, reducing the risk of post-acquisition surprises and facilitating informed decision-making.
                
                For further information or inquiries, please contact us:
                """

contact_table_data = [
        ['Company Name', 'Customer Health Check'],
        ['Address', '[Placeholder Address]'],
        ['Email', '[Placeholder Email]'],
        ['Phone', '[Placeholder Phone Number]'],
        ['Website', '[Placeholder Website]']
    ]


tool_methodology_and_limitations="""The Customer Health Check tool provides a comprehensive analysis of customer data to determine the completeness and accuracy of records. This tool utilizes a boolean "AND" methodology to identify records that meet specific criteria defined as 'complete'. A complete record typically includes essential data points such as customer name, email address, and phone number. Additional criteria can be specified as needed.
                                    
                                    This tool's analysis is based on the data provided in the uploaded files, and its accuracy is contingent on the quality and comprehensiveness of the uploaded data. While this tool is robust in identifying completeness, it does not verify the validity of the data beyond the specified criteria. Therefore, the findings should be interpreted as an initial assessment rather than a final judgment.
                                    
                                    For a detailed understanding of the tool's codebase and methodology, please refer to the documentation included in the uploaded zip file.
                                    """

common_next_steps="""
                ## Common Next Steps
                
                The output of the Customer Health Check tool represents the first step in understanding the health of the customer database. This initial analysis highlights the completeness of records and identifies potential gaps that need further investigation.
                
                Typically, the next steps involve a manual discovery period conducted by a consultancy to validate and verify the findings. This phase includes in-depth analysis and validation to ensure the accuracy of the customer data and to address any identified issues.
                
                While we offer consultancy services to assist with this manual discovery period, it is not a requirement. Your team can choose to engage our consultancy services for a seamless transition from analysis to action, or you may opt to utilize your internal resources or third-party consultants to complete the due diligence process.
                
                Our goal is to provide you with the tools and insights needed to make informed decisions, ensuring a smooth and successful acquisition process.
                """


