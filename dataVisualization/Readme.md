# Data Visualization Project

## Overview
This Django web application provides an interactive platform for visualizing data through various types of charts. Users can select different data fields to generate and view charts using Chart.js.

## Features
- Interactive chart generation (bar, line, pie)
- Dynamic data selection through forms
- Responsive design using Bootstrap
- Data management via Django's admin interface

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/datavisualization.git
   cd datavisualization

   python -m venv venv
source venv/bin/activate 

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
