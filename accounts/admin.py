from django.contrib import admin
# Register your models here.
from .models import addRecipe,recipeComment


class addRecipeAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "timestamp", "updated")

    class Meta:
        model = addRecipe


admin.site.register(addRecipe, addRecipeAdmin)

class recipeCommenteAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "timestamp", "updated")

    class Meta:
        model = recipeComment


admin.site.register(recipeComment, recipeCommenteAdmin)