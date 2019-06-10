import graphene
from core.file_upload import types


class TyalentInput(graphene.InputObjectType):

    career = graphene.String(description="Career")
    payment_type = graphene.String(
        description="Type of Payment. Is it hourly or salary based?")
    expected_salary = graphene.Float(description="Your expected Salary")
    full_name = graphene.String(description='Full Name')
    age = graphene.Int(description='Age')
    city = graphene.String(description='City')
    address = graphene.String(description='Address')
    name_of_company = graphene.String(description='Name of Company')
    job_title = graphene.String(description='Job Title')
    zip_code = graphene.Int(description='Zip Code')
    slogan = graphene.String(description='Slogan')
    bio = graphene.String(description='Bio')
    website = graphene.String(description='Website')
    github = graphene.String(description='Github')
    twitter = graphene.String(description='Twitter')
    linkedin = graphene.String(description='Linked in')
    facebook = graphene.String(description='Facebook')


class ExperienceInput(graphene.InputObjectType):

    title = graphene.String(description='Title')
    name_of_company = graphene.String(description='Name of Company')
    location = graphene.String(description='Location')
    start_date = graphene.types.datetime.Date(description='Start Date')
    end_date = graphene.types.datetime.Date(description='End Date')


class SkillInput(graphene.InputObjectType):

    heading = graphene.String(
        description='Heading of Skill like Technical Skill')
    title = graphene.String(description='Title of Skill')
    description = graphene.String(description='Title of Skill')
    level = graphene.Float(description='Level of Skill between 1 - 5')


class LanguageInput(graphene.InputObjectType):

    name = graphene.String(description='Name of Language')


class EducationInput(graphene.InputObjectType):

    title = graphene.String(description='Title of Education')
    sub_title = graphene.String(description='Sub Title of Education')
    start_date = graphene.types.datetime.Date(description='Start Date')
    end_date = graphene.types.datetime.Date(description='End Date')


class AchievementInput(graphene.InputObjectType):

    category = graphene.String(description='Category')
    title = graphene.String(description='Title')
    sub_title = graphene.String(description='Sub Title')
    description = graphene.String(description='Description')


class PortfolioInput(graphene.InputObjectType):

    category = graphene.String(description='Category')
    title = graphene.String(description='Title')
    sub_title = graphene.String(description='Sub Title')
    description = graphene.String(description='Description')
    url = graphene.String(description='URL')
    image = types.Upload(description='Upload image')


class PortfolioGalleryInput(graphene.InputObjectType):

    title = graphene.String(description='Title')
    description = graphene.String(description='Description')
    url = graphene.String(description='URL')
    image = types.Upload(description='Upload image')
