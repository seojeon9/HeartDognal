from kafka import KafkaProducer

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        print(request)
        response = self.get_response(request)
        return response
