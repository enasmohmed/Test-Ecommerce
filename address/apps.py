from django.utils.translation import gettext_lazy as _

from oscar.core.application import OscarConfig


class AddressConfig(OscarConfig):
    label = 'address'
    name = 'address'
    verbose_name = _('Address')
