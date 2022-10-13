from django.urls import path

from movies import views

urlpatterns = [
    path('list/', views.movie_list_view, name='list'),
    path('image/<int:pk>', views.image_view, name="image"),
    path(
        'upload-poster/',
        views.upload_poster,
        name="upload-poster"
    )
]
