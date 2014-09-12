import sys, glob
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.dialog.ttypes import *
from livetex.operator.ttypes import *
from livetex.department.ttypes import *
from livetex.vote.ttypes import *

from livetex.presence import Presence

try:

  transport = THttpClient.THttpClient('http://localhost:10050/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = Presence.Client(protocol)
  
  transport.open()

  department = Department('56', 'some_name', { 'opt1': 'val1' })
  status = 'some_status'

  operators = client.getOperators(status)
  print 'getOperators is ok: ' + str(operators)[:50] + '...'

  departments = client.getDepartments(status)
  print 'getDepartments is ok: ' + str(departments)[:50] + '...'

  departmentOperators = client.getDepartmentOperators(department)
  print 'getDepartmentOpeartors is ok: ' + str(departmentOperators)[:50] + '...'


except Thrift.TException, tx:
  
  print '%s' % (tx.message)