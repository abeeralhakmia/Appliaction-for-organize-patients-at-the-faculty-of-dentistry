from django.contrib.auth.mixins import UserPassesTestMixin


class IsDonor(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "You must be a donor to perform this action."

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        return self.request.user.is_donor


class IsNurse(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "You must be a nurse to perform this action."

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        return self.request.user.is_nurse
