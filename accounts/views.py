from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.shortcuts import render, redirect
from .models import addRecipe, recipeComment
from .forms import UserLoginForms, UserRegisterForm, addRecipeForm, recipeCommentForm


# Create your views here.
def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    print("nopes")
    title = "Login"
    form = UserLoginForms(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "form": form,
        "title": "Login"
    }
    return render(request, "login.html", context)


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": "User Register"
    }
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return render(request, "form.html", {})

def allrecipe(request):
    if not request.user.is_authenticated():
        return redirect("login")
    queryset = addRecipe.objects.all()
    print(queryset)
    context = {
        "queryset": queryset,
    }
    return render(request, "allrecipe.html", context)

def homeIndex(request):
    if not request.user.is_authenticated():
        return redirect("login")

    form = addRecipeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        recipe_add = form.cleaned_data.get("recipe_name")  # one way to print
        recipe_add = form.cleaned_data.get("recipe_add")
        instance.username = request.user.username
        instance.save()
        return redirect("/")
    context = {
        "form": form,
    }
    return render(request, "home.html", context)

def commentrecipe(request, recipeid):
    if not request.user.is_authenticated():
        return redirect("login")
    queryset = addRecipe.objects.all().filter(pk=recipeid)
    queryset1 = recipeComment.objects.all().filter(recipe_pk=recipeid)


    form = recipeCommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        recipe_comment = form.cleaned_data.get("recipe_comment")
        instance.username = request.user.username
        instance.recipe_pk = recipeid
        instance.save()
    context = {
        "form" : form,
        "queryset" : queryset,
        "queryset1" : queryset1,
        "recipeid" : recipeid,
    }
    print("sachin")
    print(recipeid)
    return render(request, "hola.html", context)
