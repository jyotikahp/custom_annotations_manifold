import boto3
import json

from botocore.exceptions import ClientError

from utils.upload import upload_to_s3, get_presigned_url
from utils.config import custom_annotations_lambda, DEFAULT_REGION
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def add_custom_annotations(schema_change, local_filepath):
    presigned_url = get_presigned_url()
    upload_to_s3(presigned_url, local_filepath)

    lambda_client = boto3.client('lambda', region_name=DEFAULT_REGION)
    try:
        response=lambda_client.invoke(
            FunctionName=custom_annotations_lambda,
            InvocationType='Event',
            Payload=json.dumps(schema_change)
        )
    except ClientError:
        logger.exception("Couldn't invoke function %s.", custom_annotations_lambda)
        raise
    return response
