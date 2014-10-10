import sys, threading, os
sys.path.append('gen-py')


def runScript(fileName):
  os.system('python ' + fileName)

threads = []
files = [
  'authentication_private_run.py',
  'authentication_public_run.py',
  'dialog_run.py',
  'presence_run.py',
  'visitor_run.py'
]

for fileItem in files: 
  thread = threading.Thread(target=runScript, args=(fileItem,))
  thread.start()
  threads.append(thread)


for thread in threads:
  thread.join()