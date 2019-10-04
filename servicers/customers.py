from defs import customer_pb2
from defs import customer_pb2_grpc
import logging


class Customers(customer_pb2_grpc.CustomerServicer):

    def GetCustomers(self, request, context):
        
        # Mock Data
        customers = [
            type('',(),{'name':'Ahmet', 'lastname':'Yılmaz'})(), 
            type('',(),{'name':'Hasan', 'lastname':'Yılmaz'})()]

        customers_response = customer_pb2.CustomersResponse()

        for customer in customers:
            if str(customer.name) == str(request.customerName):
                customers_response.customers.append(customer_pb2.CustomerData(name=customer.name, lastname=customer.lastname))
        
        if len(customers_response.customers) == 0:
            logging.info("No customers found with name %s" % request.customerName)

        return customers_response

