from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
from infra.hdfs_client import get_client
from infra.jdbc import DataWarehouse, find_data

class DogKindExtractor:
    file_dir = '/roadpet/dog/kind'

    @classmethod
    def extract_data(cls):
        