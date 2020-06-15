from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import VoltageClass, CommutationJournal, NameOfSubstation, NameOfBranch, CircuitBreakers, SwitchType
from .forms import JurForm
from .calculation import vedenie_arhiva

def index(request):
    journal = CommutationJournal.objects.all()
    substations = NameOfSubstation.objects.all()
    branchs = NameOfBranch.objects.all()
    return render(request, 'accounting/index.html', {'commutation_journal': journal, 'substations': substations, 'branchs': branchs, 'title':'Комутационный журнал'})


def substation_jur(request, name_of_substation_id ):
      journal = CommutationJournal.objects.filter(name_of_substation_id=name_of_substation_id)
      v = NameOfSubstation.objects.get(pk=name_of_substation_id)
      v1 = v.branch_id
      substations = NameOfSubstation.objects.filter(branch_id=v1)
      branchs = NameOfBranch.objects.all()

      return render(request, 'accounting/substation_jur.html', {'commutation_journal': journal, 'substations': substations, 'branchs': branchs, 'title':'Комутационный журнал'})

def branch_jur(request, branch_id):
    journal = CommutationJournal.objects.filter(branch_id=branch_id)
    substations = NameOfSubstation.objects.filter(branch_id=branch_id)
    branchs = NameOfBranch.objects.all()
    return render(request, 'accounting/branch_jur.html', {'commutation_journal': journal, 'substations': substations, 'branchs': branchs, 'title': 'Комутационный журнал'})


def circuit_breakers_jur(request):
    circuit_breakers = CircuitBreakers.objects.all()
    substations = NameOfSubstation.objects.all()
    branchs = NameOfBranch.objects.all()
    return render(request, 'accounting/circuit_breakers_jur.html', {'circuit_breakers': circuit_breakers, 'substations': substations, 'branchs': branchs,'title': 'Выключатели'})


def breakers_substation_jur(request, name_of_substation_id):
    circuit_breakers = CircuitBreakers.objects.filter(name_of_substation_id=name_of_substation_id)
    v = NameOfSubstation.objects.get(pk=name_of_substation_id)
    v1 = v.branch_id
    substations = NameOfSubstation.objects.filter(branch_id=v1)
    branchs = NameOfBranch.objects.all()
    return render(request, 'accounting/circuit_breakers_jur.html',
                  {'circuit_breakers': circuit_breakers, 'substations': substations, 'branchs': branchs,
                   'title': 'Выключатели'})


def breakers_branch_jur(request, branch_id):
    circuit_breakers = CircuitBreakers.objects.filter(branch_id=branch_id)
    substations = NameOfSubstation.objects.filter(branch_id=branch_id)
    branchs = NameOfBranch.objects.all()
    return render(request, 'accounting/circuit_breakers_jur.html',
                  {'circuit_breakers': circuit_breakers, 'substations': substations, 'branchs': branchs,
                   'title': 'Выключатели'})


def add_commutation(request):
    journal = CommutationJournal.objects.all()
    substations = NameOfSubstation.objects.all()
    branchs = NameOfBranch.objects.all()
    if request.method == 'POST':
        form = JurForm(request.POST)
        #x = form.dispatcher_name# достаем из формы диспетчерское наименование
        #if form.is_valid():
        z = form.save(commit=False)
        x = z.dispatcher_name_id
        tok_kommutacii = z.current_of_commutation
        z.save()
        x1 = CircuitBreakers.objects.get(pk=x) # по дисп наименованию вызываем объект из базы выключателей
        x2 = x1.switch_type_id # сохраняем в переменную тип выключателя
        x3 = SwitchType.objects.get(pk=x2) # по типу  вызываем объект из базы типов выключателей
        nominal_tok_kommutacii = x3.rated_breaking_current
        znachenie_meh_resursa = x1.mechanical_resource
        znachenie_com_resursa = x1.switching_resource

        diap1 = x3.third_bound
        diap2 = x3.second_bound
        diap3 = x3.first_bound
        n_diap1 = x3.third_bound_number_of_commutation
        n_diap2 = x3.second_bound_number_of_commutation
        n_diap3 = x3.first_bound_number_of_commutation
        n_mehanichesk = x3.mechanical_resource
        y = vedenie_arhiva(nominal_tok_kommutacii, znachenie_meh_resursa, znachenie_com_resursa, tok_kommutacii, diap1, diap2, diap3, n_diap1, n_diap2, n_diap3, n_mehanichesk)
        znachenie_com_resursa = y[0]
        znachenie_meh_resursa = y[1]
        x1.switching_resource = znachenie_com_resursa
        x1.mechanical_resource = znachenie_meh_resursa
        x1.save()

        return render(request, 'accounting/index.html', {'commutation_journal': journal, 'substations': substations, 'branchs': branchs, 'title':'Комутационный журнал'})
        #return HttpResponse(znachenie_com_resursa)

    else:
        form = JurForm()
        return render(request, 'accounting/add_commutation.html', {'form': form})
