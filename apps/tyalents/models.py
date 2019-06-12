from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from core.models.timestamp_models import TimeStampModels
from apps.accounts.models import Profile
from core.utils import create_slug


class Tyalent(TimeStampModels):
    CAREER_CHOICES = (
        ('Beginner', 'begineer'),
        ('Intermediate', 'intermediate'),
        ('Experienced', 'experienced'),
    )
    PAY_CHOICEs = (
        ('Hourly Rate', 'hourly_rate'),
        ('Salary', 'salary'),
    )
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    career = models.CharField(
        max_length=14, default="begineer", choices=CAREER_CHOICES)
    payment_type = models.CharField(
        max_length=12, choices=PAY_CHOICEs, default="salary")
    expected_salary = models.FloatField(blank=False, null=False)
    name_of_company = models.CharField(max_length=150, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Tyalent"
        verbose_name_plural = "Tyalents"

    def __str__(self):
        return f"{self.user.__str__()}"


class Experience(TimeStampModels):
    tyalent = models.ForeignKey(
        Tyalent, on_delete=models.CASCADE, related_name="experience")
    title = models.CharField(max_length=150, blank=False, null=False)
    name_of_company = models.CharField(max_length=150, blank=False, null=False)
    location = models.CharField(max_length=150, blank=False, null=False)
    start_date = models.DateField(max_length=150, blank=False, null=False)
    end_date = models.DateField(max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return self.title


class Skill(TimeStampModels):
    tyalent = models.ForeignKey(
        Tyalent, on_delete=models.CASCADE, related_name="skill")
    # Technical Skills, Operational Skills, Management Skills
    heading = models.CharField(max_length=80, blank=True, null=True)
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    level = models.FloatField(default=1, validators=[
                              MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.title


class Language(TimeStampModels):
    tyalent = models.ForeignKey(
        Tyalent, on_delete=models.CASCADE, related_name="language")
    name = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.name


class Education(TimeStampModels):
    tyalent = models.ForeignKey(
        Tyalent, on_delete=models.CASCADE, related_name="education")
    title = models.CharField(max_length=150, blank=False, null=False)
    sub_title = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(max_length=150, blank=False, null=False)
    end_date = models.DateField(max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return self.title


class Achievement(TimeStampModels):
    tyalent = models.ForeignKey(
        Tyalent, on_delete=models.CASCADE, related_name="achievement")
    category = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=250, blank=False, null=False)
    sub_title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        return f"{self.category} - {self.title}"


class Portfolio(TimeStampModels):
    tyalent = models.ForeignKey(
        Tyalent, on_delete=models.CASCADE, related_name="portfolio")
    category = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=250, blank=False, null=False)
    sub_title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"

    def __str__(self):
        return f"{self.title}"


class Gallery(TimeStampModels):
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="gallery")
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='portfolio/gallery/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return f"{self.portfolio.__str__()} - {self.title}"


class JobType(TimeStampModels):
    tyalent = models.ForeignKey(
        Tyalent, on_delete=models.CASCADE, related_name="job_type")
    is_freelance = models.BooleanField(default=False)
    is_full_time = models.BooleanField(default=True)
    is_part_time = models.BooleanField(default=False)
    is_internship = models.BooleanField(default=False)
    is_temporary = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Job Type'
        verbose_name_plural = 'Job Types'

    def __str__(self):
        return f"{self.tyalent.__str__()}"


# class CareerLevel(TimeStampModels):
#     CAREER_CHOICES = (
#         'Beginner', 'begineer',
#         'Intermediate', 'intermediate',
#         'Experienced', 'experienced',
#     )
#     career = models.CharField(
#         max_length=14, default="begineer", choices=CAREER_CHOICES)

#     class Meta:
#         verbose_name = 'Career Level'
#         verbose_name = 'Career Levels'

#     def __str__(self):
#         return self.career
