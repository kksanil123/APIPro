from assertpy import assert_that
from utilities import logger
import pytest
import requests
import json
from utilities import readproperties as rp


@pytest.fixture()
def param():
    f = open('TestData/post_data_res.txt')
    f1 = json.load(f)
    id = f1['id']
    f.close()
    return id


def test_delete_data(param):
    url = rp.prod_service_url + '/v2/pet/' + str(param)
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    logger.Loggen().give_logger().log(20, '**** Delete Request Test Started *****')
    res = requests.delete(url, headers=header)
    print(res.content)
    assert_that(res.status_code).is_equal_to(200)
    logger.Loggen().give_logger().log(20, '**** Delete Request Test Finished *****')
