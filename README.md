# recordpb

Record Service API Protobuf

# Interface

Public interface based on gRPC to communicate with RecordBase on any program language.

The main service called `recordbase.RecordService` and it is available on each data node in API endpoint host:port.

# Golang

Build
```
make
```

# Python

Install python3 on local machine and them required libraries.
Requirements:
```
pip install grpcio-tools
```

Build
```
make python
```

