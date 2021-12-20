from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from snippet_app.views import (
    HelloView,
    RegisterApi,
    SnippetView,
    SnippetDetailView,
    TagListView,
    SnippetByTagView,
)

urlpatterns = [
    # Your URLs...
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('', HelloView.as_view(), name='homepage'),
    path('api/register/', RegisterApi.as_view()),

    path('api/snippet/', SnippetView.as_view(), name='snippet'),
    path('api/snippet/add/', SnippetView.as_view(), name='snippet-add'),

    path('api/snippet/<id>/', SnippetDetailView.as_view(), name='snippet-details'),
    path('api/snippet/delete/<id>/', SnippetDetailView.as_view(), name='snippet-delete'),
    path('api/snippet/edit/<id>/', SnippetDetailView.as_view(), name='snippet-edit'),

    path('api/tag/list/', TagListView.as_view(), name='tags'),
    path('api/snippet/list/<tag_id>/', SnippetByTagView.as_view(), name='snippet-by-tag-id'),
]
