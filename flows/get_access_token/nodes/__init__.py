# coding: utf-8

from arkfbp.nodes import APINode, FunctionNode
import settings


class GetAccessTokenNode(APINode):

    url = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/'

    method = 'POST'

    headers = {
        'content-type': 'application/json',
    }

    params = {
        'app_id': settings.APP_ID,
        'app_secret': settings.APP_SECRET,
    }


class ProcessNode(FunctionNode):

    def run(self):
        data = self.inputs
        return data.get('app_access_token')