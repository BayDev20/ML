from setuptools import setup, find_packages

setup(
    name="insurance_predictor",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "Flask-SQLAlchemy",
        "scikit-learn",
        "pandas",
        "numpy",
        # Add any other dependencies
    ],
    entry_points={
        'console_scripts': [
            'run_insurance_predictor=run:main',
        ],
    },
)
