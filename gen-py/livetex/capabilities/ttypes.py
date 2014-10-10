# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Capabilities:
  """
  Список доступных возможностей клиента.


  CHAT: поддержка начала чата и обмена сообщениями.

  LEAD: поддержка работы с лидами.

  CALL: поддержка возможности совершить звонок.

  INVITATION: поддержка обработки приглашения в диалог.

  COBROWSE: поддердка возможности "Виртуальный Ассистент".

  FILES_RECEIVE: поддержка приема файлов.

  FILES_SEND: поддержка передачи файлов.
  """
  CHAT = 0
  LEAD = 1
  CALL = 2
  INVITATION = 3
  COBROWSE = 4
  FILES_RECEIVE = 5
  FILES_SEND = 6

  _VALUES_TO_NAMES = {
    0: "CHAT",
    1: "LEAD",
    2: "CALL",
    3: "INVITATION",
    4: "COBROWSE",
    5: "FILES_RECEIVE",
    6: "FILES_SEND",
  }

  _NAMES_TO_VALUES = {
    "CHAT": 0,
    "LEAD": 1,
    "CALL": 2,
    "INVITATION": 3,
    "COBROWSE": 4,
    "FILES_RECEIVE": 5,
    "FILES_SEND": 6,
  }

