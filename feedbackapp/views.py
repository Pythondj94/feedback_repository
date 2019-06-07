from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt
date1=dt.datetime.now()

def feedback_view(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedbackData(
                name=name,
                rating=rating,
                date=date1,
                feedback=feedback
            )
            data.save()
            fdata=FeedbackData.objects.all()
            fform=FeedbackForm()
            return render(request,'feedback.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse("User Invalid Data")
    else:
        fform=FeedbackForm()
        fdata=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'fdata':fdata})

