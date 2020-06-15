from django.contrib import admin
from .models import CircuitBreakers
from .models import CommutationJournal
from .models import NameOfSubstation
from .models import NameOfBranch
from .models import VoltageClass
from .models import SwitchType

class CircuitBreakersAdmin(admin.ModelAdmin) :
    list_display = ('id', 'branch', 'name_of_substation', 'dispatcher_name', 'switch_type', 'updated_at', 'switching_resource', 'mechanical_resource')
    search_fields = ('dispatcher_name', 'name_of_substation')
    list_filter = ('name_of_substation', 'branch')

class CommutationJournalAdmin(admin.ModelAdmin) :
    list_display = ('id', 'branch', 'name_of_substation', 'dispatcher_name', 'date_of_commutation', 'current_of_commutation', 'user_name')
    search_fields = ('dispatcher_name', 'name_of_substation')
    list_filter = ('name_of_substation', 'branch')




admin.site.register(CircuitBreakers, CircuitBreakersAdmin)
admin.site.register(CommutationJournal, CommutationJournalAdmin)
admin.site.register(NameOfSubstation)
admin.site.register(NameOfBranch)
admin.site.register(VoltageClass)
admin.site.register(SwitchType)
