import sys, glob, time
sys.path.append('gen-py')

from livetex.dialog.ttypes import *
from livetex.operator.ttypes import *

class ClientDialogHandler:
  def dialog(self):
    pass
  def close(self):
    pass
  def member(self, operator):
    pass
  def ban(self, message):
    pass
  def receiveFileMessage(self, message):
    pass
  def receiveTextMessage(self, message):
    pass
  def confirmTextMessage(self, message):
    pass
  def receiveHoldMessage(self, message):
    pass
  def receiveTypingMessage(self, message):
    pass

