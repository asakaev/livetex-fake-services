#
# Autogenerated by Thrift Compiler (0.9.1)
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
  def removeToken(self, token):
    """
    Parameters:
     - token
    """
    pass

  def checkToken(self, token):
    """
    Parameters:
     - token
    """
    pass

  def addEndpoints(self, serv, environment, endpoints):
    """
    Parameters:
     - serv
     - environment
     - endpoints
    """
    pass

  def removeEndpoints(self, serv, environment, endpoints):
    """
    Parameters:
     - serv
     - environment
     - endpoints
    """
    pass

  def getEndpoints(self, serv, environment):
    """
    Parameters:
     - serv
     - environment
    """
    pass

  def changeEnvironment(self, client, environment):
    """
    Parameters:
     - client
     - environment
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def removeToken(self, token):
    """
    Parameters:
     - token
    """
    self.send_removeToken(token)
    self.recv_removeToken()

  def send_removeToken(self, token):
    self._oprot.writeMessageBegin('removeToken', TMessageType.CALL, self._seqid)
    args = removeToken_args()
    args.token = token
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_removeToken(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = removeToken_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return

  def checkToken(self, token):
    """
    Parameters:
     - token
    """
    self.send_checkToken(token)
    return self.recv_checkToken()

  def send_checkToken(self, token):
    self._oprot.writeMessageBegin('checkToken', TMessageType.CALL, self._seqid)
    args = checkToken_args()
    args.token = token
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_checkToken(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = checkToken_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "checkToken failed: unknown result");

  def addEndpoints(self, serv, environment, endpoints):
    """
    Parameters:
     - serv
     - environment
     - endpoints
    """
    self.send_addEndpoints(serv, environment, endpoints)
    self.recv_addEndpoints()

  def send_addEndpoints(self, serv, environment, endpoints):
    self._oprot.writeMessageBegin('addEndpoints', TMessageType.CALL, self._seqid)
    args = addEndpoints_args()
    args.serv = serv
    args.environment = environment
    args.endpoints = endpoints
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_addEndpoints(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = addEndpoints_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return

  def removeEndpoints(self, serv, environment, endpoints):
    """
    Parameters:
     - serv
     - environment
     - endpoints
    """
    self.send_removeEndpoints(serv, environment, endpoints)
    self.recv_removeEndpoints()

  def send_removeEndpoints(self, serv, environment, endpoints):
    self._oprot.writeMessageBegin('removeEndpoints', TMessageType.CALL, self._seqid)
    args = removeEndpoints_args()
    args.serv = serv
    args.environment = environment
    args.endpoints = endpoints
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_removeEndpoints(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = removeEndpoints_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return

  def getEndpoints(self, serv, environment):
    """
    Parameters:
     - serv
     - environment
    """
    self.send_getEndpoints(serv, environment)
    return self.recv_getEndpoints()

  def send_getEndpoints(self, serv, environment):
    self._oprot.writeMessageBegin('getEndpoints', TMessageType.CALL, self._seqid)
    args = getEndpoints_args()
    args.serv = serv
    args.environment = environment
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getEndpoints(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getEndpoints_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getEndpoints failed: unknown result");

  def changeEnvironment(self, client, environment):
    """
    Parameters:
     - client
     - environment
    """
    self.send_changeEnvironment(client, environment)
    self.recv_changeEnvironment()

  def send_changeEnvironment(self, client, environment):
    self._oprot.writeMessageBegin('changeEnvironment', TMessageType.CALL, self._seqid)
    args = changeEnvironment_args()
    args.client = client
    args.environment = environment
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_changeEnvironment(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = changeEnvironment_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["removeToken"] = Processor.process_removeToken
    self._processMap["checkToken"] = Processor.process_checkToken
    self._processMap["addEndpoints"] = Processor.process_addEndpoints
    self._processMap["removeEndpoints"] = Processor.process_removeEndpoints
    self._processMap["getEndpoints"] = Processor.process_getEndpoints
    self._processMap["changeEnvironment"] = Processor.process_changeEnvironment

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

  def process_removeToken(self, seqid, iprot, oprot):
    args = removeToken_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = removeToken_result()
    self._handler.removeToken(args.token)
    oprot.writeMessageBegin("removeToken", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_checkToken(self, seqid, iprot, oprot):
    args = checkToken_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = checkToken_result()
    result.success = self._handler.checkToken(args.token)
    oprot.writeMessageBegin("checkToken", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_addEndpoints(self, seqid, iprot, oprot):
    args = addEndpoints_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = addEndpoints_result()
    self._handler.addEndpoints(args.serv, args.environment, args.endpoints)
    oprot.writeMessageBegin("addEndpoints", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_removeEndpoints(self, seqid, iprot, oprot):
    args = removeEndpoints_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = removeEndpoints_result()
    self._handler.removeEndpoints(args.serv, args.environment, args.endpoints)
    oprot.writeMessageBegin("removeEndpoints", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getEndpoints(self, seqid, iprot, oprot):
    args = getEndpoints_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getEndpoints_result()
    result.success = self._handler.getEndpoints(args.serv, args.environment)
    oprot.writeMessageBegin("getEndpoints", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_changeEnvironment(self, seqid, iprot, oprot):
    args = changeEnvironment_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = changeEnvironment_result()
    self._handler.changeEnvironment(args.client, args.environment)
    oprot.writeMessageBegin("changeEnvironment", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class removeToken_args:
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
    oprot.writeStructBegin('removeToken_args')
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

class removeToken_result:

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
    oprot.writeStructBegin('removeToken_result')
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

class checkToken_args:
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
    oprot.writeStructBegin('checkToken_args')
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

class checkToken_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (CheckTokenResult, CheckTokenResult.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = CheckTokenResult()
          self.success.read(iprot)
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
    oprot.writeStructBegin('checkToken_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
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

class addEndpoints_args:
  """
  Attributes:
   - serv
   - environment
   - endpoints
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'serv', None, None, ), # 1
    (2, TType.STRING, 'environment', None, None, ), # 2
    (3, TType.LIST, 'endpoints', (TType.STRUCT,(Endpoint, Endpoint.thrift_spec)), None, ), # 3
  )

  def __init__(self, serv=None, environment=None, endpoints=None,):
    self.serv = serv
    self.environment = environment
    self.endpoints = endpoints

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
          self.serv = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.environment = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.endpoints = []
          (_etype39, _size36) = iprot.readListBegin()
          for _i40 in xrange(_size36):
            _elem41 = Endpoint()
            _elem41.read(iprot)
            self.endpoints.append(_elem41)
          iprot.readListEnd()
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
    oprot.writeStructBegin('addEndpoints_args')
    if self.serv is not None:
      oprot.writeFieldBegin('serv', TType.STRING, 1)
      oprot.writeString(self.serv)
      oprot.writeFieldEnd()
    if self.environment is not None:
      oprot.writeFieldBegin('environment', TType.STRING, 2)
      oprot.writeString(self.environment)
      oprot.writeFieldEnd()
    if self.endpoints is not None:
      oprot.writeFieldBegin('endpoints', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.endpoints))
      for iter42 in self.endpoints:
        iter42.write(oprot)
      oprot.writeListEnd()
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

