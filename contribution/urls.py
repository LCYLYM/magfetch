from django.urls import path
from .views import (
    ContributionCategoryCreateView,
    ContributionCategoryUpdateView,
    ContributionCategoryDeleteView,
    ContributionUploadView,
    ContributionListView,
)

urlpatterns = [
    # Contribution Category
    path('category/create/', ContributionCategoryCreateView.as_view(),
         name='category_create'),
    path('category/<slug>/update/', ContributionCategoryUpdateView.as_view(),
         name='category_update'),
    path('category/<slug>/delete/', ContributionCategoryDeleteView.as_view(),
         name='category_delete'),
    # Contribution
    path('upload/', ContributionUploadView.as_view(), name='upload'),
    path('list/', ContributionListView.as_view(), name='contribution_list'),
    path('<slug>/detail/', ContributionUploadView.as_view(), name='contribution_detail'),
]
