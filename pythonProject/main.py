import sys, os
import boto3, botocore
from sqlalchemy import create_engine
import pandas as pd
#import sqlalchemy_handler
#engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
#df.to_sql('table_name', engine, method=psql_insert_copy)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def connect_to_db(port=5432):
    my_env = os.environ.copy()
    user = my_env['POSTGRES_USER']
    pass1 = my_env['POSTGRES_PASSWORD']
    db = my_env['POSTGRES_DB']
    host = my_env['POSTGRES_HOST']
    engine = None
    try:
        engine = create_engine('postgresql://'+user+':'+pass1+'@'+host+':'+str(port)+'/'+db)
    except Exception as e:
        print("Can not connect to DB there is an Error ")
        print(f"Error=>{e}")
        sys.exit(1)

    return engine


def download_csv(s3name: str, filename: str, target: str):

    try:
        s3 = boto3.client('s3')
        with open(target, 'wb') as f:
            s3.download_fileobj(s3name, filename, f)

    except (Exception, botocore.exceptions.ClientError, botocore.exceptions.ParamValidationError) as e:
        print(f"Error occurred while trying to download {filename} => the Error {e}")
        sys.exit(1)
    return s3


def load_file_db (filename, table, engine):
    try:
        pd_file = pd.read_csv(filename)
        pd_file.to_sql(con=engine, name=table, if_exists='append')
    except Exception as e:
        print(f"Error load CSV file to DB ==> {e}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = '/tmp/download_emp'
    #engine = connect_to_db('dockeruser', 'dockerPasswd', 'csvDB', 'vlptk-jenkinit01', 5432)
    engine = connect_to_db(5432)
    download_csv('mahmoodm297', 'employees.csv', f)
    load_file_db(f, 'empleyees', engine)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
