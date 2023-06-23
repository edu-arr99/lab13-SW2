Feature:

Scenario:
  * url 'http://127.0.0.1:8080/igv'
  * method get
  * status 200
  * match response == { "igv": "Internal Server Error - 500" }

