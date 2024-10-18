import pandas as pd
from app.models import Expense

def get_expense_dataframe():
    expenses = Expense.query.all()
    return pd.DataFrame([(e.date, e.amount, e.description, e.category) for e in expenses],
                        columns=['date', 'amount', 'description', 'category'])

def calculate_insights(df):
    insights = {
        'total_spent': df['amount'].sum(),
        'average_expense': df['amount'].mean(),
        'top_categories': df.groupby('category')['amount'].sum().sort_values(ascending=False).head(5).to_dict(),
        'monthly_trend': df.groupby(df['date'].dt.to_period('M'))['amount'].sum().to_dict()
    }
    return insights


