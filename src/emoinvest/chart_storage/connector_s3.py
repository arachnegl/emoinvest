import boto3
from botocore.exceptions import ClientError
from configurations.config_reader import get_config_reader
from pathlib import Path

configuration_reader = get_config_reader()


def build_file_path(file_name):
    return Path('/', configuration_reader.get('storage', 'tmp_chart'), file_name)


def save_file_to_s3(file_name, bucket_name='emoinvest'):
    file_path = build_file_path(file_name)
    s3 = boto3.resource('s3',
                        aws_access_key_id=configuration_reader.get('settings', 'keyId'),
                        aws_secret_access_key=configuration_reader.get('settings', 'sKeyId'))
    data = open(file_path, 'rb')
    s3.Bucket(bucket_name).put_object(Key=file_name, Body=data)


def download_file_from_s3(file_name, downloaded_file_name, bucket_name='emoinvest'):
    s3 = boto3.resource('s3',
                        aws_access_key_id=configuration_reader.get('settings', 'keyId'),
                        aws_secret_access_key=configuration_reader.get('settings', 'sKeyId'))

    try:
        return s3.Bucket(bucket_name).download_file(file_name, downloaded_file_name)
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            print("Could not read from s3")
