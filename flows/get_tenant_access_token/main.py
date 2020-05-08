from arkfbp.flow import Flow
from arkfbp.graph import Graph


from flows.get_tenant_access_token.nodes import GetTenantAccessTokenNode, ProcessNode


class Main(Flow):

    def create_graph(self):
        g = Graph()
        g.add(
            {
                'cls': GetTenantAccessTokenNode,
                'id': 1,
                'next': 2,
            }).add(
            {
                'cls': ProcessNode,
                'id': 2,
            }
        )

        return g


if __name__ == '__main__':
    flow = Main()
    outputs = flow.main()
    print(outputs)
