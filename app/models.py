from app import db
from datetime import datetime, UTC

class Expense(db.Model):
    """
    Represents an expense record in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=lambda: datetime.now(UTC))  # Automatically set to current UTC time
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Expense {self.description}>'

class InsuranceRecord(db.Model):
    """
    Represents an insurance record in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    children = db.Column(db.Integer, nullable=False)
    smoker = db.Column(db.String(3), nullable=False)
    region = db.Column(db.String(20), nullable=False)
    charges = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=lambda: datetime.now(UTC))  # Automatically set to current UTC time

    def __repr__(self):
        return f'<InsuranceRecord {self.id}>'
