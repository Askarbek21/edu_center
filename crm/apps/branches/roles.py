from rest_framework_roles.roles import is_user, is_anon, is_admin


def is_student(request, view):
    return all(is_user(request, view),request.user.role == 'Student')

def is_teacher(request, view):
    return all(is_user(request, view),request.user.role == 'Teacher')


ROLES = {
    # Django out-of-the-box
    'admin': is_admin,
    'user': is_user,
    'anon': is_anon,
    # Some custom role examples
    'student': is_student,
    'teacher': is_teacher,
}