from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from core.models.timestamp_models import TimeStampModels
from apps.accounts.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Company(TimeStampModels):
    COMPANY_SIZE = (
        ('1-9', '1-9'),
        ('10-49', '10-49'),
        ('50-99', '50-99'),
        ('99-999', '99-999'),
        ('1000+', '1000+'),
    )
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="company")
    name_of_company = models.CharField(max_length=200, blank=True, null=True)
    business_email = models.EmailField(blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    company_size = models.CharField(
        max_length=7, choices=COMPANY_SIZE, default="1-9")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories", default="")
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    google_plus = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name_of_company}"


class Service(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=250, blank=False, null=False)
    sub_title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='company/services/', blank=True, null=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.company.__str__()} - {self.title}"
