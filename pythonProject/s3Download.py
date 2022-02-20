import sys , os
import boto3 , botocore
from postgres import Postgres

s3 = boto3.client('s3')

def downloadFile (fileName,target):
    s3 = boto3.client('s3')
    try:
        s3.download_fileobj('mahmoodm297', fileName, target)
    except (Exception,  botocore.exceptions.ClientError, botocore.exceptions.ParamValidationError) as e:
        print (f"Error occurred while trying to download {fileName} => the Error {e}")
        sys.exit()
my_env = os.environ.copy()
my_env["PATH"] = "/bin:/usr/bin:/usr/sbin:/sbin:" + my_env["PATH"]
#s3 = boto3.client('s3')
#s3.download_file('mahmoodm297', 'employees.csv', '/tmp/test')


with open('/tmp/test123', 'wb') as f:
    s3.download_fileobj('mahmoodm297', 'employees.csv', f)



if __name__ == '__main__':

