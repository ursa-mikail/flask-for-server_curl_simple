
python app.py

open -a "Google Chrome" http://127.0.0.1:5000

curl -X GET http://127.0.0.1:5000/items/1
curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"item_id": "1", "data": "some data"}'
curl -X PUT http://127.0.0.1:5000/items/1 -H "Content-Type: application/json" -d '{"data": "updated data"}'

curl -X DELETE http://127.0.0.1:5000/items/1

""" terminal (client):
% curl -X GET http://127.0.0.1:5000/items/1
{
  "error": "Item not found"
}
% curl -X PUT http://127.0.0.1:5000/items/1 -H "Content-Type: application/json" -d '{"data": "updated data"}'

{
  "error": "Item not found"
}
% curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"item_id": "1", "data": "some data"}'

{
  "message": "Item created"
}
% curl -X PUT http://127.0.0.1:5000/items/1 -H "Content-Type: application/json" -d '{"data": "updated data"}'            

{
  "message": "Item updated"
}
% curl -X GET http://127.0.0.1:5000/items/1                                                                              
{
  "data": "updated data"
}
% curl -X DELETE http://127.0.0.1:5000/items/1        

{
  "message": "Item deleted"
}
% curl -X GET http://127.0.0.1:5000/items/1   
{
  "error": "Item not found"
}

 % curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"item_id": "1", "data": "some data"}'

{
  "message": "Item created"
}
% curl -X GET http://127.0.0.1:5000/items/1                                                                              
{
  "data": "some data",
  "item_id": "1"
}

"""

terminal (main:server):
At the trace: 
"""
127.0.0.1 - - [07/Oct/2024 20:15:38] "GET /items/1 HTTP/1.1" 404 -
127.0.0.1 - - [07/Oct/2024 20:16:13] "PUT /items/1 HTTP/1.1" 404 -
127.0.0.1 - - [07/Oct/2024 20:16:31] "POST /items HTTP/1.1" 201 -
127.0.0.1 - - [07/Oct/2024 20:16:39] "PUT /items/1 HTTP/1.1" 200 -
127.0.0.1 - - [07/Oct/2024 20:16:47] "GET /items/1 HTTP/1.1" 200 -
127.0.0.1 - - [07/Oct/2024 20:17:04] "DELETE /items/1 HTTP/1.1" 200 -
127.0.0.1 - - [07/Oct/2024 20:17:09] "GET /items/1 HTTP/1.1" 404 -
127.0.0.1 - - [07/Oct/2024 20:18:45] "PUT /items/1 HTTP/1.1" 404 -
127.0.0.1 - - [07/Oct/2024 20:18:58] "POST /items HTTP/1.1" 201 -
127.0.0.1 - - [07/Oct/2024 20:19:11] "GET /items/1 HTTP/1.1" 200 -
"""

