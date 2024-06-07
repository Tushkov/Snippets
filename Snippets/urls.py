from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="add"),
    path('snippets/list', views.snippets_page, name="list"),
    path('snippets/<int:snippet_id>', views.detail_snippet_page, name="detail"),
    path('snippets/delete/<int:snippet_id>', views.delete_snippet_page, name="delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

