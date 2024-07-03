from PIL import Image 
from pathlib import Path
import boto3
import os 

from IO import s3_upload, s3_download

s3_client = boto3.client('s3',
                         aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                         aws_secret_access_key=os.environ['AWS_SECRET_ACCESS'],
                         region_name='ap-northeast-2'
                         )

# 이미지 읽어오기 
image_paths = list(Path('data').glob('*.jpg'))
image = Image.open(image_paths[0])

# bucket 및 key 설정
bucket = "ocr-labeler"
key = image_paths[0].name


# S3에 이미지 업로드
s3_upload(image=image, 
          s3_client=s3_client, 
          bucket=bucket,
          key=key
          )

# S3에서 이미지 다운로드
downloaded_image = s3_download(s3_client=s3_client,
                               bucket=bucket,
                               key=key
                               )

downloaded_image.save('downloaded_image.jpg')

