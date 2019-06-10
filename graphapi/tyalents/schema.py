from graphene import relay, ObjectType, Field
from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField
from graphene_django.filter.fields import DjangoFilterConnectionField

from apps.tyalents import models


class TyalentNode(DjangoObjectType):
    class Meta:
        model = models.Tyalent
        interfaces = (relay.Node, )


class ExperienceNode(DjangoObjectType):
    class Meta:
        model = models.Experience
        interfaces = (relay.Node, )


class SkillNode(DjangoObjectType):
    class Meta:
        model = models.Skill
        interfaces = (relay.Node, )


class LanguageNode(DjangoObjectType):
    class Meta:
        model = models.Language
        interfaces = (relay.Node, )


class EducationNode(DjangoObjectType):
    class Meta:
        model = models.Education
        interfaces = (relay.Node, )


class AchievementNode(DjangoObjectType):
    class Meta:
        model = models.Achievement
        interfaces = (relay.Node, )


class PortfolioNode(DjangoObjectType):
    class Meta:
        model = models.Portfolio
        interfaces = (relay.Node, )


class PortfolioGalleryNode(DjangoObjectType):
    class Meta:
        model = models.Gallery
        interfaces = (relay.Node, )


class TyalentQueries(ObjectType):
    tyalent = Field(TyalentNode)
    tyalents = DjangoConnectionField(TyalentNode)
    experience = Field(ExperienceNode)
    experiences = DjangoConnectionField(ExperienceNode)
    skill = Field(SkillNode)
    skills = DjangoConnectionField(SkillNode)
    language = Field(LanguageNode)
    languages = DjangoConnectionField(LanguageNode)
    education = Field(EducationNode)
    educations = DjangoConnectionField(EducationNode)
    achievement = Field(AchievementNode)
    achievements = DjangoConnectionField(AchievementNode)
    portfolio = Field(PortfolioNode)
    portfolios = DjangoConnectionField(PortfolioNode)
    gallery = Field(PortfolioGalleryNode)
    galleries = DjangoConnectionField(PortfolioGalleryNode)

    @staticmethod
    def resolve_tyalent(self, info, **kwargs):
        if info.context.user.is_authenticated:
            return models.Tyalent.objects.get(user=info.context.user)
        return None
