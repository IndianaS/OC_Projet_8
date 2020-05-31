from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from products.models import Favorite

from .forms import CustomUserCreationForm


@login_required(login_url='/users/login/')
def profile(request):
    """Django view profile page."""

    return render(request, 'users/profile.html')


def create_account(request):
    """Django view account creation."""

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/users/profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/create_account.html', {'form': form})


@login_required(login_url='/users/login/')
def favorites_user(request):
    """Django view favorite page of users."""

    user = request.user
    product_favorite = Favorite.objects.filter(user=user)
    substitutes = [favorite.substitute for favorite in product_favorite]

    return render(request, 'users/favorites.html',
                  {'substitutes': substitutes})

def password_reset(request):
    return render(request, 'users/password_reset.html')
