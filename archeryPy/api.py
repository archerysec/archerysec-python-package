#!/usr/bin/env python

__author__ = "wensaus (https://github.com/wensaus)"
__contributors__ = ["wensaus"]
__status__ = "Production"
__license__ = "MIT"

import requests
import json


class ArcheryRestApi(object):
    def __init__(self, host):

        self.host = host

    def archery_auth(self, username, password):
        """
        Get the auth token.
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json'}
            data = {"username": username, "password": password}
            res = requests.post(url=f'{self.host}/api/auth/token/',
                                data=json.dumps(data), headers=headers)
            return {
                "token": res.json()['access'],
                "refresh": res.json()['refresh'],
            }
        except requests.exceptions as e:
            raise e

    def archery_auth_refresh(self, refresh):
        """
        Get the  refresh auth token.
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json'}
            data = {"refresh": refresh}
            res = requests.post(
                url=f'{self.host}/api/auth/token/refresh/', headers=headers, data=json.dumps(data))
            return {
                "token": res.json()['access']
            }
        except requests.exceptions as e:
            raise e

    def archery_auth_verify(self, auth_token):
        """
        Get the  verify auth token.
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json'}
            data = {"token": auth_token}
            res = requests.post(
                url=f'{self.host}/api/auth/token/verify/', headers=headers, data=json.dumps(data))
            return {
                "status": res.status_code
            }
        except requests.exceptions as e:
            raise e

    def archery_workflow_list(self, auth_token, params):
        """
        List all workflow orders (filtered, paginated)
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'Bearer {auth_token}'}
            res = requests.get(
                url=f'{self.host}/api/v1/workflow/', headers=headers, params=params)
            return {"data": res.json()}
        except requests.exceptions as e:
            raise e

    def archery_workflow_submit(self, auth_token, data):
        """
        Submit workflow orders
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'Bearer {auth_token}'}
            res = requests.post(
                url=f'{self.host}/api/v1/workflow/', headers=headers, data=json.dumps(data))
            return {"data": res.json()}
        except requests.exceptions as e:
            raise e

    def archery_workflow_audit(self, auth_token, data):
        """
        audit workflow orders
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'Bearer {auth_token}'}
            res = requests.post(
                url=f'{self.host}/api/v1/workflow/audit/', headers=headers, data=json.dumps(data))
            return {"data": res.json()}
        except requests.exceptions as e:
            raise e

    def archery_workflow_auditlist(self, auth_token, data):
        """
        auditlist workflow orders
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'Bearer {auth_token}'}
            res = requests.post(
                url=f'{self.host}/api/v1/workflow/auditlist/', headers=headers, data=json.dumps(data))
            return {"data": res.json()}
        except requests.exceptions as e:
            raise e

    def archery_workflow_execute(self, auth_token, data):
        """
        execute workflow orders
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'Bearer {auth_token}'}
            res = requests.post(
                url=f'{self.host}/api/v1/workflow/execute/', headers=headers, data=json.dumps(data))
            return {"data": res.json()}
        except requests.exceptions as e:
            raise e

    def archery_workflow_log(self, auth_token, data):
        """
        execute workflow orders
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'Bearer {auth_token}'}
            res = requests.post(
                url=f'{self.host}/api/v1/workflow/log/', headers=headers, data=json.dumps(data))
            return {"data": res.json()}
        except requests.exceptions as e:
            raise e

    def archery_workflow_sqlcheck(self, auth_token, data):
        """
        sqlcheck workflow orders
        :return:
        """
        try:
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'Bearer {auth_token}'}
            res = requests.post(
                url=f'{self.host}/api/v1/workflow/sqlcheck/', headers=headers, data=json.dumps(data))
            return {"data": res.json()}
        except requests.exceptions as e:
            raise e
