from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import FormLaporan

# Create your views here.
def login(request):
   return render(request, 'app/login.html')

def home(request):
   return render(request, 'app/home.html')

def data(request):
   laporan = Laporan.objects.all()

   context = {'laporan':laporan}
   return render(request, 'app/data.html', context)

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

def create(request):
	form = FormLaporan()
	if request.method == 'POST':
		form = FormLaporan(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/data/')


	context = {'form':form}
	return render(request, 'app/form.html', context)

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

def delete(request, pk):
	laporan = Laporan.objects.get(spk=pk)

	if request.method == "POST":
		laporan.delete()
		return redirect('/data/')

	context = {'item':laporan}
	return render(request, 'app/delete.html', context)