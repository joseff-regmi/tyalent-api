import graphene

from core.utils import get_instance
from apps.tyalents import models
from graphapi.tyalents import schema
from graphapi.tyalents import types

# use decorator login_required


class CreateTyalent(graphene.Mutation):
    class Arguments:
        input = types.TyalentInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    tyalent = graphene.Field(schema.TyalentNode)

    @staticmethod
    def mutate(self, info, **args):
        is_authenticated = info.context.user.is_authenticated
        data = args.get('input')
        if not is_authenticated:
            errors = ['unauthenticated']
            return CreateTyalent(success=False, errors=errors)
        else:
            tyalent = models.Tyalent.objects.create(
                user=info.context.user,
                career=data.get('career', None),
                payment_type=data.get('payment_type', None),
                expected_salary=data.get('expected_salary', None),
                full_name=data.get('full_name', None),
                age=data.get('age', None),
                city=data.get('city', None),
                address=data.get('address', None),
                name_of_company=data.get('name_of_company', None),
                job_title=data.get('job_title', None),
                zip_code=data.get('zip_code', None),
                slogan=data.get('slogan', None),
                bio=data.get('bio', None),
                website=data.get('website', None),
                github=data.get('github', None),
                linkedin=data.get('linkedin', None),
                twitter=data.get('twitter', None),
                facebook=data.get('facebook', None))
            return CreateTyalent(tyalent=tyalent, success=True, errors=None)


class UpdateTyalent(graphene.Mutation):
    class Arguments:
        input = types.TyalentInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    tyalent = graphene.Field(schema.TyalentNode)

    @staticmethod
    def mutate(self, info, **args):
        is_authenticated = info.context.user.is_authenticated
        data = args.get('input')
        if not is_authenticated:
            errors = ['unauthenticated']
            return UpdateTyalent(success=False, errors=errors)
        else:
            tyalent = models.Tyalent.objects.get(user=info.context.user)
            tyalent.career = data.get('career', None)
            tyalent.payment_type = data.get('payment_type', None)
            tyalent.expected_salary = data.get('expected_salary', None)
            tyalent.full_name = data.get('full_name', None)
            tyalent.age = data.get('age', None)
            tyalent.city = data.get('city', None)
            tyalent.address = data.get('address', None)
            tyalent.name_of_company = data.get('name_of_company', None)
            tyalent.job_title = data.get('job_title', None)
            tyalent.zip_code = data.get('zip_code', None)
            tyalent.slogan = data.get('slogan', None)
            tyalent.bio = data.get('bio', None)
            tyalent.website = data.get('website', None)
            tyalent.github = data.get('github', None)
            tyalent.linkedin = data.get('linkedin', None)
            tyalent.twitter = data.get('twitter', None)
            tyalent.facebook = data.get('facebook', None)
            tyalent.save()
            return UpdateTyalent(tyalent=tyalent, success=True, errors=None)


