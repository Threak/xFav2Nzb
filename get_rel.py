#!/usr/bin/env python2

import os
import os.path
import sys
import urllib

from search_nzb import search_nzbsites
from font_colors import font_colors

#if true, choose first nzb if several found
silent_dl = True

#name of config file where all keys get stored
config_file = 'get_fav.cfg'
config_path = os.path.expanduser('~/.get_fav')

#directory where nzbs get stored
nzb_path = os.path.join(config_path, 'nzbs')

if not os.path.exists(config_path):
	os.makedirs(config_path)
config_file = os.path.join(config_path, config_file)

if len(sys.argv) < 2:
	rels = []
	user_in = raw_input('Enter releases to search:\n')
	while 1:
		if user_in == '':
			break
		else:
			rels.append(user_in)
			user_in = raw_input()
else:
	rels = sys.argv[1:]

new_dir = os.path.join(nzb_path, 'manual')
if not os.path.exists(new_dir):
	os.makedirs(new_dir)

if not rels == []:
	for rel in rels:
		nzb = search_nzbsites(rel, False, config_file)
		if nzb[0]==0:
			#print nzb[1]
			filename = '%(dirname)s_%(source)s_%(size)sMb.nzb' % {'dirname': rel, 'source': nzb[3], 'size': nzb[2]}
			urllib.urlretrieve(nzb[1], os.path.join(nzb_path, 'manual', filename))
			print font_colors.OKGREEN + '\t DL:' + filename + font_colors.ENDC
		else:
			print font_colors.FAIL + '\t ' + nzb[1] + font_colors.ENDC

#print search_nzbsites('DmC.Devil.may.Cry-RELOADED', False, config_file)
