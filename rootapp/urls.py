from django.urls import path

from rootapp import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.index,name='index'),
    path('dash',views.dash,name='dash'),
    path('submit',views.submit,name='submit'),
    path('viewdata', views.viewdata, name='viewdata'),
    path('delete/<int:id>/', views.deldata, name='deldata'),
    path('update/<int:id>/', views.update_data, name='update_data'),

]
