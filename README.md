# API Test Tool
API testing

## Installation
 Python Version: Python 3.13.5  
 Make sure python is installed on your system  
 Install the python libraries used  
* pip install -r requirements.txt 

## Test Execution
python -m pytest -v

## Tests
* **Test 01**: Check the api response code, Expected 200 when request succeeded.
* **Test 02**: Check length of data recieved, Expected 100
* **Test 03**: Check type of data returned, Expected data type list of dictionary
* **Test 04**: Check the content of list, Expected dictionary
* **Test 05**: Check the keys in the dictionary, Expected 'userID', 'id', 'title', 'body'
* **Test 06**: Check the data type values in the dictionary, Expected 'userID' of type int, 'id' is of type int, 'title' is of type str, 'body' is of type str
* **Test 07**: Create a post and check the response, Expected response code 201
* **Test 08**: Update a post and check the response, Expected response code 201
* **Test 09**: Delete a post and check the response, Expected response code 200
* **Test 10**: Update a post with invalid id, and check the response, Expected response code 500
* **Test 11**: Delete a post with invalid id, and check the response, Expected response code 404