class CreateExperience(graphene.Mutation):
    class Arguments:
        input = types.ExperienceInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    experience = graphene.Field(schema.ExperienceNode)

    @staticmethod
    def mutate(self, info, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ['unauthenticated']
            return CreateExperience(success=False, errors=errors)
        else:
            tyalent = models.Tyalent.objects.get(user=info.context.user)
            experience = models.Experience.objects.create(
                tyalent=tyalent,
                title=data.get('title', None),
                name_of_company=data.get('name_of_company', None),
                location=data.get('location', None),
                start_date=data.get('start_date', None),
                end_date=data.get('end_date', None),
            )
            return CreateExperience(experience=experience, success=True, errors=None)


class UpdateExperience(graphene.Mutation):
    class Arguments:
        input = types.ExperienceInput()
        id = graphene.String(required=True)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    experience = graphene.Field(schema.ExperienceNode)

    @staticmethod
    def mutate(self, info, id=None, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ["unauthenticated"]
            return UpdateExperience(success=False, errors=errors)
        else:
            experience = get_instance(models.Experience, id)
            experience.title = data.get('title', None)
            experience.name_of_company = data.get('name_of_company', None)
            experience.location = data.get('location', None)
            experience.start_date = data.get('start_date', None)
            experience.end_date = data.get('end_date', None)
            experience.save()
            return UpdateExperience(experience=experience, success=True, errors=None)


class CreateSkill(graphene.Mutation):
    class Arguments:
        input = types.SkillInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    skill = graphene.Field(schema.SkillNode)

    @staticmethod
    def mutate(self, info, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ['unauthenticated']
            return CreateSkill(success=False, errors=errors)
        else:
            tyalent = models.Tyalent.objects.get(user=info.context.user)
            skill = models.Skill.objects.create(
                tyalent=tyalent,
                heading=data.get('heading', None),
                title=data.get('title', None),
                description=data.get('description', None),
                level=data.get('level', None),

            )
            return CreateSkill(skill=skill, success=True, errors=None)


class UpdateSkill(graphene.Mutation):
    class Arguments:
        input = types.SkillInput()
        id = graphene.String(required=True)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    skill = graphene.Field(schema.SkillNode)

    @staticmethod
    def mutate(self, info, id=None, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ["unauthenticated"]
            return UpdateSkill(success=False, errors=errors)
        else:
            skill = get_instance(models.Skill, id)
            skill.heading = data.get('heading', None),
            skill.title = data.get('title', None)
            skill.description = data.get('description', None),
            skill.level = data.get('level', None),
            skill.save()
            return UpdateSkill(skill=skill, success=True, errors=None)


class CreateLanguage(graphene.Mutation):
    class Arguments:
        input = types.LanguageInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    language = graphene.Field(schema.LanguageNode)

    @staticmethod
    def mutate(self, info, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ['unauthenticated']
            return CreateLanguage(success=False, errors=errors)
        else:
            tyalent = models.Tyalent.objects.get(user=info.context.user)
            language = models.Language.objects.create(
                tyalent=tyalent,
                name=data.get('name', None),
            )
            return CreateLanguage(language=language, success=True, errors=None)


class UpdateLanguage(graphene.Mutation):
    class Arguments:
        input = types.LanguageInput()
        id = graphene.String(required=True)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    language = graphene.Field(schema.LanguageNode)

    @staticmethod
    def mutate(self, info, id=None, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ["unauthenticated"]
            return UpdateLanguage(success=False, errors=errors)
        else:
            language = get_instance(models.Language, id)
            language.name = data.get('name', None)
            language.save()
            return UpdateLanguage(language=language, success=True, errors=None)


class CreateEducation(graphene.Mutation):
    class Arguments:
        input = types.EducationInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    education = graphene.Field(schema.EducationNode)

    @staticmethod
    def mutate(self, info, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ['unauthenticated']
            return CreateEducation(success=False, errors=errors)
        else:
            tyalent = models.Tyalent.objects.get(user=info.context.user)
            education = models.Education.objects.create(
                tyalent=tyalent,
                title=data.get('title', None),
                sub_title=data.get('sub_title', None),
                start_date=data.get('start_date', None),
                end_date=data.get('end_date', None),
            )
            return CreateEducation(education=education, success=True, errors=None)


class UpdateEducation(graphene.Mutation):
    class Arguments:
        input = types.EducationInput()
        id = graphene.String(required=True)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    education = graphene.Field(schema.EducationNode)

    @staticmethod
    def mutate(self, info, id=None, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ["unauthenticated"]
            return UpdateEducation(success=False, errors=errors)
        else:
            education = get_instance(models.Education, id)
            education.title = data.get('title', None)
            education.sub_title = data.get('sub_title', None)
            education.start_date = data.get('start_date', None)
            education.end_date = data.get('end_date', None)
            education.save()
            return UpdateEducation(education=education, success=True, errors=None)


class CreateAchievement(graphene.Mutation):
    class Arguments:
        input = types.AchievementInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    achievement = graphene.Field(schema.AchievementNode)

    @staticmethod
    def mutate(self, info, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ['unauthenticated']
            return CreateAchievement(success=False, errors=errors)
        else:
            tyalent = models.Tyalent.objects.get(user=info.context.user)
            achievement = models.Achievement.objects.create(
                tyalent=tyalent,
                category=data.get('category', None),
                title=data.get('title', None),
                sub_title=data.get('sub_title', None),
                description=data.get('description', None),
            )
            return CreateAchievement(achievement=achievement, success=True, errors=None)


class UpdateAchievement(graphene.Mutation):
    class Arguments:
        input = types.AchievementInput()
        id = graphene.String(required=True)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    achievement = graphene.Field(schema.AchievementNode)

    @staticmethod
    def mutate(self, info, id=None, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ["unauthenticated"]
            return UpdateAchievement(success=False, errors=errors)
        else:
            # tyalent = models.Tyalent.objects.get(user=info.context.user)
            achievement = get_instance(models.Achievement, id)
            # achievement = Achievement.objects.get(tyalent=tyalent, id=data.get('id'))
            achievement.category = data.get('category', None)
            achievement.title = data.get('title', None)
            achievement.sub_title = data.get('sub_title', None)
            achievement.description = data.get('description', None)
            achievement.save()
            return UpdateAchievement(achievement=achievement, success=True, errors=None)


class CreatePortfolio(graphene.Mutation):
    class Arguments:
        input = types.PortfolioInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    portfolio = graphene.Field(schema.PortfolioNode)

    @staticmethod
    def mutate(self, info, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ['unauthenticated']
            return CreatePortfolio(success=False, errors=errors)
        else:
            tyalent = models.Tyalent.objects.get(user=info.context.user)
            portfolio = models.Portfolio.objects.create(
                tyalent=tyalent,
                category=data.get('category', None),
                title=data.get('title', None),
                sub_title=data.get('sub_title', None),
                description=data.get('description', None),
                url=data.get('url', None),
                image=info.context.FILES.get(data.get('image', None))
            )
            return CreatePortfolio(portfolio=portfolio, success=True, errors=None)


class UpdatePortfolio(graphene.Mutation):
    class Arguments:
        input = types.PortfolioInput()
        id = graphene.String(required=True)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    portfolio = graphene.Field(schema.PortfolioNode)

    @staticmethod
    def mutate(self, info, id=None, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ["unauthenticated"]
            return UpdatePortfolio(success=False, errors=errors)
        else:
            portfolio = get_instance(models.Portfolio, id)
            portfolio.category = data.get('category', None)
            portfolio.title = data.get('title', None)
            portfolio.sub_title = data.get('sub_title', None)
            portfolio.description = data.get('description', None)
            portfolio.url = data.get('url', None)
            portfolio.image = info.context.FILES.get(data.get('image', None))
            portfolio.save()
            return UpdatePortfolio(portfolio=portfolio, success=True, errors=None)


class CreatePortfolioGallery(graphene.Mutation):
    class Arguments:
        input = types.PortfolioGalleryInput(required=True)
        id = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    portfolio_gallery = graphene.Field(schema.PortfolioGalleryNode)

    @staticmethod
    def mutate(self, info, id=None, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ['unauthenticated']
            return CreatePortfolioGallery(success=False, errors=errors)
        else:
            portfolio = get_instance(models.Portfolio, id)
            portfolio_gallery = models.Gallery.objects.create(
                portfolio=portfolio,
                title=data.get('title', None),
                description=data.get('description', None),
                url=data.get('url', None),
                image=info.context.FILES(data.get('image', None))
            )
            return CreatePortfolioGallery(portfolio_gallery=portfolio_gallery, success=True, errors=None)


class UpdatePortfolioGallery(graphene.Mutation):
    class Arguments:
        input = types.PortfolioGalleryInput()
        id = graphene.String(required=True)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    portfolio_gallery = graphene.Field(schema.PortfolioGalleryNode)

    @staticmethod
    def mutate(self, info, id=None, **args):
        data = args.get('input')
        is_authenticated = info.context.user.is_authenticated
        if not is_authenticated:
            errors = ["unauthenticated"]
            return UpdatePortfolioGallery(success=False, errors=errors)
        else:
            portfolio_gallery = get_instance(models.Gallery, id)
            portfolio_gallery.title = data.get('title', None)
            portfolio_gallery.description = data.get('description', None)
            portfolio_gallery.url = data.get('url', None)
            portfolio_gallery.image = info.context.FILES(
                data.get('image', None))
            portfolio_gallery.save()
            return UpdatePortfolioGallery(portfolio_gallery=portfolio_gallery, success=True, errors=None)
