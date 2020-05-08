# coding: utf-8

from arkfbp.nodes import APINode, FunctionNode
import settings


class GetTenantAccessTokenNode(APINode):

    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'

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
        return data.get('tenant_access_token')