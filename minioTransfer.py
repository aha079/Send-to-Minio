from minio import Minio
from minio.error import ResponseError
import os
client = Minio('localhost', access_key='minioadmin', secret_key='minioadmin', secure=True)
for root, dirs, files in os.walk("."):
    for file in files:
        print(root)
        try:
            with open(os.path.join(root,file), 'rb') as file_data:
                file_stat = os.stat(os.path.join(root,file))
                print(client.put_object('bucketname',os.path.join(root[2:],file),file_data, file_stat.st_size))
        except ResponseError as err:
            print(err)