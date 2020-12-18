from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import csv
from django.http import HttpResponse
from .models import *
class RecruitmentDetails(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'branch', 'batch', 'phoneNumber', 'status', 'recruitmentYear')
    list_filter = ('recruitmentYear', 'status', 'batch')
    list_editable = ('status', )
    readonly_fields = ('application_id', )
    filter_horizontal = ()
    search_fields = ('name', 'roll_number')
    actions = ['export_as_csv']
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = ['name', 'roll_number', 'branch', 'batch', 'phoneNumber','email', 'status', 'recruitmentYear']
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename = {}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = 'Export Selected'

class AccountDetails(UserAdmin):
    list_display = ('username', 'email', 'is_recruitment_applicant', 'is_admin')
    list_filter = ('is_recruitment_applicant', )
    filter_horizontal = ()
    fieldsets = ()
    search_fields = ('username', 'email')
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(Account, AccountDetails)
admin.site.register(RecruitmentApplicant, RecruitmentDetails)