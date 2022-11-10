from django.urls import path

from apps.blog.views import CategoryListView, PostByCategoryView

urlpatterns = [
    path('categories_blog/', CategoryListView.as_view(), name='category-list'),
    path('categories_blog/<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
]
