import graphene

from django.contrib.auth.tokens import default_token_generator
from djoser.conf import settings as djoser_settings
from djoser.utils import decode_uid
from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer,
    RefreshJSONWebTokenSerializer
)
from django.conf import settings

from apps.accounts.serializers import PasswordResetConfirmRetypeSerializer, RegistrationSerializer
from .schema import UserQuery, ProfileQuery
from .types import ProfileInput
from .utils import send_activation_email, send_password_reset_email

User = settings.AUTH_USER_MODEL


class Register(graphene.Mutation):
    '''
        Mutation to register a user
    '''
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        password_repeat = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    email = graphene.String()

    def mutate(self, info, email, password, password_repeat):
        if password == password_repeat:
            try:
                serializer = RegistrationSerializer(data={
                    'email': email,
                    'password': password,
                    'is_active': False
                })
                if serializer.is_valid():
                    user = serializer.save()
                    if djoser_settings.get('SEND_ACTIVATION_EMAIL'):
                        context = {
                            'user': user,
                            'request': info.context
                        }
                        send_activation_email(context)
                    return Register(success=bool(user.id), email=user.email)
                else:
                    print("error", serializer.errors)
            except Exception:
                # errors = {
                #     "email": "Email already registered"
                # }
                errors = ["email", "Email already registered"]
                return Register(success=False, errors=errors)
            errors = ["password", "Passwords don't match."]
            return Register(success=False, errors=errors)


class Activate(graphene.Mutation):
    """
    Mutation to activate a user's registration
    """
    class Arguments:
        token = graphene.String(required=True)
        uid = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, token, uid):

        try:
            uid = decode_uid(uid)
            user = User.objects.get(pk=uid)
            if not default_token_generator.check_token(user, token):
                return Activate(success=False, errors=['stale token'])
            user.is_active = True
            user.save()
            return Activate(success=True, errors=None)

        except Exception:
            return Activate(success=False, errors=['unknown user'])


class Login(graphene.Mutation):
    """
    Mutation to login a user
    """
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    token = graphene.String()
    user = graphene.Field(UserQuery)

    def mutate(self, info, email, password):
        user = {'email': email, 'password': password}
        serializer = JSONWebTokenSerializer(data=user)
        if serializer.is_valid():
            token = serializer.object['token']
            user = serializer.object['user']
            print('user', user)
            return Login(success=True, user=user, token=token)
        else:
            print("serializers errors", serializer.errors)
            return Login(
                success=False,
                token=None,
                errors=['email', 'Unable to login with provided credentials.']
            )


class RefreshToken(graphene.Mutation):
    """
    Mutation to reauthenticate a user
    """
    class Arguments:
        token = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    token = graphene.String()

    def mutate(self, info, token):
        serializer = RefreshJSONWebTokenSerializer(data={'token': token})
        if serializer.is_valid():
            return RefreshToken(
                success=True,
                token=serializer.object['token'],
                errors=None
            )
        else:
            return RefreshToken(
                success=False,
                token=None,
                errors=['email', 'Unable to login with provided credentials.']
            )


class ResetPassword(graphene.Mutation):
    """
    Mutation for requesting a password reset email
    """

    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, email):
        try:
            user = User.objects.get(email=email)
            context = {
                'user': user,
                'request': info.context
            }
            send_password_reset_email(context)
            return ResetPassword(success=True)
        except Exception:
            return ResetPassword(success=True)


class ResetPasswordConfirm(graphene.Mutation):
    """
    Mutation for requesting a password reset email
    """

    class Arguments:
        uid = graphene.String(required=True)
        token = graphene.String(required=True)
        email = graphene.String(required=True)
        new_password = graphene.String(required=True)
        re_new_password = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, uid, token, email, new_password, re_new_password):
        serializer = PasswordResetConfirmRetypeSerializer(data={
            'uid': uid,
            'token': token,
            'email': email,
            'new_password': new_password,
            're_new_password': re_new_password,
        })
        if serializer.is_valid():
            serializer.user.set_password(serializer.data['new_password'])
            serializer.user.save()
            return ResetPasswordConfirm(success=True, errors=None)
        else:
            return ResetPasswordConfirm(
                success=False, errors=[serializer.errors])


class DeleteAccount(graphene.Mutation):
    """
    Mutation to delete an account
    """
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, email, password):
        user = info.context.user
        is_authenticated = user.is_authenticated
        if not is_authenticated:
            errors = ['unauthenticated']
        elif is_authenticated and not email == user.email:
            errors = ['forbidden']
        elif not user.check_password(password):
            errors = ['wrong password']
        else:
            user.delete()
            return DeleteAccount(success=True)
        return DeleteAccount(success=False, errors=errors)


class CreateProfile(graphene.Mutation):
    """
    Mutation to create a profile
    """
    class Arguments:
        input = ProfileInput()

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    profile = graphene.Field(ProfileQuery)

    def mutate(self, info, **args):
        user = info.context.user
        data = args.get('input')
        if not user.is_authenticated:
            errors = ['unauthenticated']
            return CreateProfile(success=False, errors=errors)
        else:
            profile = Profile.objects.create(
                user=user,
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                age=data.get('age'),
                country=data.get('country'),
                city=data.get('city'),
                address=data.get('address'),
                phone_number=data.get('phone_number'),
                zip_code=data.get('zip_code'),
                slogan=data.get('slogan'),
                bio=data.get('bio')
            )
            return CreateProfile(profile=profile, success=True, errors=None)


class UpdateProfile(graphene.Mutation):
    """
    Mutation to create a profile
    """
    class Arguments:
        input = ProfileInput()

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    profile = graphene.Field(ProfileQuery)

    def mutate(self, info, **args):
        user = info.context.user
        data = args.get('input')
        if not user.is_authenticated:
            errors = ['unauthenticated']
            return UpdateProfile(success=False, errors=errors)
        else:
            profile = Profile.objects.get(user=user)
            profile.first_name = data.get('first_name')
            profile.last_name = data.get('last_name')
            profile.age = data.get('age')
            profile.country = data.get('country')
            profile.city = data.get('city')
            profile.address = data.get('address')
            profile.phone_number = data.get('phone_number')
            profile.zip_code = data.get('zip_code')
            profile.slogan = data.get('slogan')
            profile.bio = data.get('bio')
            return UpdateProfile(profile=profile, success=True, errors=None)


class SelectRole(graphene.Mutation):
    '''
        mutation to select a role that can be tyalent, company or recruiter
    '''
    class Arguments:
        role = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    role = graphene.String()

    def mutate(self, info, role):
        user = info.context.user
        is_authenticated = user.is_authenticated
        if is_authenticated:
            if role == "is_company":
                user.is_company = True
            if role == "is_recruiter":
                user.is_recruiter = True
            else:
                user.is_tyalent = True
            user.save()
            return SelectRole(success=True, role=role)
        return SelectRole(success=False, errors=["Not authenticated"])
