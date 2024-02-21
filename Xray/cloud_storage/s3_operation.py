import os
import sys
from Xray.exception import XrayException


class S3operation:
    def sync_folder_to_s3(self,folder:str,bucket_name:str,bucket_folder_name:str)-> None:

        try:      
            command:str=(
                f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}"
            )
            os.system(command)

        except Exception as e:
            raise XrayException(e,sys)
    

    def sync_folder_to_s3(self,folder:str,bucket_name:str,bucket_folder_name:str)-> None:

        try:
            command:str=(
                f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/{folder}"
            )
        except Exception as e:
            raise XrayException(e,sys)
