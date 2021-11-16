
import os

if os.path.exists("data_type_pb2.py"):
    os.remove("data_type_pb2.py")

if os.path.exists("data_type_pb2_grpc.py"):
    os.remove("data_type_pb2_grpc.py")


if os.path.exists("test_pb2.py"):
    os.remove("test_pb2.py")

if os.path.exists("test_pb2_grpc.py"):
    os.remove("test_pb2_grpc.py")

if os.path.exists("chunk_pb2.py"):
    os.remove("chunk_pb2.py")

if os.path.exists("chunk_pb2_grpc.py"):
    os.remove("chunk_pb2_grpc.py")

print("removed files")