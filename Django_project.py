from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('interest_quiz/', views.interest_quiz, name='interest_quiz'),
    path('community_groups/', views.community_groups, name='community_groups'),
    path('join_group/<int:group_id>/', views.join_group, name='join_group'),
    path('create_group/', views.create_group, name='create_group'),
    path('search_groups/', views.search_groups, name='search_groups'),
     path('fundraiser_list/', views.fundraiser_list, name='fundraiser_list'),
    path('create_fundraiser/', views.create_fundraiser, name='create_fundraiser'),
    path('donate/<int:fundraiser_id>/', views.donate, name='donate'),
    path('donate/<int:fundraiser_id>/credit_card/', views.credit_card_payment, name='credit_card_payment'),
    path('donate/<int:fundraiser_id>/debit_card/', views.debit_card_payment, name='debit_card_payment'),
    path('donate/<int:fundraiser_id>/paypal/', views.paypal_payment, name='paypal_payment'),
    path('donate/<int:fundraiser_id>/upi/', views.upi_payment, name='upi_payment'),
    path('payment_success/<int:fundraiser_id>/', views.payment_success, name='payment_success'),
    path('group_chat/<int:group_id>/', views.group_chat, name='group_chat'),
    path('my_groups/', views.my_groups, name='my_groups'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
        path('', views.home, name='home'),
    path('group/<int:pk>/', views.group_detail, name='group_detail'),
   

]
