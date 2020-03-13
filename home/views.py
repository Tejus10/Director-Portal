from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import internal_letter,external_letter,external_past,internal_past
from .forms import *
from datetime import datetime

@login_required
def home(request):
	context = {
               'external_letters':external_letter.objects.all().order_by('si_no'),
               'internal_letters':internal_letter.objects.all().order_by('si_no'),
               'title':'Home'
               }
	return render(request,'home/home.html',context )

@login_required
def internal_creation_form(request):
    form = Internal_creation_form(request.POST or None)
    if form.is_valid():
        letter = form.save()
        if request.POST['referred_to']:
            u = User.objects.get(pk=request.POST['referred_to'])
            internal_past.objects.create(comment=str(request.POST['remarks']), fro=str(request.user.username), to=str(u.username), dated=datetime.date(datetime.now()), file=letter)
        return redirect('home')

    context = {
        'form' : form,
        'title':'New File'
    }
    return render(request,'home/internal_form.html',context)

@login_required
def external_creation_form(request):
    form = External_creation_form(request.POST or None)
    if form.is_valid():
        letter = form.save()
        if request.POST['referred_to']:
            u = User.objects.get(pk=request.POST['referred_to'])
            external_past.objects.create(comment=str(request.POST['remarks']), fro=str(request.user.username), to=str(u.username), dated=datetime.date(datetime.now()), file=letter)
        return redirect('home')

    context = {
        'form' : form,
        'title':'New File'
    }
    return render(request,'home/external_form.html',context)	

@login_required
def edit_external(request,letter_id):
    if request.method == 'POST':

        letter = external_letter.objects.get(pk=letter_id) 
        form = External_creation_form(request.POST or None,instance=letter)
        if(form.is_valid()):            
            form.save()
            # messages.success(request,"Item has been Edited!")
            if request.POST['referred_to']:
                u = User.objects.get(pk=request.POST['referred_to'])
                external_past.objects.create(comment=str(request.POST['remarks']), fro=str(request.user.username), to=str(u.username), dated=datetime.date(datetime.now()), file=letter)
            return redirect('home')
    else:        
        letter = external_letter.objects.get(pk=letter_id) 
        form = External_creation_form(instance=letter)
        return render(request,'home/edit_external.html',{'form':form, 'title':'Edit'})

@login_required
def edit_internal(request,letter_id):
    if request.method == 'POST':

        letter = internal_letter.objects.get(pk=letter_id) 
        form = Internal_creation_form(request.POST or None,instance=letter)
        if(form.is_valid()):            
            form.save()
            # messages.success(request,"Item has been Edited!")
            if request.POST['referred_to']:
                u = User.objects.get(pk=request.POST['referred_to'])
                internal_past.objects.create(comment=str(request.POST['remarks']), fro=str(request.user.username), to=str(u.username), dated=datetime.date(datetime.now()), file=letter)
            return redirect('home')
    else:        
        letter = internal_letter.objects.get(pk=letter_id) 
        form = Internal_creation_form(instance=letter)
        return render(request,'home/edit_internal.html',{'form':form, 'title':'Edit'})    


@login_required
def files_referred(request):
    user = request.user
    efile = external_letter.objects.filter(referred_to = user)
    ifile = internal_letter.objects.filter(referred_to = user)
    context = {
    'efile' : efile,
    'ifile' : ifile,
    'title':'My Files'
    }

    return render(request,'home/myfiles.html',context)


@login_required
def detail_internal(request,letter_id):
    letter = internal_letter.objects.get(pk=letter_id)
    out = letter.internal_past_set.all().order_by('-dated')
    out = out.order_by('-time')
    context = {
    'out' : out,
    'title':'File Details'
    }
    return render(request,'home/detail.html', context)


@login_required
def detail_external(request,letter_id):
    letter = external_letter.objects.get(pk=letter_id)
    out = letter.external_past_set.all().order_by('-dated')
    out = out.order_by('-time')
    context = {
    'out' : out,
    'title':'File Details'
    }
    return render(request,'home/detail.html', context)    