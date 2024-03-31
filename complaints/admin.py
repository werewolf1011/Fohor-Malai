from django.contrib import admin
from django.utils.html import format_html

from .models import Complaints


class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "complainer_name",
        "complainer_address",
        "complainer_phone",
        "waste_type",
        "complaint_desc",
        "complain_status",
        "created_at",
        "modified_at",
        "image",
        "image_tag",
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="auto" height="150px" />'.format(obj.image.url))
        else:
            return "No Image"

    list_filter = (
        "complain_status",
        "created_at",
        "modified_at",
    )

    ordering = (
        "-created_at",
        "-modified_at",
    )

    search_fields = (
        "complainer_name",
        "complainer_address",
        "complainer_phone",
        "waste_type",
        "complaint_desc",
    )

    def has_change_permission(self, request, obj=None):
        # Allow change permission only if the user is an admin
        if request.user.is_superuser:
            return True
        # For staff members, check if they have permission and return accordingly
        if request.user.is_staff and request.user.has_perm("complaints.change_complaints"):
            return True
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If editing an existing object
            # Allow changing only the complain_status field for staff members
            if not request.user.is_superuser and request.user.is_staff:
                return [
                    field.name
                    for field in self.model._meta.fields
                    if field.name != "complain_status"
                ]
        # If creating a new object or admin editing, no fields will be read-only
        return []


admin.site.register(Complaints, ComplaintAdmin)
