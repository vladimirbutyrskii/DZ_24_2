from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons-create')
              ] + router.urls
