import json
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from analysis.MyAnalysis import MyAnalysis


def home(request):
    data = [];
    for i in range(1, 100):
        person = {};
        person['name'] = 'james' + str(i);
        person['position'] = 'position' + str(i);
        person['office'] = 'office' + str(i);
        person['age'] = i;
        person['salary'] = i * 100;
        dd = time.time();
        person['date'] = time.ctime(dd);
        data.append(person);
    context = {
        'section':'main_section.html',
        'persons':data
    };
    return render(request, 'index.html', context)

def dashboard1(request):
    context = {
        'section':'dashboard1.html',
    };
    return render(request, 'index.html', context);

def dashboard2(request):
    context = {
        'section':'dashboard2.html',
    };
    return render(request, 'index.html', context);

def dashboard3(request):
    context = {
        'section':'dashboard3.html',
    };
    return render(request, 'index.html', context);

def babydashboard(request):
    context = {
        'section':'babydashboard.html',
    };
    return render(request, 'index.html', context);

def dashboard5(request):
    context = {
        'section':'dashboard5.html',
    };
    return render(request, 'index.html', context);

def dashboard6(request):
    context = {
        'section':'dashboard6.html',
    };
    return render(request, 'index.html', context);


def tabledata(request):
    print('tabledata')
    data = [];
    for i in range(1,100):
        person = {};
        person['name'] = 'james'+str(i);
        person['position'] = 'position' + str(i);
        person['office'] = 'office' + str(i);
        person['age'] = i;
        person['salary'] = i*100;
        dd = time.time();
        person['date'] = time.ctime(dd);
        data.append(person);
    print(data);
    return HttpResponse(json.dumps(data),content_type='application/json');


def chart1(request):
    print('tabledata')
    data = [{
                'name': 'Tokyo',
                'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 23.3, 18.3, 13.9, 9.6]
            }, {
                'name': 'London',
                'data': [4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
            }];
    return HttpResponse(json.dumps(data),content_type='application/json');

def chart2(request):
    data2 = [{
                    'name': 'Spain',
                    'y': 505370,
                    'z': 92.9
                }, {
                    'name': 'France',
                    'y': 551500,
                    'z': 118.7
                }, {
                    'name': 'Poland',
                    'y': 312685,
                    'z': 124.6
                }, {
                    'name': 'Czech Republic',
                    'y': 78867,
                    'z': 137.5
                }, {
                    'name': 'Italy',
                    'y': 301340,
                    'z': 201.8
                }, {
                    'name': 'Switzerland',
                    'y': 41277,
                    'z': 214.5
                }, {
                    'name': 'Germany',
                    'y': 357022,
                    'z': 235.6
                }]
    print(data2)
    return HttpResponse(json.dumps(data2),content_type='application/json');


def chart_baby(request):
    data = MyAnalysis().baby();
    print(data);
    return HttpResponse(json.dumps(data), content_type='application/json');

def pop_increase(request):
    data = MyAnalysis().pop3year();
    return HttpResponse(json.dumps(data), content_type='application/json');
