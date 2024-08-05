from django.shortcuts import render
from django.http import JsonResponse
from .models import Company  # Adjust according to your model
import json

def index(request):
    return render(request, 'dataVisualization/index.html')

def chart(request):
    if request.method == 'POST':
        x_value = request.POST.get('xValues')
        y_value = request.POST.get('yValues')
        
        # Process data based on selected xValue and yValue
        # Example: Fetch data from the database
        data = Company.objects.values_list(x_value, y_value).distinct()
        
        # Convert data to format suitable for chart.js
        x_labels = [item[0] for item in data]
        y_values = [item[1] for item in data]
        
        context = {
            'xaxis': json.dumps(x_labels),
            'yaxis': json.dumps(y_values),
            'chartname': 'bar',  # Default chart type
            'xfield': x_value,
            'yfield': y_value
        }
        return render(request, 'dataVisualization/chart.html', context)
    
    # Default context in case of GET request
    context = {
        'xaxis': json.dumps([]),
        'yaxis': json.dumps([]),
        'chartname': 'bar',
        'xfield': '',
        'yfield': ''
    }
    return render(request, 'dataVisualization/chart.html', context)