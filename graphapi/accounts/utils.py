from djoser.compat import get_user_email
from djoser.email import ActivationEmail, PasswordResetEmail


def send_activation_email(context):
    print("######## send_activation_email user ##############", context.user)
    to = [get_user_email(context.user)]
    ActivationEmail(context.request, {'user': context.user}).send(to)


def send_password_reset_email(context):
    to = [get_user_email(context.user)]
    PasswordResetEmail(context.request, {'user': context.user}).send(to)
