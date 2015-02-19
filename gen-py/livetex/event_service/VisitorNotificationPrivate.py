# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  """
  Приватные методы сервиса оповещений посетителя о событиях.
  """
  def destroyConnection(self, token):
    """
    Принудительный разрыв постоянного соединения.


    token: уникальный идентификатор клиента.

    Parameters:
     - token
    """
    pass

  def addDestroyListener(self, token, endpoint):
    """
    Подпись на оповещение о разрыве постоянного соединения.

    token: уникальный идентификатор клиента.

    endpoint: точка входа сервиса обработки оповещения разрыва постоянного соединения.
      Реализует интерфейс DestroyHandler.
      WARNING: Дополнительные ограничения на передаваемый endpoint: доступное
      значение поля service LivetexService.DESTROY_HANDLER

    Parameters:
     - token
     - endpoint
    """
    pass

  def write(self, token, rawData):
    """
    Передача данных клиенту.

    token: уникальный идентификатор клиента.

    rawData: данные передаваемые клиенту.

    Parameters:
     - token
     - rawData
    """
    pass


class Client(Iface):
  """
  Приватные методы сервиса оповещений посетителя о событиях.
  """
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def destroyConnection(self, token):
    """
    Принудительный разрыв постоянного соединения.


    token: уникальный идентификатор клиента.

    Parameters:
     - token
    """
    self.send_destroyConnection(token)
    self.recv_destroyConnection()

  def send_destroyConnection(self, token):
    self._oprot.writeMessageBegin('destroyConnection', TMessageType.CALL, self._seqid)
    args = destroyConnection_args()
    args.token = token
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_destroyConnection(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = destroyConnection_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return

  def addDestroyListener(self, token, endpoint):
    """
    Подпись на оповещение о разрыве постоянного соединения.

    token: уникальный идентификатор клиента.

    endpoint: точка входа сервиса обработки оповещения разрыва постоянного соединения.
      Реализует интерфейс DestroyHandler.
      WARNING: Дополнительные ограничения на передаваемый endpoint: доступное
      значение поля service LivetexService.DESTROY_HANDLER

    Parameters:
     - token
     - endpoint
    """
    self.send_addDestroyListener(token, endpoint)
    self.recv_addDestroyListener()

  def send_addDestroyListener(self, token, endpoint):
    self._oprot.writeMessageBegin('addDestroyListener', TMessageType.CALL, self._seqid)
    args = addDestroyListener_args()
    args.token = token
    args.endpoint = endpoint
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_addDestroyListener(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = addDestroyListener_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return

  def write(self, token, rawData):
    """
    Передача данных клиенту.

    token: уникальный идентификатор клиента.

    rawData: данные передаваемые клиенту.

    Parameters:
     - token
     - rawData
    """
    self.send_write(token, rawData)
    self.recv_write()

  def send_write(self, token, rawData):
    self._oprot.writeMessageBegin('write', TMessageType.CALL, self._seqid)
    args = write_args()
    args.token = token
    args.rawData = rawData
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_write(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = write_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["destroyConnection"] = Processor.process_destroyConnection
    self._processMap["addDestroyListener"] = Processor.process_addDestroyListener
    self._processMap["write"] = Processor.process_write

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_destroyConnection(self, seqid, iprot, oprot):
    args = destroyConnection_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = destroyConnection_result()
    self._handler.destroyConnection(args.token)
    oprot.writeMessageBegin("destroyConnection", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_addDestroyListener(self, seqid, iprot, oprot):
    args = addDestroyListener_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = addDestroyListener_result()
    self._handler.addDestroyListener(args.token, args.endpoint)
    oprot.writeMessageBegin("addDestroyListener", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_write(self, seqid, iprot, oprot):
    args = write_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = write_result()
    self._handler.write(args.token, args.rawData)
    oprot.writeMessageBegin("write", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class destroyConnection_args:
  """
  Attributes:
   - token
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'token', None, None, ), # 1
  )

  def __init__(self, token=None,):
    self.token = token

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.token = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('destroyConnection_args')
    if self.token is not None:
      oprot.writeFieldBegin('token', TType.STRING, 1)
      oprot.writeString(self.token)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class destroyConnection_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('destroyConnection_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class addDestroyListener_args:
  """
  Attributes:
   - token
   - endpoint
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'token', None, None, ), # 1
    (2, TType.STRUCT, 'endpoint', (livetex.endpoint.ttypes.Endpoint, livetex.endpoint.ttypes.Endpoint.thrift_spec), None, ), # 2
  )

  def __init__(self, token=None, endpoint=None,):
    self.token = token
    self.endpoint = endpoint

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.token = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.endpoint = livetex.endpoint.ttypes.Endpoint()
          self.endpoint.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('addDestroyListener_args')
    if self.token is not None:
      oprot.writeFieldBegin('token', TType.STRING, 1)
      oprot.writeString(self.token)
      oprot.writeFieldEnd()
    if self.endpoint is not None:
      oprot.writeFieldBegin('endpoint', TType.STRUCT, 2)
      self.endpoint.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class addDestroyListener_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('addDestroyListener_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class write_args:
  """
  Attributes:
   - token
   - rawData
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'token', None, None, ), # 1
    (2, TType.STRING, 'rawData', None, None, ), # 2
  )

  def __init__(self, token=None, rawData=None,):
    self.token = token
    self.rawData = rawData

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.token = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.rawData = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('write_args')
    if self.token is not None:
      oprot.writeFieldBegin('token', TType.STRING, 1)
      oprot.writeString(self.token)
      oprot.writeFieldEnd()
    if self.rawData is not None:
      oprot.writeFieldBegin('rawData', TType.STRING, 2)
      oprot.writeString(self.rawData)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class write_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('write_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)