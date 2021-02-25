import os
import urllib3
import json

def lambda_handler(event, context):
    
  VoteID = '48d75c359ce4'
 
  http = urllib3.PoolManager()
  QuestionsURI = http.request('GET','https://api.mentimeter.com/questions/'+VoteID,headers={'Content-Type': 'application/json'})
  ResultsURI = http.request('GET','https://api.mentimeter.com/questions/'+VoteID+'/result',headers={'Content-Type': 'application/json'})
  GetQuestions = json.loads(QuestionsURI.data.decode('utf-8'))
  #Questions=GetQuestions.json()
  GetResults =json.loads(ResultsURI.data.decode('utf-8'))
  #Results=GetResults.json()
  resultDict = {
        "question": GetQuestions['question'],
        "results": GetResults['results']
      }
  return (resultDict)
