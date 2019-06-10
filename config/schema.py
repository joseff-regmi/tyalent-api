import graphene

from graphapi.tyalents.schema import TyalentQueries
from graphapi.tyalents import mutations as tyalent_mutation


class Queries(TyalentQueries, graphene.ObjectType):
    pass
    # tyalent_profile = graphene.Field(TyalentQueries)


class Mutations(graphene.ObjectType):
    tyalent = tyalent_mutation.CreateTyalent.Field()
    updateTyalent = tyalent_mutation.UpdateTyalent.Field()
    experience = tyalent_mutation.CreateExperience.Field()
    updateExperience = tyalent_mutation.UpdateExperience.Field()
    skill = tyalent_mutation.CreateSkill.Field()
    updateSkill = tyalent_mutation.UpdateSkill.Field()
    language = tyalent_mutation.CreateLanguage.Field()
    updateLanguage = tyalent_mutation.UpdateLanguage.Field()
    education = tyalent_mutation.CreateEducation.Field()
    updateEducation = tyalent_mutation.UpdateEducation.Field()
    achievement = tyalent_mutation.CreateAchievement.Field()
    updateAchievement = tyalent_mutation.UpdateAchievement.Field()
    portfolio = tyalent_mutation.CreatePortfolio.Field()
    updatePortfolio = tyalent_mutation.UpdatePortfolio.Field()
    portfolioGallery = tyalent_mutation.CreatePortfolioGallery.Field()
    updatePortfolioGallery = tyalent_mutation.UpdatePortfolioGallery.Field()


schema = graphene.Schema(query=Queries, mutation=Mutations)

# schema.execute(
#     '''
#         query {
#             hello
#         }
#     '''
# )
