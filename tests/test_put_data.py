from assertpy import assert_that
import requests
import json
import pytest
from utilities import readproperties as rp
from utilities import logger


@pytest.fixture()
def req_body():
    f = open(r'TestData/post_data_res.txt')
    fp1 = json.load(f)
    f.close()
    id = fp1['id']
    data = {
        "id": id,
        "category": {
            "id": 0,
            "name": f"UPDATED_NAME_Testing_pet_{id}"
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
    body = json.dumps(data)
    return body


def test_put_data(req_body):
    url = rp.prod_service_url + '/v2/pet'
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    logger.Loggen().give_logger().log(20,'**** PUT Request Test Started *****')
    res = requests.put(url, data=req_body, headers=header)

    with open('TestData/put_data_res.txt', 'w') as f:
        f.writelines(str(res.content).strip('b\''))

    print(res.content)
    assert_that(res.json()).is_equal_to(json.loads(req_body))
    logger.Loggen().give_logger().log(20, '**** PUT Request Test Finished *****')

