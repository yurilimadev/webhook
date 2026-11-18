class EndpointRepository:

    endpoint_list = {
        "email":[],
        "endpoint":[]
    }
    def cadastrar(self,email,endpoint):
        self.endpoint_list['email'].append(email)
        self.endpoint_list['endpoint'].append(endpoint)
