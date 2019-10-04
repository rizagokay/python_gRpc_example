
import logging
import grpc
from defs import customer_pb2_grpc
from servicers.customers import Customers
from concurrent import futures


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    customer_pb2_grpc.add_CustomerServicer_to_server(Customers(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.debug("gRPC Server Started.")
    logging.debug("Waiting for termination.")
    server.wait_for_termination()
    
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    serve()
