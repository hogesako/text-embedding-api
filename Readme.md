## usage
start api
```
docker run -p 9500:9500 hogesako/text-embedding-api:0.0.1
```

request vectorize
```
curl -X POST -H "Content-Type: application/json" -d \'{"sentence":"test-sentence"}\' http://localhost:9500/vectorize
```