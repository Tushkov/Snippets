from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="add"),
    path('snippets/list', views.snippets_page, name="list"),
    path('snippets/<int:snippet_id>', views.detail_snippet_page, name="detail"),
    path('snippets/<int:snippet_id>/delete', views.delete_snippet_page, name="delete"),
    path('snippets/<int:snippet_id>/edit', views.edit_snippet_page, name="edit"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
