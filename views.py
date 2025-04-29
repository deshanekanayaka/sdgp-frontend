from django.shortcuts import render, redirect
from .forms import LocalAccountForm


def local_account_login(request):
    if request.method == "POST":
        form = LocalAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")  # Create a success page or message
    else:
        form = LocalAccountForm()
    return render(request, "login.html", {"form": form})
