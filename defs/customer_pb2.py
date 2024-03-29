# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: customer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='customer.proto',
  package='customer',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x63ustomer.proto\x12\x08\x63ustomer\"&\n\x0e\x43ustomerLookup\x12\x14\n\x0c\x63ustomerName\x18\x01 \x01(\t\">\n\x11\x43ustomersResponse\x12)\n\tcustomers\x18\x01 \x03(\x0b\x32\x16.customer.CustomerData\".\n\x0c\x43ustomerData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08lastname\x18\x02 \x01(\t2S\n\x08\x43ustomer\x12G\n\x0cGetCustomers\x12\x18.customer.CustomerLookup\x1a\x1b.customer.CustomersResponse\"\x00\x62\x06proto3')
)




_CUSTOMERLOOKUP = _descriptor.Descriptor(
  name='CustomerLookup',
  full_name='customer.CustomerLookup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customerName', full_name='customer.CustomerLookup.customerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=66,
)


_CUSTOMERSRESPONSE = _descriptor.Descriptor(
  name='CustomersResponse',
  full_name='customer.CustomersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customers', full_name='customer.CustomersResponse.customers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=130,
)


_CUSTOMERDATA = _descriptor.Descriptor(
  name='CustomerData',
  full_name='customer.CustomerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='customer.CustomerData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastname', full_name='customer.CustomerData.lastname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=178,
)

_CUSTOMERSRESPONSE.fields_by_name['customers'].message_type = _CUSTOMERDATA
DESCRIPTOR.message_types_by_name['CustomerLookup'] = _CUSTOMERLOOKUP
DESCRIPTOR.message_types_by_name['CustomersResponse'] = _CUSTOMERSRESPONSE
DESCRIPTOR.message_types_by_name['CustomerData'] = _CUSTOMERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerLookup = _reflection.GeneratedProtocolMessageType('CustomerLookup', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERLOOKUP,
  '__module__' : 'customer_pb2'
  # @@protoc_insertion_point(class_scope:customer.CustomerLookup)
  })
_sym_db.RegisterMessage(CustomerLookup)

CustomersResponse = _reflection.GeneratedProtocolMessageType('CustomersResponse', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERSRESPONSE,
  '__module__' : 'customer_pb2'
  # @@protoc_insertion_point(class_scope:customer.CustomersResponse)
  })
_sym_db.RegisterMessage(CustomersResponse)

CustomerData = _reflection.GeneratedProtocolMessageType('CustomerData', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERDATA,
  '__module__' : 'customer_pb2'
  # @@protoc_insertion_point(class_scope:customer.CustomerData)
  })
_sym_db.RegisterMessage(CustomerData)



_CUSTOMER = _descriptor.ServiceDescriptor(
  name='Customer',
  full_name='customer.Customer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=180,
  serialized_end=263,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomers',
    full_name='customer.Customer.GetCustomers',
    index=0,
    containing_service=None,
    input_type=_CUSTOMERLOOKUP,
    output_type=_CUSTOMERSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMER)

DESCRIPTOR.services_by_name['Customer'] = _CUSTOMER

# @@protoc_insertion_point(module_scope)
