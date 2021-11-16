import os
import hashlib
import time
import file_transfer_lib as lib


if __name__ == '__main__':
    client = lib.FileClient('localhost:8888')

    # demo for file uploading
    in_file_name = './tmp/test.jpg'
    if not os.path.exists(in_file_name):
        raise Exception("file not exists!")

    file_size = os.path.getsize(in_file_name)
    start_time = time.time()
    response = client.upload(in_file_name)
    print("Time used for uploading is: ", time.time() - start_time)
    assert response == file_size


    # demo for file downloading:
    out_file_name = './tmp/test_out.jpg'
    if os.path.exists(out_file_name):
        os.remove(out_file_name)
    start_time = time.time()
    client.download('whatever_name', out_file_name)
    print("Time used for downloading is: ", time.time() - start_time)
    orig_hash = hashlib.md5(open(in_file_name,'rb').read()).hexdigest()
    download_hash = hashlib.md5(open(out_file_name,'rb').read()).hexdigest()
    assert orig_hash == download_hash

    