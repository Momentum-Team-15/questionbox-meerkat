"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views as api_views
from api.router import router

urlpatterns = [
    path("", include("api.urls")),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/', include(router.urls)),
    path('api/questions/<int:question_pk>/answers/', api_views.AnswerListCreateView.as_view(), name="answers"),
    path('api/user/<int:user_pk>/questions/', api_views.UserQuestions.as_view(), name="user_questions"),
    path('api/myquestions/', api_views.MyQuestions.as_view(), name="my_questions"),
    path('api/questions/<int:question_pk>/favorites/', api_views.CreateUpdateFavoriteView.as_view(), name="favorite_questions"),
    path('api/myfavorites/', api_views.FavoriteQuestionListView.as_view(), name="list_favorite"),
    path("api/questions/<int:question_pk>/answers/<int:pk>/accept/", api_views.AnswerAcceptedView.as_view(), name="accept_answer"),
    path('api/myanswers/', api_views.MyAnswers.as_view(), name="my_answers")
]
