all:
	python3 -m grpc_tools.protoc -I ./proto --python_out=./proto --grpc_python_out=./proto ./proto/helloworld.proto
clean:
	rm proto/helloworld_pb2_grpc.py proto/helloworld_pb2.py
server:
	@python3 server.py
client:
	@python3 client.py
