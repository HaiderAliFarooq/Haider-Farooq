# --------------------------------------------------------------------------- #
# This class contains the generic utils which can be used for any API testing #
# --------------------------------------------------------------------------- #

import requests
import yaml
import os
import json


class Utils:

    def call_request(self, pstr_method, pstr_url, pdict_headers, **kwargs):
        """
        Description:
            |  This method allow users to create call requests

        """
        try:
            if pstr_url == "":
                return "URL can't be Null"

            pstr_json = kwargs.get('json', None)
            pstr_payload = kwargs.get('payload', None)

            if pstr_method.capitalize() == "Get":
                response = requests.get(pstr_url, headers=pdict_headers, data=pstr_payload)

            elif pstr_method.capitalize() == "Post":
                response = requests.post(pstr_url, headers=pdict_headers, data=pstr_payload, json=pstr_json)

            elif pstr_method.capitalize() == "Patch":
                if pstr_payload is not None or pstr_json is not None:
                    response = requests.patch(pstr_url, headers=pdict_headers, data=pstr_payload, json=pstr_json)
                else:
                    return "Please provide payload"

            elif pstr_method.capitalize() == "Delete":
                response = requests.delete(pstr_url, headers=pdict_headers, data=pstr_payload,
                                           json=pstr_json)
            else:
                return "Request Method is not valid"

            return response
        except Exception as e:
            return "Exception Occurred in call_request(....): " + str(e)

    def read_config(self):
        try:
            str_config_file_path = os.path.abspath(os.pardir) + r"\Config.yml"
            with open(str_config_file_path, 'r') as config_yml:
                config = yaml.load(config_yml)

            str_base_url = config['base_url']
            return str_base_url
        except Exception as e:
            return "Exception Occurred in read_config(....): " + str(e)

    def read_json(self, pstr_filename):
        try:
            str_file_path = os.path.abspath(os.pardir) + "\PayLoad\\" + pstr_filename
            with open(str_file_path) as obj_data_file:
                json_data = json.load(obj_data_file)

            return json_data
        except Exception as e:
            return "Exception Occurred in read_json(....): " + str(e)

    def create_url(self, pstr_name):
        try:
            base_url = self.read_config()
            str_service_file_path = os.path.abspath(os.pardir) + r"\service_description.yml"
            with open(str_service_file_path, 'r') as service_yml:
                config = yaml.load(service_yml)

            str_request_url = base_url + config[pstr_name]['endpoint']
            return str_request_url
        except Exception as e:
            return "Exception Occurred in create_url(....): " + str(e)
