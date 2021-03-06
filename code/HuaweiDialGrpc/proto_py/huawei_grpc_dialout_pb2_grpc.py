import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import huawei_grpc_dialout_pb2 as huawei__grpc__dialout__pb2


class gRPCDataserviceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.dataPublish = channel.stream_stream(
        '/huawei_dialout.gRPCDataservice/dataPublish',
        request_serializer=huawei__grpc__dialout__pb2.serviceArgs.SerializeToString,
        response_deserializer=huawei__grpc__dialout__pb2.serviceArgs.FromString,
        )


class gRPCDataserviceServicer(object):

  def dataPublish(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_gRPCDataserviceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'dataPublish': grpc.stream_stream_rpc_method_handler(
          servicer.dataPublish,
          request_deserializer=huawei__grpc__dialout__pb2.serviceArgs.FromString,
          response_serializer=huawei__grpc__dialout__pb2.serviceArgs.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'huawei_dialout.gRPCDataservice', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
