#!/usr/bin/env python
# coding: utf-8

""" JSON and XML compare """

import os
import json
import requests
import xmltodict
from xml.etree import ElementTree
from pprint import pprint as _pprint
from requests.auth import HTTPBasicAuth

LOGIN_URL = 'https://python-for-qa.herokuapp.com/login'
DATA_URL = 'https://python-for-qa.herokuapp.com/data'

JSON_FILE = 'data.json'
XML_FILE = 'data.xml'


def load_data():
    """ Grab xml and json """
    login_request = requests.get(LOGIN_URL, auth=HTTPBasicAuth("admin", "password"))
    login_response_data = json.loads(login_request.content)
    auth_headers = {"X-AUTH-TOKEN" : login_response_data['token']}
    # json is default
    json_data_response = requests.get(DATA_URL, headers=auth_headers)
    with open(JSON_FILE, 'a') as json_file:
        json_file.write(json_data_response.content)
    auth_headers['Accept'] = 'application/xml'
    xml_data_response = requests.get(DATA_URL, headers=auth_headers)
    with open(XML_FILE, 'a') as xml_file:
        xml_file.write(xml_data_response.content)

def main():
    if not os.path.exists(JSON_FILE) or not os.path.exists(XML_FILE):
        load_data()
    else:
        with open(XML_FILE, 'rt') as xml_file:
            data = xml_file.read()
            xml_data  = xmltodict.parse(data)
        json_data = json.loads(open(JSON_FILE, 'r').read())
        for item in json_data:
            print item['_id']
            raw_input()

if __name__ == "__main__":
    main()

