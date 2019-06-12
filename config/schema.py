import graphene

from graphapi.tyalents.schema import TyalentQueries
from graphapi.tyalents import mutations as tyalent_mutation
from graphapi.accounts.schema import UserSchema
from graphapi.accounts import mutations as accounts_mutation


class Queries(TyalentQueries, UserSchema, graphene.ObjectType):
    pass
    # tyalent_profile = graphene.Field(TyalentQueries)


class Mutations(graphene.ObjectType):
    register = accounts_mutation.Register.Field()
    login = accounts_mutation.Login.Field()
    activate = accounts_mutation.Activate.Field()
    deleteAccount = accounts_mutation.DeleteAccount.Field()
    refreshToken = accounts_mutation.RefreshToken.Field()
    resetPassword = accounts_mutation.ResetPassword.Field()
    resetPasswordConfirmation = accounts_mutation.ResetPasswordConfirm.Field()
    selectRole = accounts_mutation.SelectRole.Field()
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
