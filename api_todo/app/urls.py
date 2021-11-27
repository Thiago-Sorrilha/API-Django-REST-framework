
# from django.db import router
from app.views import TodoViewSet
# from app.views import TodoDetailChangeAndDelete, TodoListAndCreate
# from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls


"""
urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
]
"""
