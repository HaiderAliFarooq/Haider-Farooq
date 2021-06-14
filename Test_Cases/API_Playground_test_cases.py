# --------------------------------------------------------------------------- #
# This class contains the test cases for API Playground API                   #
# --------------------------------------------------------------------------- #

import json
import random
from Business_Logic.business_logic import BusinessLogic


# Test Case 1: Get all products
def test_products_all():
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Products', 'GET')

    assert obj_response.status_code == 200


# Test Case 2: Get specific product
def test_products_specific():
    int_product_id = 9132294
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Products', 'GET', int_product_id)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == int_product_id


# Test Case 3: Delete specific product
def test_products_delete():
    str_name = 'test product delete'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.add_product('Products', 'POST', str_name, 'test-product-type',
                                                  500, 7, 'Honda')
    assert obj_response.status_code == 201
    int_id = json.loads(obj_response.content)['id']
    obj_response = obj_business_logic.call_api_playground_endpoints('Products', 'DELETE', int_id)

    assert obj_response.status_code == 200
    obj_response = obj_business_logic.call_api_playground_endpoints('Products', 'GET', int_id)
    assert obj_response.status_code == 404


# Test Case 4: Verify limit parameter for products - maximum limit is allowed only for 25 records
def test_products_limit_pass():
    int_limit = 25
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Products', 'GET', pint_limit=int_limit)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['limit'] == int_limit


# Test Case 5:Verify if limit works fine above 25. The value 25 is verified in the last assertion as hard code
# because limit is always max at 25. So even if we give value above 25, limit returns as 25.
def test_products_limit_fail():
    int_limit = 26
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Products', 'GET', pint_limit = int_limit)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['limit'] == 25


# Test Case 6: Verify product addition
def test_products_add():
    pstr_name = 'test-prodcut1'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.add_product('Products', 'POST', pstr_name, 'test-product-type',
                                                  500, 7, 'Honda')

    assert obj_response.status_code == 201
    assert json.loads(obj_response.content)['id'] is not None
    assert json.loads(obj_response.content)['name'] == pstr_name
    int_id= json.loads(obj_response.content)['id']
    obj_response = obj_business_logic.call_api_playground_endpoints('Products', 'DELETE', int_id)
    assert obj_response.status_code == 200


# Test Case 7: Verify product edit
def test_products_edit():
    pint_id = 48530
    pstr_name = 'test-prodcut100000'

    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.edit_product('Products', 'PATCH', pint_id, pstr_name, 'test-product-type 123',
                                                   500, 7, 'Honda123')

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == pint_id
    assert json.loads(obj_response.content)['name'] == pstr_name


# Test Case 8 - Verify if querying the data works for products
def test_products_select_type():
    pstr_type = 'HardGood'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Products', 'GET', pstr_type=pstr_type)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['data'][0]['type'] == pstr_type


# Test cases for testing stores endpoint
# Test Case 1: Get all stores
def test_stores_all():
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Stores', 'GET')

    assert obj_response.status_code == 200


# Test Case 2: Get specific store
def test_stores_specific():
    int_store_id = 20
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Stores', 'GET', int_store_id)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == int_store_id


# Test Case 3: Verify store addition
def test_store_add():
    pstr_name = 'test-store007'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.add_store('Stores', 'POST', pstr_name, 'test-store-type',
                                                'shop number 007', 'ground floor', 'Hopkins', 'MN', '55305',
                                                44.45, 90.01, "Mon: 10-9; Tue: 10-9; Wed: 10-9; Thurs: 10-9; Fri:10-9; "
                                                "Sat: 10-9; Sun: 10-8")

    assert obj_response.status_code == 201
    assert json.loads(obj_response.content)['id'] is not None
    assert json.loads(obj_response.content)['name'] == pstr_name
    int_store_id = json.loads(obj_response.content)['id']
    obj_response = obj_business_logic.call_api_playground_endpoints('Stores', 'DELETE', int_store_id)
    assert obj_response.status_code == 200


# Test Case 4: Verify store editing
def test_store_edit():
    pint_id = 8924
    pstr_name = 'test-store100000'

    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.edit_store('Stores', 'PATCH', pint_id, pstr_name, 'test-store_type 123',
                                                   'shop number 007 m', '1st floor', 'Yorkshire', None, None, None,
                                                 None, None)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == pint_id
    assert json.loads(obj_response.content)['name'] == pstr_name


# Test Case 5: Delete specific store
def test_stores_delete():
    str_name = 'test-store007'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.add_store('Stores', 'POST', str_name, 'test-store-type',
                                                'shop number 007', 'ground floor', 'Hopkins', 'MN', '55305',
                                                44.45, 90.01, "Mon: 10-9; Tue: 10-9; Wed: 10-9; Thurs: 10-9; Fri:10-9; "
                                                "Sat: 10-9; Sun: 10-8")
    assert obj_response.status_code == 201

    int_store_id = json.loads(obj_response.content)['id']
    obj_response = obj_business_logic.call_api_playground_endpoints('Stores', 'DELETE', int_store_id)
    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == int_store_id
    obj_response = obj_business_logic.call_api_playground_endpoints('Stores', 'GET', int_store_id)
    assert obj_response.status_code == 404


