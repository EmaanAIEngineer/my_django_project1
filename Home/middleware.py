import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Get session ID
        session_id = request.session.session_key

        # If session not created yet
        if not session_id:
            request.session.save()
            session_id = request.session.session_key

        # Get user
        if request.user.is_authenticated:
            user = request.user.username
            is_auth = True
        else:
            user = "Anonymous"
            is_auth = False

        # Get IP
        ip = self.get_client_ip(request)

        # URL
        url = request.path

        # Log everything
        logger.info(
            f"SessionID: {session_id} | User: {user} | IP: {ip} | URL: {url} | Authenticated: {is_auth}"
        )

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')