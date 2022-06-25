
from nameko.rpc import rpc, RpcProxy


class Index(object):
    name = "book"
    register_rpc = RpcProxy("book")

    @rpc
    def book(self):
        return {'data': "microserice book"}
