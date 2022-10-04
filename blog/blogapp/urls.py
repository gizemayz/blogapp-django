from django.urls import path
from .views import HomeView, AboutView, PostDetailView, NewPostView, UpdatePostView, DeletePostView, AddCommentView, AddCategoryView, CategoryView, CategoryListView  # SearchPostView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('about/', AboutView.as_view(), name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', NewPostView.as_view(), name='new_post'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='new_comment'),
    path('add_category/', AddCategoryView.as_view(), name='new_category'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryView.as_view(), name='each-category'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
