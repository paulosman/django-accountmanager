from django.conf import settings
from django.core.urlresolvers import reverse

import wellknown
from xrd import Link

# add rel=acct-mgmt Link element to host-meta XRD
amcd_path = reverse('accountmanager.views.amcd')
hostmeta = wellknown.get_hostmeta()
hostmeta.links.append(Link(
    rel='http://services.mozilla.com/amcd/0.1', href=amcd_path))
