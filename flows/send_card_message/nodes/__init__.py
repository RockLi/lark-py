# coding: utf-8

from arkfbp.nodes import TriggerFlowNode, APINode, FunctionNode


class RunGetTenantAccessTokenFlowNode(TriggerFlowNode):

    flowname = 'get_tenant_access_token'


class StoreTokenNode(FunctionNode):

    def run(self):
        self.state.update({
            'token': self.inputs,
        })


class RunGetFindUserByMobilesFlowNode(TriggerFlowNode):

    flowname = 'find_user_by_mobile'

    def get_inputs(self):
        return {
            'mobile': [self.flow.inputs['mobile']],
        }


class SendCardMessageNode(APINode):

    url = 'https://open.feishu.cn/open-apis/message/v4/send/'
    method = 'POST'

    def get_headers(self):
        return {
            'Authorization': 'Bearer ' + self.state.get('token')
        }

    def get_params(self):
        data = self.inputs
        user_info = data[self.flow.inputs['mobile']][0]

        return {
            "user_id": user_info['user_id'],
            "msg_type": "interactive",
            "update_multi": False,
            "card": {
                "config": {
                    "wide_screen_mode": True,
                },
                "header": {
                    "title": {
                        "tag": "plain_text",
                        "content": "消息卡片的标题",
                    }
                },
                "elements": [
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": "消息卡片的内容\n很长很长的内容"
                        }
                    },
                    {
                        "tag": "hr",
                    },
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": "[附件1](https://cdn.futurelabedu.com/futurelabs/1540435182000.pdf)\n[附件2](http://yanjiusuo.dev.attackt.com/static/schooladmin/default.xlsx)",
                        },
                    },
                    {
                        "tag": "action",
                        "actions": [
                            {
                                "tag": "button",
                                "text": {
                                    "tag": "plain_text",
                                    "content": "拒绝"
                                },
                                "url": "http://c4.dev.attackt.com/deny",
                                "type": "default"
                            },
                            {
                                "tag": "button",
                                "text": {
                                    "tag": "plain_text",
                                    "content": "同意"
                                },
                                "url": "http://c4.dev.attackt.com/accept",
                                "type": "primary"
                            },
                        ]
                    }
                ]
            }
        }
