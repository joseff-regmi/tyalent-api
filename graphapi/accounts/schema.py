import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from apps.accounts.models import User, Profile


class UserQuery(DjangoObjectType):
    """
    User Node
    """
    class Meta:
        model = User
        filter_fields = {
            'email': ['exact', ]
        }
        exclude_fields = ('password', 'is_superuser', )
        interfaces = (graphene.relay.Node, )


class ProfileQuery(DjangoObjectType):
    """
    Profile Node
    """
    class Meta:
        model = Profile


class UserSchema(graphene.ObjectType):
    users = DjangoFilterConnectionField(UserQuery)
    user = graphene.Field(UserQuery)

    def resolve_user(self, info):
        if info.context.user.is_authenticated:
            return info.context.user
        return None
