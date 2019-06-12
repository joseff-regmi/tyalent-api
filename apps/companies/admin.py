from django.contrib import admin

from apps.companies.models import Company, Service, Category


class CompanyAdmin(admin.ModelAdmin):
    class Meta:
        model = Company


class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


admin.site.register(Company, CompanyAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
