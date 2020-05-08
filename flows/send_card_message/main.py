# coding: utf-8

from arkfbp.flow import Flow
from arkfbp.graph import Graph


from flows.send_card_message.nodes import (
    RunGetTenantAccessTokenFlowNode,
    RunGetFindUserByMobilesFlowNode,
    SendCardMessageNode,
    StoreTokenNode,
)


class Main(Flow):

    def create_graph(self):
        g = Graph()
        g.add({
            'cls': RunGetTenantAccessTokenFlowNode,
            'id': 1,
            'next': 2,
        })

        g.add({
            'cls': StoreTokenNode,
            'id': 2,
            'next': 3,
        })

        g.add({
            'cls': RunGetFindUserByMobilesFlowNode,
            'id': 3,
            'next': 4,
        })

        g.add({
            'cls': SendCardMessageNode,
            'id': 4,
        })

        return g

