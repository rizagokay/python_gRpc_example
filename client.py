
from __future__ import print_function
import logging

import grpc

from defs import customer_pb2
from defs import customer_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = customer_pb2_grpc.CustomerStub(channel)
        response = stub.GetCustomers(customer_pb2.CustomerLookup(customerName= "Hassan"))

    print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
