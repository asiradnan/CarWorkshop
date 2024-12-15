from django.shortcuts import render
from .forms import AppointmentForm, MechanicsForm
from .models import Mechanics, Appointments
from django.contrib import messages
from django.http import HttpResponseRedirect

def client(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            if len(x.customer_phone)<11 or len(x.customer_phone)>11:
                messages.error(request, 'Phone number must be 11 digits!')
                return render(request, 'client.html', {'form': form})
            for i in x.customer_phone:
                if i not in '0123456789':
                    messages.error(request, 'Phone number must contain only digits!')
                    return render(request, 'client.html', {'form': form})
            for i in x.car_regi_num:
                if i not in '0123456789':
                    messages.error(request, 'Registration number must contain only digits!')
                    return render(request, 'client.html', {'form': form})
            if Appointments.objects.filter(customer_phone=x.customer_phone, date=x.date).exists():
                messages.error(request, 'Appointment already booked for this date!')
                return render(request, 'client.html', {'form': form})
            if Appointments.objects.filter(mechanic = x.mechanic, date=x.date).count() >= 4:
                messages.error(request, 'Mechanic already booked for this date!')
                return render(request, 'client.html', {'form': form})
            x.save()
            messages.success(request, 'Appointment booked successfully!')
            return HttpResponseRedirect('/')
    else:
        form = AppointmentForm()
    return render(request, 'client.html', {'form': form})

def admin(request):
    appoints = Appointments.objects.all()
    if request.method == 'POST':
        form = MechanicsForm(request.POST)
        if form.is_valid():
            form.save()
            mechanics = Mechanics.objects.all()
            messages.success(request, 'Mechanic added successfully!')
    else:
        mechanics = Mechanics.objects.all()
        form = MechanicsForm()
    return render(request, 'admin.html', {'form': form, 'mechanics': mechanics, 'appointments': appoints})

def edit(request,id):
    appointment = Appointments.objects.get(id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            x = form.save(commit=False)
            if Appointments.objects.filter(mechanic = x.mechanic, date=x.date).count() >= 4:
                messages.error(request, 'Mechanic already booked for this date!')
                return render(request, 'edit.html', {'form': form, 'appointment': appointment})
            messages.success(request, 'Appointment updated successfully!')
            return HttpResponseRedirect('/admin')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'edit.html', {'form': form, 'appointment': appointment})

def mechanic_slot(request):
    if request.method == 'POST':
        mechanic = request.POST.get('mechanic')
        date = request.POST.get('date')
        appointments = Appointments.objects.filter(mechanic=mechanic, date=date)
        mechanic = Mechanics.objects.get(id=mechanic)
        return render(request, 'mechanic_slot.html', {'appointments': appointments, 'mechanic': mechanic, 'date': date, 'count': 4-appointments.count()})
    else:
        return HttpResponseRedirect('/admin')