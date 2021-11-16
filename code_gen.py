from grpc_tools import protoc
import os
#grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/example.proto

if os.path.exists("data_type_pb2.py"):
    os.remove("data_type_pb2.py")

if os.path.exists("data_type_pb2_grpc.py"):
    os.remove("data_type_pb2_grpc.py")


if os.path.exists("test_pb2.py"):
    os.remove("test_pb2.py")

if os.path.exists("test_pb2_grpc.py"):
    os.remove("test_pb2_grpc.py")

print("removed files")

protoc.main((
    '',
    '-I./protos',
    '--python_out=.',
    '--grpc_python_out=.',
    './protos/test.proto',
))

protoc.main((
    '',
    '-I./protos',
    '--python_out=.',
    '--grpc_python_out=.',
    './protos/data_type.proto',
))

protoc.main((
    '',
    '-I./protos',
    '--python_out=.',
    '--grpc_python_out=.',
    './protos/chunk.proto',
))