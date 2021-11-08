def isAuthenticated(request):
    if request.user.is_authenticated:
        return True
    return False