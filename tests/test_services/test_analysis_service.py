import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from app.services.analysis_service import manage_analysis_button

class TestAnalysisService(unittest.TestCase):

    @patch('app.services.analysis_service.st')
    def test_manage_analysis_button(self, mock_streamlit):
        # Mock the button click to always return True
        mock_streamlit.button.return_value = True

        # Create a sample dataframe
        data = {'Name': ['John Doe', 'Jane Doe'], 'Email': ['john@example.com', 'jane@example.com']}
        df = pd.DataFrame(data)

        # Call the function with the mocked button click
        with patch('app.services.analysis_service.analyze_customer_table') as mock_analyze:
            mock_analyze.return_value = {'summary': data, 'percent_complete': 100}
            manage_analysis_button(df=df, criteria_list=['Name', 'Email'])

            # Verify the results are displayed in Streamlit
            self.assertTrue(mock_streamlit.subheader.called)
            self.assertTrue(mock_streamlit.write.called)
            self.assertTrue(mock_streamlit.dataframe.called)

if __name__ == '__main__':
    unittest.main()
