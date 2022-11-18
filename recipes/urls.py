from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RecipeAPIView, CategoryAPIView

router = SimpleRouter()
router.register('recipes', RecipeAPIView, basename='recipes')
router.register('categories', CategoryAPIView, basename='profiles')

urlpatterns = router.urls
# urlpatterns.append(path('recipes/upload/', RecipePhotoUpload.as_view()),)
urlpatterns = format_suffix_patterns(urlpatterns)
