import logging
import boto3
from botocore.exceptions import ClientError
import requests
from utils.config import key, bucket, action

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def generate_presigned_url(s3_client, client_method, method_parameters, expires_in):
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod=client_method,
            Params=method_parameters,
            ExpiresIn=expires_in
        )
        logger.info("Got presigned URL: %s", url)
    except ClientError:
        logger.exception(
            f"Couldn't get a presigned URL for client method {client_method}.")
        raise
    return url


def get_presigned_url():
    s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4'))
    url = generate_presigned_url(
        s3_client, action, {'Bucket': bucket, 'Key': key}, 3600)
    return url


def upload_to_s3(url, local_filepath):
    logger.info("Using the Requests package to send a request to the URL.")
    response = None
    logger.info("Putting data to the URL.")
    try:
        with open(local_filepath, 'r') as object_file:
            object_text = object_file.read()
        response = requests.put(url, data=object_text)
    except FileNotFoundError:
        logger.info(f"Couldn't find {local_filepath}. For a PUT operation, the key must be the name of a file that "
                    f"exists on your computer.")

    if response is not None:
        logger.info("Got response:")
        logger.info(f"Status: {response.status_code}")
        logger.info(response.text)
