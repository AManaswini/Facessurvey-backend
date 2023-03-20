from django.urls import path
from faces import views

urlpatterns = [
    path('getuserrelease1/',views.getUserPatternRelease1),
    path('getuserreleaseevaluation1/',views.getUserPatternReleaseevaluation1),
    path('postresults/',views.postResults)
]