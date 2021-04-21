from django.forms import ModelForm
from django import forms
from .models import Laporan

class FormLaporan(ModelForm):
    class Meta:
        model = Laporan
        fields = ['spk', 'zona', 'nama', 'alamat', 'tanggal', 'gangguan', 'jenis', 'status']
        widgets = {
            'spk' : forms.NumberInput(attrs={'class':'form-control'}),
            'zona' : forms.Select(attrs={'class':'form-control'}),
            'nama' : forms.TextInput(attrs={'class':'form-control'}),
            'alamat' : forms.TextInput(attrs={'class':'form-control'}),
            'tanggal' : forms.DateInput(attrs={'class':'form-control'}),
            'gangguan' : forms.TextInput(attrs={'class':'form-control'}),
            'jenis' : forms.Select(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
        } 
