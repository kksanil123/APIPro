import json
from utilities.logger import Loggen
import pytest
from utilities import readproperties as rp
import requests
from assertpy import assert_that


@pytest.fixture()
def prepare_request():
    f = open('TestData/post_data_res.txt', "r")
    json_data = json.loads(f.read())
    end_point = f'/v2/pet/{json_data["id"]}'
    return [rp.prod_service_url + end_point, json_data]



def test_get_request(prepare_request):
    Loggen.give_logger().log(20, '**** Get Request Test Started *****')
    req, exp_res = prepare_request
    header = {'accept': 'application/json'}
    res = requests.get(url=req, headers=header)
    with open(r'TestData/get_data_res.txt','w+') as f:
        f.writelines(str(res.content).strip('b\''))
    res.close()
    print(res.content)
    assert_that(res.json()).is_equal_to(exp_res)
    Loggen.give_logger().log(20, '**** Get Request Test Finished ****')

