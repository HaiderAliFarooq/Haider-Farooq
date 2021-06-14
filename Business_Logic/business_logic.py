# --------------------------------------------------------------------------- #
# This class contains the implementation of Business Logic and API calls      #
# --------------------------------------------------------------------------- #

import json
from API_Framework.Common import Utils


class BusinessLogic:

    obj_utils = Utils()
    header_dict = {}
    base_url = ''

    def __init__(self):

        self.base_url = self.obj_utils.read_config()
        self.header_dict = {'Content-Type': 'application/json'}

    def call_api_playground_endpoints(self, pstr_endpoint, pstr_method, pint_id=None, pint_limit=None, pstr_type=None):
        # e.g URL: http://localhost:3030/products
        # e.g URL: http://localhost:3030/products/1234
        try:
            str_request_url = self.obj_utils.create_url(pstr_endpoint)

            if pint_id is not None:
                str_request_url = str_request_url + '/' + str(pint_id)

            if pint_limit is not None:
                str_request_url = str_request_url + '?$limit=' + str(pint_limit)

            if pstr_type is not None:
                str_request_url = str_request_url + '?type=' + pstr_type

            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict)
            return response
        except Exception as e:
            return "Exception Occurred in call_products_endpoints(....): " + str(e)

    def add_product(self, pstr_endpoint, pstr_method, pstr_name, pstr_type, pstr_price, pstr_shipping,
                    pstr_manufacturer):
        try:
            payload = self.obj_utils.read_json("add_product_payload.json")

            payload['name'] = pstr_name
            payload['type'] = pstr_type
            payload['price'] = pstr_price
            payload['shipping'] = pstr_shipping
            payload['manufacturer'] = pstr_manufacturer

            str_request_url = self.obj_utils.create_url(pstr_endpoint)

            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict, json=payload)
            return response
        except Exception as e:
            return "Exception Occurred in adding products method(....): " + str(e)

    def edit_product(self, pstr_endpoint, pstr_method, pint_id, pstr_name, pstr_type, pstr_price, pstr_shipping,
                     pstr_manufacturer):
        try:
            obj_response = self.call_api_playground_endpoints('Products', 'GET', pint_id=pint_id)
            payload = json.loads(obj_response.content)

            if pstr_name is not None:
                payload['name'] = pstr_name
            if pstr_type is not None:
                payload['type'] = pstr_type
            if pstr_price is not None:
                payload['price'] = pstr_price
            if pstr_shipping is not None:
                payload['shipping'] = pstr_shipping
            if pstr_manufacturer is not None:
                payload['manufacturer'] = pstr_manufacturer

            str_request_url = self.obj_utils.create_url(pstr_endpoint) + '/' + str(pint_id)
            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict, json=payload)
            return response
        except Exception as e:
            return "Exception Occurred in editing products method(....): " + str(e)

    def add_store(self, pstr_endpoint, pstr_method, pstr_name, pstr_type, pstr_address, pstr_address2,
                    pstr_city, pstr_state, pstr_zip, pint_lat, pint_long, pstr_hours):
        try:
            payload = self.obj_utils.read_json("add_store_payload.json")
            payload['name'] = pstr_name
            payload['type'] = pstr_type
            payload['address'] = pstr_address
            payload['address2'] = pstr_address2
            payload['city'] = pstr_city
            payload['state'] = pstr_state
            payload['zip'] = pstr_zip
            payload['lat'] = pint_lat
            payload['lng'] = pint_long
            payload['hours'] = pstr_hours
            str_request_url = self.obj_utils.create_url(pstr_endpoint)
            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict, json=payload)
            return response
        except Exception as e:
            return "Exception Occurred in adding stores method(....): " + str(e)

    def edit_store(self, pstr_endpoint, pstr_method, pint_id, pstr_name, pstr_type, pstr_address, pstr_address2,
                   pstr_city, pstr_state, pstr_zip, pint_lat, pint_long, pstr_hours):
        try:
            obj_response = self.call_api_playground_endpoints('Stores', 'GET', pint_id=pint_id)
            payload = json.loads(obj_response.content)

            if pstr_name is not None:
                payload['name'] = pstr_name
            if pstr_type is not None:
                payload['type'] = pstr_type
            if pstr_address is not None:
                payload['price'] = pstr_address
            if pstr_address2 is not None:
                payload['shipping'] = pstr_address2
            if pstr_city is not None:
                payload['manufacturer'] = pstr_city
            if pstr_state is not None:
                payload['state'] = pstr_state
            if pstr_zip is not None:
                payload['zip'] = pstr_zip
            if pint_lat is not None:
                payload['lat'] = pint_lat
            if pint_long is not None:
                payload['lng'] = pint_long
            if pstr_hours is not None:
                payload['hours'] = pstr_hours

            str_request_url = self.obj_utils.create_url(pstr_endpoint) + '/' + str(pint_id)
            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict, json=payload)
            return response
        except Exception as e:
            return "Exception Occurred in editing stores method(....): " + str(e)

    def add_services(self, pstr_endpoint, pstr_method, pstr_name):
        try:
            payload = self.obj_utils.read_json("add_services_payload.json")
            payload['name'] = pstr_name

            str_request_url = self.obj_utils.create_url(pstr_endpoint)
            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict, json=payload)
            return response
        except Exception as e:
            return "Exception Occurred in adding services method(....): " + str(e)

    def edit_services(self, pstr_endpoint, pstr_method, pint_id, pstr_name):
        try:
            obj_response = self.call_api_playground_endpoints('Stores', 'GET', pint_id=pint_id)
            payload = json.loads(obj_response.content)

            if pstr_name is not None:
                payload['name'] = pstr_name

            str_request_url = self.obj_utils.create_url(pstr_endpoint) + '/' + str(pint_id)
            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict, json=payload)
            return response
        except Exception as e:
            return "Exception Occurred in editing services method(....): " + str(e)

    def add_categories(self, pstr_endpoint, pstr_method, pstr_name, pstr_id):
        try:
            payload = self.obj_utils.read_json("add_categories_payload.json")
            payload['name'] = pstr_name
            payload['id'] = pstr_id

            str_request_url = self.obj_utils.create_url(pstr_endpoint)
            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict, json=payload)
            return response
        except Exception as e:
            return "Exception Occurred in adding categories method(....): " + str(e)

    def edit_categories(self, pstr_endpoint, pstr_method, pstr_name, pint_id):
        try:
            obj_response = self.call_api_playground_endpoints('Categories', 'GET', pint_id=pint_id)
            payload = json.loads(obj_response.content)

            if pstr_name is not None:
                payload['name'] = pstr_name

            str_request_url = self.obj_utils.create_url(pstr_endpoint) + '/' + pint_id
            response = self.obj_utils.call_request(pstr_method, str_request_url, self.header_dict, json=payload)
            return response
        except Exception as e:
            return "Exception Occurred in edit categories method(....): " + str(e)