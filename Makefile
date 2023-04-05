
all: go python java

go:
	rm -f *.swagger.json
	protoc proto/*.proto -I . -I third_party -I ~/go/include/google/protobuf --go_out=. --go-grpc_out=. --grpc-gateway_out=logtostderr=true,allow_delete_body=true:. --openapiv2_out=logtostderr=true,allow_delete_body=true:.

python:
	python3 -m grpc_tools.protoc -I . -I third_party -I ~/go/include/google/protobuf --python_out=python3 --grpc_python_out=python3 proto/*.proto

java:
	mvn clean install

update:
	go get -u ./...


