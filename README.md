# petstore

This is an implementation of the [Petstore API](https://github.com/OAI/OpenAPI-Specification/blob/66fe9db36115bbf5425892aaaac6dba5e3c5df59/examples/v3.0/petstore.yaml).

One difference is that this does not support the creation of new pets.

This API is currently being served at https://petstore-p7er.onrender.com.

## Running the server

```bash
git clone https://github.com/gptscript-ai/petstore.git
cd petstore
docker build -t petstore .
docker run --rm -p 8080:8080 petstore

# Send a request to the server:
curl localhost:8080/pets
```

If you want to use the OpenAPI definition with your local server, be sure to update the `static/openapi.yaml`
file before you build and run your Docker container.

## GPTScript example

```
Tools: https://petstore-p7er.onrender.com/openapi

List all the pets. What are the names of the dogs?
```
