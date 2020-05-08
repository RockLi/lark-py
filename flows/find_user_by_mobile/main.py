from arkfbp.flow import Flow
from arkfbp.graph import Graph

from flows.find_user_by_mobile.nodes import RunGetTenantAccessTokenFlowNode, GetUserNode, ProcessNode


class Main(Flow):

    def create_graph(self):
        g = Graph()
        g.add(
            {
                'cls': RunGetTenantAccessTokenFlowNode,
                'id': 1,
                'next': 2,
            }).add({
                'cls': GetUserNode,
                'id': 2,
                'next': 3,
            }).add({
                'cls': ProcessNode,
                'id': 3,
            })

        return g


if __name__ == '__main__':
    flow = Main()
    outputs = flow.main({
        'mobile': ['18600014356', '18945815579'],
    })
    print(outputs)
