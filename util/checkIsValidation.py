from django.contrib import messages
from django.shortcuts import redirect
def isValidation(request, path, message):
    if message:
        messages.warning(request, message)
    if not request.user.is_authenticated:
        return redirect(path)