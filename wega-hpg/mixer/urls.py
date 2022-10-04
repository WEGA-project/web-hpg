from django.urls import path
from mixer.views import mixer, mixer_add, mixer_del,mixer_history, \
    mixer_history_add, mixer_history_clear, mixer_zero

urlpatterns = [
    path('', mixer, name='mixer_index'),
    path('add/', mixer_add, name='mixer_add'),
    path('del/<int:pk>/', mixer_del, name='mixer_del'),
    path('<int:pk>/', mixer_history, name='mixer_history'),
    path('<int:pk>/<str:pomp>/', mixer_zero, name='mixer_zero'),
    path('history/del/<int:pk>/', mixer_history_clear, name='mixer_history_clear'),
    path('history/add/', mixer_history_add, name='mixer_history_add'),
]
