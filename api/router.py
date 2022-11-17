from api import views as api_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('questions',api_views.QuestionViewSet)