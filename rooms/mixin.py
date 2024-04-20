from users import mixin as users_mixin
from django.http import Http404


class BelongsOnlyView(users_mixin.LoginOnlyView):
    def get_object(self, queryset=None):
        room = super().get_object(queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404("You can Not edit this page")
        return room
