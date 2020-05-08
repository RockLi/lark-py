# coding: utf-8

from arkfbp.nodes import TriggerFlowNode, APINode, FunctionNode


class RunGetTenantAccessTokenFlowNode(TriggerFlowNode):

    flowname = 'get_tenant_access_token'


class GetUserNode(APINode):

    url = 'https://open.feishu.cn/open-apis/user/v1/batch_get_id'

    method = 'GET'

    def get_headers(self):
        return {
            'Authorization': 'Bearer ' + self.inputs
        }

    def get_params(self):
        return {
            'mobiles': self.flow.inputs['mobile'],
        }


class ProcessNode(FunctionNode):

    def run(self):
        data = self.inputs
        return data['data']['mobile_users']

