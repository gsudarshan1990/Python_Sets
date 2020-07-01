class WaitingList:
    def __init__(self):
        self.client=[]

    def add_client(self,client1):
        self.client.append(client1)

    def __len__(self):
        return len(self.client)

w1=WaitingList()
w1.add_client("abc")
w1.add_client("def")
w1.add_client("efg")
print(len(w1))