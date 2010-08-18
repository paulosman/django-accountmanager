class StatusHeader(object):

    def process_response(self, request, response):
        if not request.user.is_authenticated():
            response['X-Account-Management-Status'] = 'none'
            return response
        status = 'active; id="%(username)s"; name="%(name)s"' % {
            'username': request.user.username,
            'name': request.user.get_full_name()
        }
        response['X-Account-Management-Status'] = status
        return response
