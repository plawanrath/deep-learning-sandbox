
import pandas as pd
import os
from sales_analysis import analyze_revenue
def test_analysis():
    # Create dummy data
    df = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-20'],
        'Product': ['A', 'A', 'B', 'B'],
        'Revenue': [100, None, 200, 300] # Missing val should become 100
    })
    df.to_csv('sales.csv', index=False)
    res = analyze_revenue('sales.csv')
    assert res['2023-01'] == 200.0 # 100 + 100(filled)
    assert res['2023-02'] == 500.0
    os.remove('sales.csv')
