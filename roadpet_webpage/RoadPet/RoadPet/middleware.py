from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
import datetime as dt
import time

class LogMiddleware:

    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        param_json =  dict(request.GET.lists()) if request.method == 'GET' else dict(request.POST.lists())

        # views.py 호출 이전에 실행 될 코드
        log_dict = {
            'ip' : request.META['REMOTE_ADDR'],
            'user': str(request.user),
            'http_method': request.method,
            'url': request.path,
            'parameter': param_json,
            'timestamp': int(time.time()),
            'session_id':'None',
        }

        if request.session.keys():
            log_dict['session_id'] = request.session.session_key

        print(log_dict)

        self.producer.send('heartdognal-log', log_dict)


        response = self.get_response(request)

        # views.py 호출 이후 실행 될 코드
        return response
