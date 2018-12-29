from django.urls import path
from . import views
from .views import IndexView, DetailView, ResultsView

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name="index" ),
    path('<int:pk>/', DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),

]