class WaitingList:
    """Describes about the waiting list"""
    def __init__(self):
        """
        Initialises the values
        """
        self.clients=[]
        
    def add_client(self,client):
        self.clients.append(client)
    
    def __getitem__(self, position):
        return self.clients[position]
    
w1=WaitingList()
w1.add_client("Emily")
w1.add_client("Jack")
w1.add_client("Johnson")
print(w1[2])