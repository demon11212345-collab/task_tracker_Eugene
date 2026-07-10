from django.core.exceptions import PermissionDenied
import time
class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.creator != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class StatusMixin:
    def mark_done(self):
        self.status = "Виконано"

    def mark_in_progress(self):
        self.status = "В процесі"