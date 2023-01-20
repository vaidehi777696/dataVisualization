from django.contrib import admin
from .models import Company
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company

class CompanyAdmin(ImportExportModelAdmin):
    company_resources = CompanyResource

admin.site.register(Company,CompanyAdmin)
