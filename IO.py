# Image IO 
from PIL import Image
import numpy as np
import io
from typing import Union

# AWS S3
import boto3

def s3_upload(image: Union[np.array, Image.Image],
              s3_client: boto3.client,
              bucket: str,
              key: str
              ) -> None:
    """
    S3로 이미지를 업로드하는 함수 
    이미지를 Bytesio 형태로 변환한 후에 이를 S3에 업로드한다. 
    
    Args:
        image (np.array): 이미지를 나타내는 numpy array
    """

    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)

    # 이미지를 BytesIO로 변환
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    # S3에 업로드
    s3_client.upload_fileobj(buffer,    
                             bucket,
                             key
                             )
    

def s3_download(s3_client: boto3.client,
                bucket: str,
                key: str
                ) -> Image:
    """
    S3로부터 이미지를 다운로드하는 함수 
    S3에 저장된 이미지를 BytesIO로 변환한 후에 이를 Image로 변환한다. 
    
    Returns:
        Image: S3에 저장된 이미지
    """
    buffer = io.BytesIO()
    s3_client.download_fileobj(bucket, 
                               key, 
                               buffer)
    buffer.seek(0)

    image = Image.open(buffer)
    
    return image