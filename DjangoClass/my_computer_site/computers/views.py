from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.

def computer_info(request):

    if request.POST:
        form = ReviewForm(request.POST)

        if form.is_valid():

            form.save()
            print(form.cleaned_data)
            return redirect(reverse('computers:thank_you'))
    else:
        form = ReviewForm()

    return render(request, 'computers/computerinfo.html',context={'form': form})

def thank_you(request):

    return render(request, 'computers/thank_you.html')

