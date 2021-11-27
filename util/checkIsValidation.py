from django.contrib import messages
from django.shortcuts import redirect


def isValidation(request, path, message):
    if not request.user.is_authenticated:
        if message:
            messages.warning(request, message)
        return redirect(path)