# Test Case 6: Verify limit parameter for stores
def test_stores_limit():
    int_limit = 24
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Stores', 'GET', pint_limit=int_limit)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['limit'] == int_limit


# Test Services endpoint
# Test Case 1: Get all services
def test_services_all():
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Services', 'GET')

    assert obj_response.status_code == 200


# Test Case 2: Get specific services
def test_services_specific():
    int_product_id = 14
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Services', 'GET', int_product_id)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == int_product_id


# Test Case 3: Verify services addition
def test_services_addition():
    pstr_name = 'Testing at doorstep'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.add_services('Services', 'POST', pstr_name)

    assert obj_response.status_code == 201
    assert json.loads(obj_response.content)['id'] is not None
    assert json.loads(obj_response.content)['name'] == pstr_name
    int_services_id = json.loads(obj_response.content)['id']
    obj_response = obj_business_logic.call_api_playground_endpoints('Services', 'DELETE', int_services_id)
    assert obj_response.status_code == 200

# Test Case 4: Verify services editing
def test_services_editing():
    pint_id = 14
    pstr_name = 'Testing at Doorstep with minimum discount'

    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.edit_services('Services', 'PATCH', pint_id, pstr_name)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == pint_id
    assert json.loads(obj_response.content)['name'] == pstr_name


# Test Case 5: Delete specific services
def test_services_delete():
    pstr_name = 'Testing at doorstep'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.add_services('Services', 'POST', pstr_name)
    assert obj_response.status_code == 201

    int_services_id = json.loads(obj_response.content)['id']
    obj_response = obj_business_logic.call_api_playground_endpoints('Services', 'DELETE', int_services_id)

    assert obj_response.status_code == 200
    obj_response = obj_business_logic.call_api_playground_endpoints('Services', 'GET', int_services_id)
    assert obj_response.status_code == 404


# Test Case 6: Verify limit parameter for services
def test_services_limit():
    int_limit = 20
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Services', 'GET', pint_limit=int_limit)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['limit'] == int_limit


# Testcases for testing the category endpoint
# Test Case 1: Get all categories
def test_categories_all():
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Categories', 'GET')

    assert obj_response.status_code == 200


# Test Case 2: Verify categories addition
def test_categories_addition():
    pstr_name = 'Medicine'
    pstr_id = '002'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.add_categories('Categories', 'POST', pstr_name, pstr_id)

    assert obj_response.status_code == 201
    assert json.loads(obj_response.content)['id'] == pstr_id
    assert json.loads(obj_response.content)['name'] == pstr_name
    obj_response = obj_business_logic.call_api_playground_endpoints('Categories', 'DELETE', pstr_id)
    assert obj_response.status_code == 200


# Test Case 3: Get specific categories
def test_categories_get_specific():
    str_product_id = 'abcat0010000'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Categories', 'GET', str_product_id)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == str_product_id


# Test Case 4: Verify categories editing
def test_categories_editing():
    str_product_id = 'abcat0010000'
    pstr_name = random.choice(['Science', 'Biology', 'Physics'])

    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.edit_categories('Categories', 'PATCH', pstr_name, str_product_id)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['id'] == str_product_id
    assert json.loads(obj_response.content)['name'] == pstr_name


# Test Case 5: Delete specific categories
def test_categories_deletion():
    pstr_name = 'Medicine'
    pstr_id = '005'
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.add_categories('Categories', 'POST', pstr_name, pstr_id)
    assert obj_response.status_code == 201

    obj_response = obj_business_logic.call_api_playground_endpoints('Categories', 'DELETE', pstr_id)
    assert obj_response.status_code == 200
    obj_response = obj_business_logic.call_api_playground_endpoints('Categories', 'GET', pstr_id)
    assert obj_response.status_code == 404


# Test Case 6: Verify limit parameter for services
def test_services_limit():
    int_limit = 25
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Stores', 'GET', pint_limit=int_limit)

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['limit'] == int_limit


# Testcases for verifying the utilities (API version and its health)
# Testcase for verifying the API version endpoint
def test_api_version():
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Version', 'GET')

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['version'] is not None


# Test case to verify that the health of API is green
def test_api_healthcheck():
    obj_business_logic = BusinessLogic()
    obj_response = obj_business_logic.call_api_playground_endpoints('Health', 'GET')

    assert obj_response.status_code == 200
    assert json.loads(obj_response.content)['uptime'] is not None
