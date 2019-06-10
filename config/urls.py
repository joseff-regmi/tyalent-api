from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.conf import settings
from django.urls import path


from core.file_upload.views import FileUploadGraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(
        FileUploadGraphQLView.as_view(graphiql=settings.DEBUG))),
]
