# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='my_protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rexample.proto\x12\x0bmy_protobuf\"\"\n\x06person\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\".\n\nall_person\x12 \n\x03Per\x18\x01 \x03(\x0b\x32\x13.my_protobuf.personb\x06proto3')
)




_PERSON = _descriptor.Descriptor(
  name='person',
  full_name='my_protobuf.person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='my_protobuf.person.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='my_protobuf.person.name', index=1,
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
  serialized_start=30,
  serialized_end=64,
)


_ALL_PERSON = _descriptor.Descriptor(
  name='all_person',
  full_name='my_protobuf.all_person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Per', full_name='my_protobuf.all_person.Per', index=0,
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
  serialized_start=66,
  serialized_end=112,
)

_ALL_PERSON.fields_by_name['Per'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['person'] = _PERSON
DESCRIPTOR.message_types_by_name['all_person'] = _ALL_PERSON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

person = _reflection.GeneratedProtocolMessageType('person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:my_protobuf.person)
  ))
_sym_db.RegisterMessage(person)

all_person = _reflection.GeneratedProtocolMessageType('all_person', (_message.Message,), dict(
  DESCRIPTOR = _ALL_PERSON,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:my_protobuf.all_person)
  ))
_sym_db.RegisterMessage(all_person)


# @@protoc_insertion_point(module_scope)
