#!/usr/bin/env python2

import oauth2 as oauth
import time
import json
import urllib
import os
import os.path
import glob #for wildcard file exists check
import sys

from get_new import get_new
from search_nzb import search_nzbsites
from font_colors import font_colors

#name of config file where all keys get stored
config_file = 'get_fav.cfg'
config_path = os.path.expanduser('~/.get_fav')

#directory where nzbs get stored
nzb_path = os.path.join(config_path, 'nzbs')

if not os.path.exists(config_path):
	os.makedirs(config_path)
config_file = os.path.join(config_path, config_file)

def decode_x (resp, x):

	fav_dict = json.loads(resp)

	fav_list = []

	for fav in fav_dict['payload']:
		fav_list.append(fav[x])
	return fav_list

try:
	with open(config_file, 'r') as f:
		config_dict = json.loads(f.read())
except IOError:
	print 'please run auth_xrel first'
	exit(-42)

#for key in config_dict:
#	print '%s: %s' % (key, config_dict[key], )

config_xrel = config_dict['xrel']

consumer_key = config_xrel['consumer_key']
consumer_secret = config_xrel['consumer_secret']

oauth_token = config_xrel['oauth_token']
oauth_token_secret = config_xrel['oauth_token_secret']

#if true, choose first nzb if several found
silent_dl = True

url = "http://api.xrel.to/api/favs/lists.json"

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
     
token = oauth.Token(key=oauth_token, secret=oauth_token_secret)

client = oauth.Client(consumer, token)

resp, content = client.request(url)
#print resp

names = decode_x(content[11:-3], 'name')
for name in names:
	new_dir = os.path.join(nzb_path, name)
	#print new_dir
	if not os.path.exists(new_dir):
		os.makedirs(new_dir)

i = 0;
for list_id in decode_x(content[11:-3], 'id'):
	print font_colors.HEADER + names[i] + font_colors.ENDC
	#print list_id
	for dirname in get_new(list_id, config_file):
		test_name = os.path.join(nzb_path, names[i], dirname + '_*_*Mb.nzb')
		print 'searching for: %s' % dirname 
		disk_file = glob.glob(test_name)
		if len(disk_file) == 0:
			nzb = search_nzbsites(dirname, silent_dl, config_file)
			#print nzb
			if (nzb[0] == 0):
				#TODO: check filenames, they may contain illegal characters
				filename = os.path.join(nzb_path, names[i], dirname + '_' + nzb[3] + '_' + nzb[2] + 'Mb.nzb')
				#print nzb[1]
				urllib.urlretrieve(nzb[1], filename)
				print font_colors.OKGREEN + '\t DL:' + filename + font_colors.ENDC
			else:
				print font_colors.FAIL + '\t ' + nzb[1] + font_colors.ENDC
		else:
			print font_colors.WARNING + '\t' + disk_file[0] + ' already exists' + font_colors.ENDC		
	i = i+1

#print decode_id(open('favs_lists', 'r').read()[11:-4])
