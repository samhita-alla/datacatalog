# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from datacatalog import service_pb2 as datacatalog_dot_service__pb2


class DataCatalogStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateDataset = channel.unary_unary(
        '/datacatalog.DataCatalog/CreateDataset',
        request_serializer=datacatalog_dot_service__pb2.CreateDatasetRequest.SerializeToString,
        response_deserializer=datacatalog_dot_service__pb2.CreateDatasetResponse.FromString,
        )
    self.GetDataset = channel.unary_unary(
        '/datacatalog.DataCatalog/GetDataset',
        request_serializer=datacatalog_dot_service__pb2.GetDatasetRequest.SerializeToString,
        response_deserializer=datacatalog_dot_service__pb2.GetDatasetResponse.FromString,
        )
    self.CreateArtifact = channel.unary_unary(
        '/datacatalog.DataCatalog/CreateArtifact',
        request_serializer=datacatalog_dot_service__pb2.CreateArtifactRequest.SerializeToString,
        response_deserializer=datacatalog_dot_service__pb2.CreateArtifactResponse.FromString,
        )
    self.GetArtifact = channel.unary_unary(
        '/datacatalog.DataCatalog/GetArtifact',
        request_serializer=datacatalog_dot_service__pb2.GetArtifactRequest.SerializeToString,
        response_deserializer=datacatalog_dot_service__pb2.GetArtifactResponse.FromString,
        )
    self.AddTag = channel.unary_unary(
        '/datacatalog.DataCatalog/AddTag',
        request_serializer=datacatalog_dot_service__pb2.AddTagRequest.SerializeToString,
        response_deserializer=datacatalog_dot_service__pb2.AddTagResponse.FromString,
        )
    self.ListArtifacts = channel.unary_unary(
        '/datacatalog.DataCatalog/ListArtifacts',
        request_serializer=datacatalog_dot_service__pb2.ListArtifactsRequest.SerializeToString,
        response_deserializer=datacatalog_dot_service__pb2.ListArtifactsResponse.FromString,
        )


class DataCatalogServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateDataset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDataset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateArtifact(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetArtifact(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddTag(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListArtifacts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataCatalogServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateDataset': grpc.unary_unary_rpc_method_handler(
          servicer.CreateDataset,
          request_deserializer=datacatalog_dot_service__pb2.CreateDatasetRequest.FromString,
          response_serializer=datacatalog_dot_service__pb2.CreateDatasetResponse.SerializeToString,
      ),
      'GetDataset': grpc.unary_unary_rpc_method_handler(
          servicer.GetDataset,
          request_deserializer=datacatalog_dot_service__pb2.GetDatasetRequest.FromString,
          response_serializer=datacatalog_dot_service__pb2.GetDatasetResponse.SerializeToString,
      ),
      'CreateArtifact': grpc.unary_unary_rpc_method_handler(
          servicer.CreateArtifact,
          request_deserializer=datacatalog_dot_service__pb2.CreateArtifactRequest.FromString,
          response_serializer=datacatalog_dot_service__pb2.CreateArtifactResponse.SerializeToString,
      ),
      'GetArtifact': grpc.unary_unary_rpc_method_handler(
          servicer.GetArtifact,
          request_deserializer=datacatalog_dot_service__pb2.GetArtifactRequest.FromString,
          response_serializer=datacatalog_dot_service__pb2.GetArtifactResponse.SerializeToString,
      ),
      'AddTag': grpc.unary_unary_rpc_method_handler(
          servicer.AddTag,
          request_deserializer=datacatalog_dot_service__pb2.AddTagRequest.FromString,
          response_serializer=datacatalog_dot_service__pb2.AddTagResponse.SerializeToString,
      ),
      'ListArtifacts': grpc.unary_unary_rpc_method_handler(
          servicer.ListArtifacts,
          request_deserializer=datacatalog_dot_service__pb2.ListArtifactsRequest.FromString,
          response_serializer=datacatalog_dot_service__pb2.ListArtifactsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'datacatalog.DataCatalog', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
