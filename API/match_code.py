import sys
import os
try:
    import json
except ImportError:
    import simplejson as json
import fp
from threading import Thread

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
    Thread(target=match, args=[fileName,code]).start()