class addEndpoints_result:

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
    oprot.writeStructBegin('addEndpoints_result')
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

class removeEndpoints_args:
  """
  Attributes:
   - serv
   - environment
   - endpoints
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'serv', None, None, ), # 1
    (2, TType.STRING, 'environment', None, None, ), # 2
    (3, TType.LIST, 'endpoints', (TType.STRUCT,(Endpoint, Endpoint.thrift_spec)), None, ), # 3
  )

  def __init__(self, serv=None, environment=None, endpoints=None,):
    self.serv = serv
    self.environment = environment
    self.endpoints = endpoints

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
          self.serv = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.environment = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.endpoints = []
          (_etype46, _size43) = iprot.readListBegin()
          for _i47 in xrange(_size43):
            _elem48 = Endpoint()
            _elem48.read(iprot)
            self.endpoints.append(_elem48)
          iprot.readListEnd()
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
    oprot.writeStructBegin('removeEndpoints_args')
    if self.serv is not None:
      oprot.writeFieldBegin('serv', TType.STRING, 1)
      oprot.writeString(self.serv)
      oprot.writeFieldEnd()
    if self.environment is not None:
      oprot.writeFieldBegin('environment', TType.STRING, 2)
      oprot.writeString(self.environment)
      oprot.writeFieldEnd()
    if self.endpoints is not None:
      oprot.writeFieldBegin('endpoints', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.endpoints))
      for iter49 in self.endpoints:
        iter49.write(oprot)
      oprot.writeListEnd()
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

class removeEndpoints_result:

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
    oprot.writeStructBegin('removeEndpoints_result')
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

class getEndpoints_args:
  """
  Attributes:
   - serv
   - environment
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'serv', None, None, ), # 1
    (2, TType.STRING, 'environment', None, None, ), # 2
  )

  def __init__(self, serv=None, environment=None,):
    self.serv = serv
    self.environment = environment

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
          self.serv = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.environment = iprot.readString();
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
    oprot.writeStructBegin('getEndpoints_args')
    if self.serv is not None:
      oprot.writeFieldBegin('serv', TType.STRING, 1)
      oprot.writeString(self.serv)
      oprot.writeFieldEnd()
    if self.environment is not None:
      oprot.writeFieldBegin('environment', TType.STRING, 2)
      oprot.writeString(self.environment)
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

class getEndpoints_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Endpoint, Endpoint.thrift_spec)), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype53, _size50) = iprot.readListBegin()
          for _i54 in xrange(_size50):
            _elem55 = Endpoint()
            _elem55.read(iprot)
            self.success.append(_elem55)
          iprot.readListEnd()
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
    oprot.writeStructBegin('getEndpoints_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter56 in self.success:
        iter56.write(oprot)
      oprot.writeListEnd()
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

class changeEnvironment_args:
  """
  Attributes:
   - client
   - environment
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'client', (ClientEntity, ClientEntity.thrift_spec), None, ), # 1
    (2, TType.STRING, 'environment', None, None, ), # 2
  )

  def __init__(self, client=None, environment=None,):
    self.client = client
    self.environment = environment

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
        if ftype == TType.STRUCT:
          self.client = ClientEntity()
          self.client.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.environment = iprot.readString();
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
    oprot.writeStructBegin('changeEnvironment_args')
    if self.client is not None:
      oprot.writeFieldBegin('client', TType.STRUCT, 1)
      self.client.write(oprot)
      oprot.writeFieldEnd()
    if self.environment is not None:
      oprot.writeFieldBegin('environment', TType.STRING, 2)
      oprot.writeString(self.environment)
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

class changeEnvironment_result:

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
    oprot.writeStructBegin('changeEnvironment_result')
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
