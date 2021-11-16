from concurrent import futures
import threading
import time
import grpc
import test_pb2
import data_type_pb2
import test_pb2_grpc


class Listener(test_pb2_grpc.client_to_publisherServicer):

    def __init__(self):
        self.counter = 0

    def request_content(self, request, context):
        seq_no = 0
        testString = "hello world"
        bundle = data_type_pb2.ticket_bundle(test=testString)
        code = 0
        error_msg_string = "no error"
        error_response = data_type_pb2.error(error_code=code, error_msg=error_msg_string)
        ticket_response = test_pb2.ticket_bundle_response(request_sequence_no=seq_no, bundles = [bundle], error_info=error_response)

        return ticket_response
    

def serve():
    """The main serve function of the server.
    This opens the socket, and listens for incoming grpc conformant packets"""

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    test_pb2_grpc.add_client_to_publisherServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    serve()
