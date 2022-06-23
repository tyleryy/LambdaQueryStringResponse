import json


def lambda_handler(event, context):

    #1 Parse out query string params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']
    
    print('transactionId = ' + transactionId + '\n')
    print('transactionType = ' + transactionType + '\n')
    print('transactionAmount = ' + transactionAmount + "\n")
    
    #2 Construct body of response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello from Lambda Land'
    
    #3 Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)
    
    #4 Return the response object
    return responseObject
    

