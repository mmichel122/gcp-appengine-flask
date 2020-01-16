from google.cloud import storage
import io
import random
import time


def thelines():
    output = io.StringIO()
    for x in range(100):
                big_number = x**2
                time.sleep(3)
                output.write(f'{x}#Stress-{big_number}\n')
    contents = output.getvalue()
    output.close()
    return contents


def create_bucket_f1():
    client = storage.Client()
    token = random.randint(1000,9999)

    # The name for the new bucket
    bucket = client.create_bucket(f'mikael-sky-demo-bucket-{token}')
    blob = bucket.blob('test-blob')

    blob.upload_from_string(
        data=thelines(),
        content_type='text/plain',
        client=client
    )
