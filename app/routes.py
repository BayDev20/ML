from flask import Blueprint, render_template, request, redirect, url_for
from app.models import InsuranceRecord
from app import db
from app.ml_model import predict_charges
from sqlalchemy import func
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Route for the home page. Displays all insurance records.
    """
    records = InsuranceRecord.query.all()
    return render_template('index.html', records=records)

@main.route('/add', methods=['GET', 'POST'])
def add_record():
    """
    Route for adding a new insurance record. Handles both GET (display form) and POST (process form) requests.
    """
    if request.method == 'POST':
        new_record = InsuranceRecord(
            age=request.form['age'],
            sex=request.form['sex'],
            bmi=request.form['bmi'],
            children=request.form['children'],
            smoker=request.form['smoker'],
            region=request.form['region'],
            charges=request.form['charges']
        )
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_record.html')

@main.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    Route for predicting insurance charges. Handles both GET (display form) and POST (process form) requests.
    """
    if request.method == 'POST':
        predicted_charge = predict_charges(
            int(request.form['age']),
            request.form['sex'],
            float(request.form['bmi']),
            int(request.form['children']),
            request.form['smoker'],
            request.form['region']
        )
        return render_template('predict.html', prediction=predicted_charge)
    return render_template('predict.html')

@main.route('/insights')
def insights():
    """
    Route for displaying insights from the insurance data.
    """
    # Calculate total records, average charge, and maximum charge
    total_records = InsuranceRecord.query.count()
    avg_charge = db.session.query(func.avg(InsuranceRecord.charges)).scalar()
    max_charge = db.session.query(func.max(InsuranceRecord.charges)).scalar()
    
    # Calculate average charges for smokers and non-smokers
    smoker_avg = db.session.query(func.avg(InsuranceRecord.charges)).filter(InsuranceRecord.smoker == 'yes').scalar()
    non_smoker_avg = db.session.query(func.avg(InsuranceRecord.charges)).filter(InsuranceRecord.smoker == 'no').scalar()
    
    # Calculate age distribution
    age_distribution = db.session.query(
        func.floor(InsuranceRecord.age / 10) * 10,
        func.count(InsuranceRecord.id)
    ).group_by(func.floor(InsuranceRecord.age / 10)).all()
    age_distribution = {f"{age}-{age+9}": count for age, count in age_distribution}
    
    # Get BMI vs Charges data for scatter plot
    bmi_charges_data = [{'x': row.bmi, 'y': row.charges} for row in db.session.query(InsuranceRecord.bmi, InsuranceRecord.charges).all()]

    return render_template('insights.html', 
                           total_records=total_records,
                           avg_charge=avg_charge,
                           max_charge=max_charge,
                           smoker_avg=smoker_avg,
                           non_smoker_avg=non_smoker_avg,
                           age_distribution=age_distribution,
                           bmi_charges_data=json.dumps(bmi_charges_data))
