# Python HelloWorld Process in Camunda 8 SelfManaged

## Dependencies
This project is meant as a minimal starting point to figuring out how Camunda Platform 8 works together with python job workers, for that it utilizes:
(as found in Camunda Docs: https://docs.camunda.io/docs/next/apis-tools/community-clients/python/)
### zeebe Python gRPC (Community Project)
https://pypi.org/project/zeebe-grpc/
https://gitlab.com/stephane.ludwig/zeebe_python_grpc

### Camunda 8 Self-Managed Docker Compose
https://docs.camunda.io/docs/next/self-managed/platform-deployment/docker/
https://github.com/camunda/camunda-platform/blob/8.3.0-alpha3/docker-compose.yaml

### Python packages
grpcio https://grpc.io/docs/languages/python/quickstart/#download-the-example
zeebe-grpc https://pypi.org/project/zeebe-grpc/

## To run this project:

### Start up docker compose
```
docker compose -f docker-compose.yaml up
```

### Start up python job worker
```
python3 jobWorker.py
```

