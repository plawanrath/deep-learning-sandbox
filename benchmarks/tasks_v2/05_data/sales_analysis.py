
import pandas as pd
def analyze_revenue(csv_path):
    # 1. Load CSV (Date, Product, Revenue)
    # 2. Fill missing Revenue with Product mean
    # 3. Aggregate total Revenue by Month
    # Return pd.Series (Index=MonthStr, Value=Sum)
    df = pd.read_csv(csv_path)

    # Ensure dates are datetime for reliable month extraction
    df['Date'] = pd.to_datetime(df['Date'])

    # Fill missing revenue values with the mean revenue for each product
    df['Revenue'] = df['Revenue'].fillna(df.groupby('Product')['Revenue'].transform('mean'))

    # Aggregate revenue by month (YYYY-MM)
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    monthly_revenue = df.groupby('Month')['Revenue'].sum()

    return monthly_revenue
