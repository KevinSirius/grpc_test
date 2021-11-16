import time
import grpc
import test_pb2_grpc
import test_pb2


def run():
    key = bytes(30)
    path = ""
    seq_no = 0
    begin = 0
    end = 1
    request = test_pb2.content_request(client_public_key=key, file_path=path, sequence_no=seq_no, range_begin=begin, range_end=end)

    with grpc.insecure_channel("localhost:9999") as channel:
        stub = test_pb2_grpc.client_to_publisherStub(channel)
        while True:
            try:
                response = stub.request_content(request)
                print(response.request_sequence_no)
                time.sleep(0.001)
            except KeyboardInterrupt:
                print("keyboard Interrupted")
                channel.unsubscribe(close)
                exit()

def close(channel):
    channel.close()


if __name__ == "__main__":
    run()