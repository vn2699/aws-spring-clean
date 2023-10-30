import boto3
from botocore.exceptions import ClientError

class kinesis:
    def __init__(self, resourceType, region, resourceName, delete_functions):
        self.resourceType = resourceType
        self.region = region
        self.resourceName = resourceName
        self.delete_functions = delete_functions
        self.kinesis = boto3.client('kinesis')
    
    def delete_action(self):
        #ec2_functions = dir(self.ec2)
        #for ec2_function in ec2_functions:
        #print(f"function name= {ec2_function}, {self.resourceType}, {self.resourceName}")
        delete_function = self.delete_functions[self.resourceType]['delete']
        status = 'false'
        print(delete_function)
        if 'deregister_stream_consumer' in delete_function:
            #print(f"function name= {ec2_function}, {self.resourceType}, {self.resourceName}")
            try:
                self.kinesis.deregister_stream_consumer(
                    #StreamARN='string',
                    ConsumerName=self.resourceName
                    #ConsumerARN='string'
                )
                status = 'true'
            except ClientError as e:
                status = 'false'
                print(e)
                pass
        else:
            print(f"{delete_function} not supported")
        print(f"Resource Type: {self.resourceType} of resourceName: {self.resourceName} is deleted")
        return status
