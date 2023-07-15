from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user_page'),

    path('settings/', views.account_setting, name='settings'),

    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),

    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html')
         , name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html')
         , name='reset_password_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset-form.html')
         , name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html')
         , name="password_reset_complete"),
    # ##############################
    # path('password-reset/', auth_view.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
    #      name="password_reset"),
    #
    # path('password_reset/done/',
    #      auth_view.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
    #      name="password_reset_done"),
    #
    # path('password_reset_confirm/<uidb64>/<token>/',
    #      auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
    #      name="password_reset_confirm"),
    #
    # path('password_reset_complete/',
    #      auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
    #      name="password_reset_complete"),
]

# 1.system email form                password resetview as view()
# 2.email sent success message
#
#
