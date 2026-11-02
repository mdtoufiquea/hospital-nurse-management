from django.shortcuts import render, redirect, get_object_or_404
from .models import Nurse
from .forms import NurseForm


# Nurse List + Search + Department Filter
def home(request):
    nurses = Nurse.objects.all()

    search_query = request.GET.get('search', '')
    department = request.GET.get('department', '')

    if search_query:
        nurses = nurses.filter(
            name__icontains=search_query
        ) | nurses.filter(
            nurse_id__icontains=search_query
        ) | nurses.filter(
            department__icontains=search_query
        ) | nurses.filter(
            email__icontains=search_query
        )

    if department:
        nurses = nurses.filter(department__iexact=department)

    departments = Nurse.objects.values_list(
        'department', flat=True
    ).distinct().order_by('department')

    context = {
        'nurses': nurses,
        'departments': departments,
        'search_query': search_query,
        'selected_department': department,
    }

    return render(request, 'nurses/home.html', context)


# Add Nurse
def add_nurse(request):
    if request.method == 'POST':
        form = NurseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NurseForm()

    return render(request, 'nurses/nurse_form.html', {
        'form': form,
        'title': 'Add New Nurse',
        'button_text': 'Add Nurse',
    })


# Edit Nurse
def edit_nurse(request, id):
    nurse = get_object_or_404(Nurse, id=id)

    if request.method == 'POST':
        form = NurseForm(
            request.POST,
            request.FILES,
            instance=nurse
        )

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NurseForm(instance=nurse)

    return render(request, 'nurses/nurse_form.html', {
        'form': form,
        'title': 'Edit Nurse',
        'button_text': 'Update Nurse',
    })


# Delete Nurse
def delete_nurse(request, id):
    nurse = get_object_or_404(Nurse, id=id)

    if request.method == 'POST':
        nurse.delete()
        return redirect('home')

    return render(request, 'nurses/delete_confirm.html', {
        'nurse': nurse
    })