from hdfs import InsecureClient

def get_client():
    return InsecureClient('http://localhost:9870', user='big')