import sys
import os
try:
    import json
except ImportError:
    import simplejson as json
import solr
import fp
import fileinput
from threading import Thread

class Unbuffered:
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

import sys
sys.stdout=Unbuffered(sys.stdout)
sys.stdin=Unbuffered(sys.stdin)


def match(fileName,code):
    response = fp.best_match_for_query(code)
    track_info = {key: value for key, value in response.metadata.items()
                 if key != "import_date"}
    if "track_id" in track_info.keys():
        track_info["track_id"] = track_info["track_id"].split("-")[0]

    print json.dumps({"ok":True, "query":code, "message":response.message(), "match":response.match(), "score":response.score, \
                     "qtime":response.qtime, "track_id":response.TRID, "total_time":response.total_time, "track_info":track_info, "file_name": fileName})
    sys.stdout.flush()

while(True):
    line = sys.stdin.readline()
    (fileName, code) = line.rstrip().split("|")
    # match(fileName, code)
    # print code
    Thread(target=match, args=[fileName,code]).start()
