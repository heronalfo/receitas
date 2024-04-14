from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import RecipesModelsSerializer
from ..models import Recipes

class RecipesListViewAPIV1(APIView):

    def get(self, *args):
    
        recipes = Recipes.objects.all()
        
        serializer = RecipesModelsSerializer(instance=recipes, many=True)
        
        return Response(serializer.data)

class RecipesDetailListViewAPIV1(APIView):

    def get(self, *args, **kwargs):
    
    
        recipe = Recipes.objects.get(id=self.kwargs["id"])
        
        serializer = RecipesModelsSerializer(instance=recipe)
        
        return Response(serializer.data)
        
        
    