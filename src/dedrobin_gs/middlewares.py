class OrderCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Implement SQL query to all orders
        # request.orders = 10
        response = self.get_response(request)

        return response
