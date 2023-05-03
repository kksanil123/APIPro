from assertpy import assert_that
import pytest
from utilities import readproperties as rp
import requests
import json
import random
from utilities.logger import Loggen


@pytest.fixture()
def prepare_request():
    end_point = '/v2/pet'
    return rp.prod_service_url + end_point


@pytest.fixture()
def req_body():
    # f = open('TestData/post_data.json')
    id = random.randint(20, 100)
    f = {
        "id": id,
        "category": {
            "id": 0,
            "name": f"Testing_pet_{id}"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    json_data = json.dumps(f)
    return json_data


def test_post_request(prepare_request, req_body):
    Loggen.give_logger().log(20, '**** Post Request Test Started *****')
    header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    res = requests.post(url=prepare_request, data=req_body, headers=header)
    with open('TestData/post_data_res.txt', mode='w') as f1:
        f1.writelines(str(res.content).strip('b\''))

    print(res.json())
    res.close()
    assert_that(res.json()).is_equal_to(json.loads(req_body))
    Loggen.give_logger().log(20, '**** Post Request Test Finished ****')

