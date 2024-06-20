Welcome
A small project on Django Rest Framework
A new user can Register/Signup using CREATE USER
A user can log in using the password and username
upon logging in page will be redirected to TOKEN page where user will recieve a token ID
Using the token user can use the API end point "https://samirgorai2.pythonanywhere.com/employeeapi/ "
User can make a GET/POST request from postman or curl
Using curl from command line interpreter:
Example GET request:
curl -X GET http://samirgorai2.pythonanywhere.com/employeeapi/ -H "Authorization: Token 2c51383716eaae5c2f796bd35f3f79ac8897fcc1"
replace token with your token
Example POST request:
curl -X POST http://samirgorai2.pythonanywhere.com/employeeapi/ -H "Authorization: Token 2c51383716eaae5c2f796bd35f3f79ac8897fcc1" -d "name=John&age=30&emp_id=2&sex=Male"
replace token with your token
set name=____ age=___ sex=_____ emp_id=_____
To make a GET request via postman (web.postman.co):
Example GET request:
postman GET
set to GET
set the URL to http://samirgorai2.pythonanywhere.com/employeeapi/
go to Authorization tab
set type to API key
set key to Authorization in value set it to TokenToken no Add to change it to header click on send.
result will be shown in 6
To make a POST request via postman (web.postman.co):
Example POST request:
postman POSTpostman POST
set to POST
set the URL to http://samirgorai2.pythonanywhere.com/employeeapi/
go to Authorization tab
set type to API key
set key to Authorization in value set it to TokenToken no Add to change it to header
go to body TAB
set it to raw
set the value to in JSON format as shown in 8
click on send
