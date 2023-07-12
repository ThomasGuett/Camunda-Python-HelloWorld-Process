import json
import logging
import grpc
from zeebe_grpc import gateway_pb2, gateway_pb2_grpc

with grpc.insecure_channel("localhost:26500") as channel:
    stub = gateway_pb2_grpc.GatewayStub(channel)

    # deploy a process definition
    with open("python-helloWorld.bpmn", "rb") as process_definition_file:
        process_definition = process_definition_file.read()
        process = gateway_pb2.ProcessRequestObject(
            name="python-helloWorld.bpmn",
            definition=process_definition
        )
    stub.DeployProcess(
        gateway_pb2.DeployProcessRequest(
            processes=[process]
        )
    )

    # start a process instance
    variables = {
        "message": "This is a Message"
    }
    stub.CreateProcessInstance(
        gateway_pb2.CreateProcessInstanceRequest(
            bpmnProcessId="PythonHelloWorld",
            version=-1,
            variables=json.dumps(variables)
        )
    )

    # start a worker
    activate_jobs_response = stub.ActivateJobs(
        gateway_pb2.ActivateJobsRequest(
            type="taskForPython",
            worker="Python worker",
            timeout=60000,
            maxJobsToActivate=32
        )
    )
    for response in activate_jobs_response:
        for job in response.jobs:
            try:
                print(job.variables)
                stub.CompleteJob(gateway_pb2.CompleteJobRequest(jobKey=job.key, variables=json.dumps({})))
                logging.info("Job Completed")
            except Exception as e:
                stub.FailJob(gateway_pb2.FailJobRequest(jobKey=job.key))
                logging.info(f"Job Failed {e}")