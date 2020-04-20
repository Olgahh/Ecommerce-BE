from rest_framework.permissions import BasePermission

class IsStaffOrOwner(BasePermission):
	message = "You must be the owner of this order"
	def has_object_permission(self, request, view, object):
		return (request.user.is_staff) or (object.profile.user == request.user)
			