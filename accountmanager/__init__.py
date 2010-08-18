from django.conf import settings

import wellknown
from xrd import Link

amcd_href = getattr(settings, 'MOZILLA_AMCD_HREF', '/meta/amcd.json')

# add rel=acct-mgmt Link element to host-meta XRD
hostmeta = wellknown.get_hostmeta()
hostmeta.links.append(Link(
    rel='http://services.mozilla.com/amcd/0.1', href=amcd_href))
