from concurrent import futures
import logging
import grpc
import sys, os
sys.path.append(os.path.abspath('./proto'))
import proto.helloworld_pb2 as helloworld_pb2
import proto.helloworld_pb2_grpc as helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    print("Now serving..")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    try:

        serve()
    except KeyboardInterrupt:
        print("Terminated")
