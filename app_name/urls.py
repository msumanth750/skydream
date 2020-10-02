from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'subjectmodel', api.SubjectModelViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for SubjectModel
    path('app_name/subjectmodel/', views.SubjectModelListView.as_view(), name='app_name_subjectmodel_list'),
    path('app_name/subjectmodel/create/', views.SubjectModelCreateView.as_view(), name='app_name_subjectmodel_create'),
    path('app_name/subjectmodel/detail/<int:pk>/', views.SubjectModelDetailView.as_view(), name='app_name_subjectmodel_detail'),
    path('app_name/subjectmodel/update/<int:pk>/', views.SubjectModelUpdateView.as_view(), name='app_name_subjectmodel_update'),
)

