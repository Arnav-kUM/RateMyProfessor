from django.urls import path
from Home import views

urlpatterns = [
    
    path('login',views.login,name = "login"),
    path('signup',views.signup,name = "signup"),
    path('searchprof',views.Search_Prof,name = "searchprof"),
    path('ProfReview',views.Prof_review,name = "ProfReview"),

]