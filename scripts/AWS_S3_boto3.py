import uuid

import boto3
import yaml
import os
from botocore.exceptions import ClientError



#https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
#https://realpython.com/python-boto3-aws-s3/
'''


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
s3_resource.meta.client
--s3.buckets.all():
--for my_bucket_object in s3.Bucket(bucket_name).objects.all()  --my_bucket_object.key
'''



def create_boto3_obj( aws_access_key_id,aws_secret_access_key,region):
    session = boto3.session.Session( aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key ,region_name=region )
    s3 = session.resource('s3')

    return s3

def list_of_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def list_file_in_bucket(s3,bucket_name):
    my_bucket = s3.Bucket(bucket_name)
    for my_bucket_object in my_bucket.objects.all():
    #for objects in my_bucket.objects.filter(Prefix="csv_files/"):
        if my_bucket_object.key.endswith('csv'): #startswith('temp')
            print(my_bucket_object.key)

def list_file_with_details(s3,bucket_name):
    my_bucket = s3.Bucket(bucket_name)
    for obj in my_bucket.objects.all():
        subsrc = obj.Object()
        print("key: {key} , storage_class: {storage_class} , last_modified: {last_modified} , size : {size}".format (key=obj.key, storage_class=obj.storage_class, last_modified=obj.last_modified , size=obj.size))
        #print(subsrc.version_id, subsrc.metadata)

def upload_file_in_bucket(s3,bucket_name,file_location,file_name):
    try:
        response=s3.meta.client.upload_file(file_location, bucket_name, file_name)
    except ClientError as ex:
        print("Error: ", ex)
    return response

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(s3,bucket_name ,region):
    response=s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': '{x}'.format(x=region)})
    return response

def delete_bucket_object(s3,bucket_name,file_name):
    response=s3.Object(bucket_name, file_name).delete()
    return response



if __name__=="__main__":
    #uploading config file
    file_path= os.path.join(os.getcwd(),'config_files','aws_cred.yaml')
    data_load=yaml.safe_load(open(file_path))
    #setting up variable
    secret_key=data_load['user_info']['prod']['Secret_Key']
    access_key = data_load['user_info']['prod']['Access_key']
    region=data_load['bucket_info']['region']
    output=data_load['bucket_info']['output']
    bucket_name=data_load['bucket_info']['bucket_name']

    # 1. creating boto3 object
    s3=create_boto3_obj(aws_access_key_id= access_key , aws_secret_access_key=secret_key,region=region)

    # 2. Get a list of all bucket names from the response
    #list_of_buckets(s3=s3)

    # 3. listing file in bucket
    #file_list=list_file_in_bucket(s3=s3,bucket_name=bucket_name)

    #listing    file in bucket with detail
    #list_file_with_details(s3=s3,bucket_name=bucket_name)

    # 4. Upload file in Bucket
    file_location = os.path.join(os.getcwd(), 'file_upload', 'temp_data1.csv')
    file_name = 'temp_data1.csv'
    bucket_name='vksh.familia.04030613'
    # upload_file=upload_file_in_bucket(s3,bucket_name,file_location,file_name)

    # 5. create bucket
    #bucket_name= create_bucket_name('vksh.2023.')
    #response=create_bucket(s3, bucket_name[:18], region)
    #print (response)

    # 6.Delete object
    file_name='temp_data.csv'
    bucket_name = 'vksh.familia.04030613'
    response=delete_bucket_object(s3, bucket_name, file_name)
    print(response)

    #delete and upload:
    file_location = os.path.join(os.getcwd(), 'file_upload', 'temp_data1.csv')
    file_name = 'temp_data1.csv'
    bucket_name = 'vksh.familia.04030613'
    upload_file = upload_file_in_bucket(s3, bucket_name, file_location, file_name)
    print (upload_file)








