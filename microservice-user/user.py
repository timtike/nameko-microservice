
from nameko.rpc import rpc, RpcProxy


class Index(object):
    name = "user"
    register_rpc = RpcProxy("user")

    @rpc
    def user(self):
        return {'data': "microserice user"}
