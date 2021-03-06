from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import FormLaporan, FormLaporanTukang
from .decorators import unauthenticated_user, allowed_users

# Create your views here.

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect('home')

		else:
			messages.info(request, 'Username or Password is incorrect')

	context = {}

	return render(request, 'app/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):

	context = {}
	return render(request, 'app/home.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['karyawan'])
def data(request):
   laporan = Laporan.objects.all()

   context = {'laporan':laporan}
   return render(request, 'app/data.html', context)

@login_required(login_url='login')
def status(request):
   laporan = Laporan.objects.all()

   total_laporan = laporan.count()
   selesai = laporan.filter(status='Selesai').count()
   pending = laporan.filter(status='Pending').count()
   penanganan = laporan.filter(status='Penanganan').count()

   barat = laporan.filter(zona='Barat').count()
   utara = laporan.filter(zona='Utara').count()
   timur = laporan.filter(zona='Timur').count()
   selatan = laporan.filter(zona='Selatan').count()

   context = {'laporan':laporan, 'total_laporan':total_laporan, 'selesai':selesai, 'pending':pending, 'penanganan':penanganan, 'barat':barat, 'utara':utara, 'timur':timur, 'selatan':selatan}
   return render(request, 'app/status.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['karyawan'])
def create(request):
	form = FormLaporan()
	if request.method == 'POST':
		form = FormLaporan(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/data/')


	context = {'form':form}
	return render(request, 'app/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['tukang'])
def dataTukang(request):
   laporan = Laporan.objects.all()

   context = {'laporan':laporan}
   return render(request, 'app/data_tukang.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['karyawan'])
def update(request, pk):

	laporan = Laporan.objects.get(spk=pk)
	form = FormLaporan(instance=laporan)

	if request.method == 'POST':
		form = FormLaporan(request.POST, instance=laporan)
		if form.is_valid():
			form.save()
			return redirect('/data/')

	context = {'form':form}
	return render(request, 'app/form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['karyawan'])
def delete(request, pk):
	laporan = Laporan.objects.get(spk=pk)

	if request.method == "POST":
		laporan.delete()
		return redirect('/data/')

	context = {'item':laporan}
	return render(request, 'app/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['tukang'])
def update_status(request, pk):

	laporan = Laporan.objects.get(spk=pk)
	form = FormLaporanTukang(instance=laporan)

	if request.method == 'POST':
		form = FormLaporanTukang(request.POST, instance=laporan)
		if form.is_valid():
			form.save()
			return redirect('/dataTukang/')

	context = {'form':form, 'item':laporan}
	return render(request, 'app/update_status.html', context)