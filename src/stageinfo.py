# -*- coding: utf-8 -*--

import config
import urllib2
import json
import codecs

class GetStageInfo:
	def __init__(self, url):
		self.json_ = self.openurl(url)

	def openurl(self, url):
		return json.loads(urllib2.urlopen(url).read(), "utf-8")

	def json(self):
		return self.json_


class StageInfo:
	def __init__(self, json_):
		self.src = json_[0]
		self.times = { 'begin':json_[0]['datetime_term_begin'], 'end':json_[0]['datetime_term_end'] }
		self.stagenames = ( json_[0]['stages'][0]['name'], json_[0]['stages'][1]['name'])



if __name__ == '__main__':

	sinfo = GetStageInfo(config.stageinfojson_url)
	a = StageInfo(sinfo.json())

	begin = a.times["begin"]
	end = a.times["end"]

	print a.times["begin"] + " ~ " + a.times["end"]
	print a.stagenames[0].encode("utf-8")
	print a.stagenames[1].encode("utf-8")

	begin.replace(':', '-')
	end.replace(':', '-')

	ww = open(config.logdir + begin + "_" + end + ".json", "w")
	enc = json.dumps(sinfo.json(), indent=4, ensure_ascii=False)
	ww.write(enc)

