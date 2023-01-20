from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Company


# Create your views here.

def fun(request):
    xaxis = request.POST.get('xValues','sector')
    yaxis = request.POST.get('yValues','end_year')
    chartname = request.POST.get('chartname','line')

    data = Company.objects.values(xaxis)[0:]
    li=[]
    xaxislist=[]
    # Filter data of X-axis values
    for i in data:
        if i not in li:
            li.append(i)

    # Dict to list convertion and removing null values
    for i in li:
        a=i.get(xaxis)
        if a!='':
            xaxislist.append(a)

    # # Logic for Y-axis
    yaxisvalues =[]
    withnullvalues =[]

    for item in xaxislist:
        # X_axis values
        # 1
        if xaxis=="sector":
            d = Company.objects.filter(sector=item)
        # 2
        elif xaxis=="topic":
            d = Company.objects.filter(topic=item)
        # 3
        elif xaxis=="region":
            d = Company.objects.filter(region=item)
        # 4
        elif xaxis=="source":
            d = Company.objects.filter(source=item)   
        # 5 
        elif xaxis=="end_year":
            d = Company.objects.filter(end_year=item) 
        # 6   
        elif xaxis=="start_year":
            d = Company.objects.filter(start_year=item)   
        # 7 
        elif xaxis=="intensity":
            d = Company.objects.filter(intensity=item)  
        # 8  
        elif xaxis=="country":
            d = Company.objects.filter(country=item) 
        # 9   
        elif xaxis=="relevance":
            d = Company.objects.filter(relevance=item) 
        # 10   
        elif xaxis=="pestle":
            d = Company.objects.filter(pestle=item)
        # 11    
        elif xaxis=="likelihood":
            d = Company.objects.filter(likelihood=item)    
        withnullvalues.append(len(d))

        # Y_axis values
        # 1
        if yaxis=="sector":
            null_exclude=d.exclude(sector="")
            yaxisvalues.append(len(null_exclude))
        # 2
        elif yaxis=="topic":
            null_exclude=d.exclude(topic="")
            yaxisvalues.append(len(null_exclude))
        # 3
        elif yaxis=="source":
            null_exclude=d.exclude(source="")
            yaxisvalues.append(len(null_exclude))
        # 4
        elif yaxis=="region":
            null_exclude=d.exclude(region="")
            yaxisvalues.append(len(null_exclude))
        # 5
        elif yaxis=="likelihood":
            null_exclude=d.exclude(likelihood=0)
            yaxisvalues.append(len(null_exclude))
        # 6
        elif yaxis=="pestle":
            null_exclude=d.exclude(pestle="")
            yaxisvalues.append(len(null_exclude))
        # 7
        elif yaxis=="relevance":
            null_exclude=d.exclude(relevance=0)
            yaxisvalues.append(len(null_exclude))
        # 8
        elif yaxis=="country":
            null_exclude=d.exclude(country="")
            yaxisvalues.append(len(null_exclude))
        # 9
        elif yaxis=="intensity":
            null_exclude=d.exclude(intensity=0)
            yaxisvalues.append(len(null_exclude))

    thank = False
    parmas = {
        "xaxis": xaxislist,
        'yaxis':yaxisvalues,
        'chartname' : chartname,
        'withnullvalue':withnullvalues,
        'xfield' : xaxis,
        'yfield' : yaxis,
        'thank' : thank
    }
    return render(request,'index.html',parmas)
