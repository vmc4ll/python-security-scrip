

import requests
from bs4 import BeautifulSoup


target_url = "http://xss.is/login"  
csrf_token_name = "csrf_token"  
test_cases = [
    {"param1": "value1", "param2": "value2"},

]

session = requests.Session()

def get_csrf_token():
    response = session.get(target_url)
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": csrf_token_name})["value"]
    return csrf_token


def send_csrf_request(url, payload):
    response = session.post(url, data=payload)
    
    print("Response:", response.status_code)
    print("Response Content:", response.text)
 
def csrf_test():

    csrf_token = get_csrf_token()

    for test_case in test_cases:
      
        test_case[csrf_token_name] = csrf_token

    
        send_csrf_request(target_url, test_case)


csrf_test()

