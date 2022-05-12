# Flask app

### Install
```
pip3 install -r requirements.txt --ignore-installed
```
### RUN
```
flask run
```

### Tesztelés
GET
```
curl http://127.0.0.1:5000/countries
```
POST
```
curl -v -X POST http://127.0.0.1:5000/countries \
   -H 'Content-Type: application/json' \
   -d '{"name":"Canada","capital":"Ottawa"}'
```
PUT
```
curl -v -X PUT http://127.0.0.1:5000/1 -H 'Content-Type: application/json' -d '{"name":"Canada","capital":"Ottawa"}'
```
DELETE
```
curl -v -X DELETE http://127.0.0.1:5000/3 \
   -H 'Content-Type: application/json'
```