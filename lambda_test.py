import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('meals')
def get_data(state,district):
    print(state, district)
    try:
        result = table.get_item(Key={'states':state, 'districts':district})
        print(result)
        if result['Item']:
            return (True, result['Item'])
        else:
            return(False, 'no item')
    except Exception as e:
        return (False,e)

def lambda_handler(event,context):
    print('hi')
    
    print(event)
    res = get_data(event['headers']['states'],event['headers']['districts'])
    
    status=200 if res[0] else 400
    print(res)
    
    return {
        
        'statusCode': status,
        'body': json.dumps(res[1])
    }
