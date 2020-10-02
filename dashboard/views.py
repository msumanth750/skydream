from django.shortcuts import render

import numpy as np
import random

# Create your views here.
def right_poles(poles):
    rhs_poles =[]
    for p in poles:
        if p.real>0:
            rhs_poles.append(p)
    return rhs_poles

def stability(poles):
    rhs_poles=right_poles(poles)
    if len(rhs_poles)==0:
        return 'Stable'
    else:
        return 'Unstable'


def index(request):
    return render(request,'dashboard/index.html')

def register(request):
    return render(request,'dashboard/register.html')

def login(request):
    return render(request,'dashboard/login.html')

def contact(request):
    return render(request,'dashboard/contact.html')

def about(request):
    return render(request,'dashboard/about.html')

def rootlocus(request):
    gradients = ['warm-flame-gradient','night-fade-gradient',
    'spring-warmth-gradient','rainy-ashville-gradient']
    pole1 =[]
    pole2 =[]
    pole3 =[]
    pole4 =[]
    pole5 =[]
    pole6 =[]
    pole7 =[]
    for k in np.arange(0,30,0.1):
        eqn = [1,6,11,6+2*k]
        roots = np.roots(eqn)
        pole1.append(roots[0])
        pole2.append(roots[1])
        pole3.append(roots[2])

    gradient = random.choice(gradients)
    context = {
    'gradient':gradient,
    "pole1":pole1,
    "pole2":pole2,
    "pole3":pole3,
    }
    return render(request,'dashboard/rootlocus.html',context)


def polezero(request):
    if (request.method == 'POST'):
        print('*'*100)
        num = request.POST.get('num')
        den = request.POST.get('den')
        ntf = [int(a) for a in num.split(" ")]
        dtf = [int(a) for a in den.split(" ")]
        print(ntf,dtf)
        zeros = np.roots(ntf)
        poles = np.roots(dtf)
        rhs_poles = right_poles(poles)
        stable = stability(poles)
        print(zeros,poles)
        result = {
            "num" : ntf,
            "den" : dtf,
            "poles" :poles,
            "zeros": zeros,
            "rhs_poles" : rhs_poles,
            "stable":stable,
        }
        return render(request,'dashboard/polezero.html',result)
    return render(request,'dashboard/polezero.html')

