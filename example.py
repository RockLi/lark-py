from flows.send_card_message.main import Main as SendCardMessageFlow

if __name__ == '__main__':
    flow = SendCardMessageFlow()
    outputs = flow.main({
        'mobile': '18600014356',
        #'mobile': '18945815579',
    })
    print(outputs)