class NetworkLayer:
    def route_data(self, data):
        print(f"Network Layer: Adding IP routing to data")
        routed_data = f"IP({data})"
        return routed_data

    def unroute_data(self, data):
        print(f"Network Layer: Removing IP routing from data")
        return data.replace("IP(", "").replace(")", "")
