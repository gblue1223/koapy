# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from koapy.backend.cybos import CybosPlusProxyService_pb2 as koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2


class CybosPlusProxyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Dispatch = channel.unary_unary(
                '/CybosPlusProxyService/Dispatch',
                request_serializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.DispatchRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.DispatchResponse.FromString,
                )
        self.Property = channel.unary_unary(
                '/CybosPlusProxyService/Property',
                request_serializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.PropertyRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.PropertyResponse.FromString,
                )
        self.Method = channel.unary_unary(
                '/CybosPlusProxyService/Method',
                request_serializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.MethodRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.MethodResponse.FromString,
                )
        self.Event = channel.stream_stream(
                '/CybosPlusProxyService/Event',
                request_serializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.EventRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.EventResponse.FromString,
                )


class CybosPlusProxyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Dispatch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Property(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Method(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Event(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CybosPlusProxyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Dispatch': grpc.unary_unary_rpc_method_handler(
                    servicer.Dispatch,
                    request_deserializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.DispatchRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.DispatchResponse.SerializeToString,
            ),
            'Property': grpc.unary_unary_rpc_method_handler(
                    servicer.Property,
                    request_deserializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.PropertyRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.PropertyResponse.SerializeToString,
            ),
            'Method': grpc.unary_unary_rpc_method_handler(
                    servicer.Method,
                    request_deserializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.MethodRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.MethodResponse.SerializeToString,
            ),
            'Event': grpc.stream_stream_rpc_method_handler(
                    servicer.Event,
                    request_deserializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.EventRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.EventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CybosPlusProxyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CybosPlusProxyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Dispatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CybosPlusProxyService/Dispatch',
            koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.DispatchRequest.SerializeToString,
            koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.DispatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Property(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CybosPlusProxyService/Property',
            koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.PropertyRequest.SerializeToString,
            koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.PropertyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Method(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CybosPlusProxyService/Method',
            koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.MethodRequest.SerializeToString,
            koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.MethodResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Event(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/CybosPlusProxyService/Event',
            koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.EventRequest.SerializeToString,
            koapy_dot_backend_dot_cybos_dot_CybosPlusProxyService__pb2.EventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
