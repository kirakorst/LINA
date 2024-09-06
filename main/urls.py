from .views import other_page
from django.urls import path
from .views import index
from .views import BBLoginView
from .views import profile
from .views import BBLogoutView
from .views import ProfileEditView
from .views import PasswordEditView
from .views import RegisterView, RegisterDoneView
from .views import user_activate
from .views import ProfileDeleteView
from .views import info_view
from .views import contact_view
from . import views



app_name = 'main'
urlpatterns = [
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('contact/', contact_view, name='contact'),
    path('info/', info_view, name='info'),
    path('accounts/profile/delete', ProfileDeleteView.as_view(), name='profile_delete'),
    path('accounts/activate/<str:sign>/', user_activate, name='activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/edit/', PasswordEditView.as_view(), name='password_edit'),
    path('accounts/profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
