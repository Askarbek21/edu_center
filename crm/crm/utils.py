def is_owner(request,view):
    obj = view.get_object()
    return request.user == obj.user