#!/bin/env python2

import urllib2
import sys
import glob
import os

def get_from(source, release):
	if source == 'srrdb':
		req = urllib2.Request('http://www.srrdb.com/release/details/%s' % release)
		try:
			res = urllib2.urlopen(req)
		except urllib2.URLError as e:
			print '%s: %s' % (release, e.reason, )
			return
		html = res.read()
		start = html.find('/download/file/%s/' % release)
		end = html.find('.nfo', start)
		nfo = 'http://www.srrdb.com%s' % html[start:end+4]
		return nfo

def get_nfos(release_list):
	nfo_urls = []
	for release in release_list:
		nfo = get_from('srrdb', release)
		if nfo:
			nfo_urls.append(nfo)
	if nfo_urls:
		cmd = 'wget -N -nv %s' % " ".join(nfo_urls)
		#print cmd
		os.system(cmd)

filetypes = ['.mkv', '.avi', '.mp4', '.iso']
if len(sys.argv) >= 2:
	releases = []
	for rel in sys.argv[1:]:
		releases.append(rel)
	get_nfos(releases)
else:
	print 'searching in current directory for: %s' % "; ".join(filetypes)
	releases = []
	for filetype in filetypes:
		for file in glob.iglob('*%s' % filetype):
			releases.append(file[:-4])
	get_nfos(list(set(releases)))
