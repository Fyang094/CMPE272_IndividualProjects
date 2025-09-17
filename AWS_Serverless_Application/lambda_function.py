import json
import boto3

from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        # Create a new student record
        student = json.loads(event['body'])
        table.put_item(Item=student)
        return {
            'statusCode':200,
            'body':json.dumps('Student record added successfully')
        }
    
    if event['httpMethod'] == 'GET':
        # Fetch student record by student_id
        student_id = event['queryStringParameters']['student_id']
        response = table.get_item(Key={'student_id':student_id})
        return {
            'statusCode':200,
            'body':json.dumps(response['Item'])
        }

    if event['httpMethod'] == 'PUT':
        # Update student's detail 
        student = json.loads(event['body'])
        student_id = student['student_id']
        table.put_item(
            Item={
                'student_id':requestJSON['student_id'],
                'name':requestJSON['name'],
                'course':requestJSON['course']
            }
        )
        return {
            'statusCode':200,
            'body':json.dumps('Student record updated successfully')
        }
    
    if event['httpMethod'] == 'DELETE':
        # Removes a student record
        student_id = event['queryStringParameters']['student_id']
        table.delete_item(Key={'student_id': student_id})
        return {
            'statusCode':200,
            'body':json.dumps('Student record deleted successfully')
        }
