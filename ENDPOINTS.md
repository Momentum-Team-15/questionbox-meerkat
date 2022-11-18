# Questionbox
This application is a question and answer platform, similar to Stack Overflow. It does _not_ have to be themed to code-related questions, though. Theming and design is up to you.

You may not be able to do ALL of the listed requirements. That is OK. Decide what the core functionality is and what you can wait to implement once you have the basics done.

*Questionbox is an Application Programming Interface (API) built using Django Rest Framework (DRF)
All requests require authentication.
## Base URL:
All endpoints begin with `https://meercat-question-box.onrender.com/`
NOTE: API Root is /api/
|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|[/auth/users/](#create-a-new-user)|Create a new user|
|POST|[/auth/token/login/](#login-user)|Login user|
|POST|[/auth/users/me/](#users-info)|User's info|
|GET|[/users](#all_users)|List of all users|
|POST|[/auth/token/logout/](#logout-user)|Logout user|
|GET|[api/questions/](#list-of-all-questions)|returns a list of all questions|
|GET|[api/questions/{pk}](#details-of-one-question)|details of one question|
|POST|[api/questions/](#create-a-question)|create a question|
|PATCH|[api/questions/{pk}](#update-a-question)|update a question|
|DELETE|[api/questions/{pk}](#delete-a-question)|delete a question|
|GET|[api/questions?search=<search_term>](#search-questions)|search questions|
## Create a new user
### Request
Required fields: username and password
Optional fields: email
```json
POST auth/users/
{
  "username": "Luke",
  "password": "Momentum1"
}
```
### Response
Response: If you receive the same info you provided, user creation was successful!
```json
201 Created
{
  "email": "",
  "username": "Luke",
  "id": 4,
}
```
## Login user
### Request
Required fields: username, password
```json
POST auth/token/login/
{
    "username": "Luke",
    "password": "Momentum1"
}
```
### Response
```json
200 OK
{
    "auth_token": "d99a2de1b0a09db0fc2da23c9fdb1fc2447fff5d"
}
```
NOTE: auth_token must be passed for all requests with the logged in user. It remains active till user is [logged out](#logout-user).
## User's info
Requirement: user must be logged in.
```json
GET /auth/users/me/
```
### Response
```json
200 OK
{
    "id": 4,
    "username": "Luke",
    "email": "",
}
```
## Logout user
### Request
Required fields: None
```json
POST /auth/token/logout/
```
### Response
```json
204 No Content
```
## list of all questions
Returns list of all questions.
### Request
Required fields: None
```json
GET api/questions/
```
### Response
```json
200 OK
[
	{
		"pk": 2,
		"title": "cat",
		"created_date": "2022-11-18T02:40:58.361845Z",
		"question": "test teat test question 2",
		"user": "tim",
		"total_answers": 0
	},
	{
		"pk": 1,
		"title": "Dog",
		"created_date": "2022-11-18T02:40:26.456804Z",
		"question": "test test test question 1",
		"user": "tim",
		"total_answers": 0
	},
	{
		"pk": 3,
		"title": "bird",
		"created_date": "2022-11-18T02:41:17.312426Z",
		"question": "test question 3",
		"user": "tim",
		"total_answers": 0
	}
]
```

## details of one question
Returns detail of one question.
### Request
Required fields: None
```json
GET api/questions/<pk>/
```
### Response
```json
200 OK
{
	"pk": 2,
	"title": "cat",
	"created_date": "2022-11-18T02:40:58.361845Z",
	"question": "test teat test question 2",
	"user": "tim",
	"total_answers": 0
}
```
## create a question
create a question.
### Request
Required fields:
```json
POST api/questions/
{
	
	"title": "snake",
	"question": "test teat test question 4"
}
```
### Response
```json
201 Created
{
	"pk": 3,
	"title": "snake",
	"created_date": "2022-11-18T03:10:55.709270Z",
	"question": "test teat test question 4",
	"user": "tim"
}
```
## update a question
update a question.
### Request
Required fields:
```json
PATCH api/questions/<pk>
{
	
	"title": "bird",
	
}
```
### Response
```json
201 Created
{
	"pk": 3,
	"title": "bird",
	"created_date": "2022-11-18T03:10:55.709270Z",
	"question": "test teat test question 4",
	"user": "tim",
	"total_answers": 0
}
```
## delete a question
delete a question.
### Request
Required fields:None
```json
DELETE api/questions/<pk>

```
### Response
```json
204 No Content

```
## search questions
Search term in question title.
### Request
Required fields: None
```json
GET api/questions?search=dog
```
### Response
```json
200 OK
[
	{
		"pk": 4,
		"title": "dog",
		"created_date": "2022-11-18T03:29:04.755255Z",
		"question": "test question 5",
		"user": "tim"
	}
]
```











