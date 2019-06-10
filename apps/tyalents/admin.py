from django.contrib import admin

from apps.tyalents import models


class TyalentAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Tyalent


class ExperienceAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Experience


class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Skill


class LanguageAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Language


class EducationAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Education


class AchievementAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Achievement


class PortfolioAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Portfolio


admin.site.register(models.Tyalent, TyalentAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.Achievement, AchievementAdmin)
admin.site.register(models.Portfolio, PortfolioAdmin)
