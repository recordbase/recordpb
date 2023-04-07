# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto import record_service_pb2 as proto_dot_record__service__pb2


class RecordServiceStub(object):
    """
    RecordService


    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCounts = channel.unary_unary(
                '/recordbase.RecordService/GetCounts',
                request_serializer=proto_dot_record__service__pb2.TenantRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.Counts.FromString,
                )
        self.Lookup = channel.unary_unary(
                '/recordbase.RecordService/Lookup',
                request_serializer=proto_dot_record__service__pb2.LookupRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.RecordEntry.FromString,
                )
        self.Search = channel.unary_stream(
                '/recordbase.RecordService/Search',
                request_serializer=proto_dot_record__service__pb2.SearchRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.RecordEntry.FromString,
                )
        self.Get = channel.unary_unary(
                '/recordbase.RecordService/Get',
                request_serializer=proto_dot_record__service__pb2.GetRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.RecordEntry.FromString,
                )
        self.Create = channel.unary_unary(
                '/recordbase.RecordService/Create',
                request_serializer=proto_dot_record__service__pb2.CreateRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.CreateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/recordbase.RecordService/Delete',
                request_serializer=proto_dot_record__service__pb2.DeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Update = channel.unary_unary(
                '/recordbase.RecordService/Update',
                request_serializer=proto_dot_record__service__pb2.UpdateRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UploadFile = channel.stream_unary(
                '/recordbase.RecordService/UploadFile',
                request_serializer=proto_dot_record__service__pb2.UploadFileContent.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DownloadFile = channel.unary_stream(
                '/recordbase.RecordService/DownloadFile',
                request_serializer=proto_dot_record__service__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.FileContent.FromString,
                )
        self.DeleteFile = channel.unary_unary(
                '/recordbase.RecordService/DeleteFile',
                request_serializer=proto_dot_record__service__pb2.DeleteFileRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Scan = channel.unary_stream(
                '/recordbase.RecordService/Scan',
                request_serializer=proto_dot_record__service__pb2.ScanRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.RecordEntry.FromString,
                )
        self.AddKeyRange = channel.unary_unary(
                '/recordbase.RecordService/AddKeyRange',
                request_serializer=proto_dot_record__service__pb2.KeyRange.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetKeyCapacity = channel.unary_unary(
                '/recordbase.RecordService/GetKeyCapacity',
                request_serializer=proto_dot_record__service__pb2.TenantRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.KeyCapacity.FromString,
                )
        self.MapGet = channel.unary_unary(
                '/recordbase.RecordService/MapGet',
                request_serializer=proto_dot_record__service__pb2.MapGetRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.MapEntry.FromString,
                )
        self.MapPut = channel.unary_unary(
                '/recordbase.RecordService/MapPut',
                request_serializer=proto_dot_record__service__pb2.MapPutRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.MapRemove = channel.unary_unary(
                '/recordbase.RecordService/MapRemove',
                request_serializer=proto_dot_record__service__pb2.MapRemoveRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.MapRange = channel.unary_stream(
                '/recordbase.RecordService/MapRange',
                request_serializer=proto_dot_record__service__pb2.MapRangeRequest.SerializeToString,
                response_deserializer=proto_dot_record__service__pb2.MapEntry.FromString,
                )


class RecordServiceServicer(object):
    """
    RecordService


    """

    def GetCounts(self, request, context):
        """
        Gets attributes counts

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Lookup(self, request, context):
        """
        Quick record lookup request

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """
        Search records by indexed attributes

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """
        Get record with all attributes

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """
        Create record with new primary_key

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """
        Delete record

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """
        Update record attributes

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request_iterator, context):
        """
        Upload File

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """
        Download File

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFile(self, request, context):
        """
        Delete File

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Scan(self, request, context):
        """
        Scan records

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddKeyRange(self, request, context):
        """
        Allocate primary key range

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetKeyCapacity(self, request, context):
        """
        Gets primary keys capacity

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MapGet(self, request, context):
        """
        Get map value associated with the record

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MapPut(self, request, context):
        """
        Put map value associated with the record. Returns old value.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MapRemove(self, request, context):
        """
        Remove map value associated with the record. Returns old value.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MapRange(self, request, context):
        """
        Scan all map key-value pairs

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecordServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCounts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCounts,
                    request_deserializer=proto_dot_record__service__pb2.TenantRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.Counts.SerializeToString,
            ),
            'Lookup': grpc.unary_unary_rpc_method_handler(
                    servicer.Lookup,
                    request_deserializer=proto_dot_record__service__pb2.LookupRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.RecordEntry.SerializeToString,
            ),
            'Search': grpc.unary_stream_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=proto_dot_record__service__pb2.SearchRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.RecordEntry.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=proto_dot_record__service__pb2.GetRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.RecordEntry.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=proto_dot_record__service__pb2.CreateRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.CreateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=proto_dot_record__service__pb2.DeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=proto_dot_record__service__pb2.UpdateRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=proto_dot_record__service__pb2.UploadFileContent.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=proto_dot_record__service__pb2.DownloadFileRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.FileContent.SerializeToString,
            ),
            'DeleteFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFile,
                    request_deserializer=proto_dot_record__service__pb2.DeleteFileRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Scan': grpc.unary_stream_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=proto_dot_record__service__pb2.ScanRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.RecordEntry.SerializeToString,
            ),
            'AddKeyRange': grpc.unary_unary_rpc_method_handler(
                    servicer.AddKeyRange,
                    request_deserializer=proto_dot_record__service__pb2.KeyRange.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetKeyCapacity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKeyCapacity,
                    request_deserializer=proto_dot_record__service__pb2.TenantRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.KeyCapacity.SerializeToString,
            ),
            'MapGet': grpc.unary_unary_rpc_method_handler(
                    servicer.MapGet,
                    request_deserializer=proto_dot_record__service__pb2.MapGetRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.MapEntry.SerializeToString,
            ),
            'MapPut': grpc.unary_unary_rpc_method_handler(
                    servicer.MapPut,
                    request_deserializer=proto_dot_record__service__pb2.MapPutRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'MapRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.MapRemove,
                    request_deserializer=proto_dot_record__service__pb2.MapRemoveRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'MapRange': grpc.unary_stream_rpc_method_handler(
                    servicer.MapRange,
                    request_deserializer=proto_dot_record__service__pb2.MapRangeRequest.FromString,
                    response_serializer=proto_dot_record__service__pb2.MapEntry.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'recordbase.RecordService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RecordService(object):
    """
    RecordService


    """

    @staticmethod
    def GetCounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/GetCounts',
            proto_dot_record__service__pb2.TenantRequest.SerializeToString,
            proto_dot_record__service__pb2.Counts.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Lookup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/Lookup',
            proto_dot_record__service__pb2.LookupRequest.SerializeToString,
            proto_dot_record__service__pb2.RecordEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/recordbase.RecordService/Search',
            proto_dot_record__service__pb2.SearchRequest.SerializeToString,
            proto_dot_record__service__pb2.RecordEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/Get',
            proto_dot_record__service__pb2.GetRequest.SerializeToString,
            proto_dot_record__service__pb2.RecordEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/Create',
            proto_dot_record__service__pb2.CreateRequest.SerializeToString,
            proto_dot_record__service__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/Delete',
            proto_dot_record__service__pb2.DeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/Update',
            proto_dot_record__service__pb2.UpdateRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/recordbase.RecordService/UploadFile',
            proto_dot_record__service__pb2.UploadFileContent.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/recordbase.RecordService/DownloadFile',
            proto_dot_record__service__pb2.DownloadFileRequest.SerializeToString,
            proto_dot_record__service__pb2.FileContent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/DeleteFile',
            proto_dot_record__service__pb2.DeleteFileRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Scan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/recordbase.RecordService/Scan',
            proto_dot_record__service__pb2.ScanRequest.SerializeToString,
            proto_dot_record__service__pb2.RecordEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddKeyRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/AddKeyRange',
            proto_dot_record__service__pb2.KeyRange.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetKeyCapacity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/GetKeyCapacity',
            proto_dot_record__service__pb2.TenantRequest.SerializeToString,
            proto_dot_record__service__pb2.KeyCapacity.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MapGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/MapGet',
            proto_dot_record__service__pb2.MapGetRequest.SerializeToString,
            proto_dot_record__service__pb2.MapEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MapPut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/MapPut',
            proto_dot_record__service__pb2.MapPutRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MapRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recordbase.RecordService/MapRemove',
            proto_dot_record__service__pb2.MapRemoveRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MapRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/recordbase.RecordService/MapRange',
            proto_dot_record__service__pb2.MapRangeRequest.SerializeToString,
            proto_dot_record__service__pb2.MapEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
