import urllib2
import json
import feedparser
import random
import time

def search_nzb(dirname, rss, silent_dl):
	rss = rss.replace(' ', '%20')
	d = feedparser.parse(rss)
	#print d
	entry_count = len(d.entries)
	retries = 0
	while (entry_count == 0 and retries < 10):
		if d['status'] != 503:
			try:
				print '>>>> %s <<<<' % d['feed']['error']['description']
			except:
				print '>>>> Error not 503 <<<<'
			break
		else:
			print '>>>> Error 503: retrying <<<<'
		retries += 1
		d = feedparser.parse(rss)
		entry_count = len(d.entries)
		time.sleep(.1 * retries)

	if (entry_count > 1):
		#user_input = -1
		#while ((user_input >= 0) & (user_input < entry_count)):
		i = 0
		for e in d.entries:
			print str(i) + '. ' + str(int(e.enclosures[0]['length'])/1024/1024) + ' Mb' + ': ' + e.title
			i = i+1
		user_input = '0'		
		if not silent_dl:
			user_input = raw_input('found %d entries, choose which one to dl: ' % i)
		if not user_input:
			return [3, 'skipping ' + dirname + ' for now']
		entry = int(user_input)
	else:
		entry = 0
		return [1,'nothing found for: ' + dirname]
		
	e = d.entries[entry]
	
	if (len(e.enclosures[0]) > 0):
		return [0, e.enclosures[0]['href'], str(int(e.enclosures[0]['length'])/1024/1024)]
	return [2,'nothing found for: ' + dirname]

def search_nzbsites(dirname, silent_dl, config_file):
	site_list = []

	with open(config_file, 'r') as f:
		config_dict = json.loads(f.read())
	
	config_changed = False
	if not silent_dl and not 'nzbzombie' in config_dict:
		user_input = raw_input('Enter your >nzbzombie< api key (or leave blank), ' +
			'visit:\nhttp://www.nzbzombie.com/api?t=register&email=%s@%s.de to register a new one:' % (random.randint(10,99), random.randint(10,99), ) )
		if user_input:
			config_dict['nzbzombie'] = {'key': user_input}
			config_changed = True
	if not silent_dl and not 'nzbplanet' in config_dict:
		user_input = raw_input('Enter your >nzbplanet< api key (or leave blank), ' + 
			'visit:\nhttp://www.nzbplanet.net/api?t=register&email=%s@%s.de to register a new one:' % (random.randint(10,99), random.randint(10,99), ) )
		if user_input:
			config_dict['nzbplanet'] = {'key': user_input}
			config_changed = True
	if config_changed:
		with open(config_file, 'w') as f:
			f.write(json.dumps(config_dict, indent=2))

	if 'nzbzombie' in config_dict:
		nzbzombie = {
			'url': 'http://www.nzbzombie.com/api?apikey=%s&t=search&q=%s',
			'key': config_dict['nzbzombie']['key'],
			'name':'nzbzombie',
		}
		#site_list.append(nzbzombie)
	#for more trustworthy results search for town.ag uploads
	nzbindex_townag = {
		'url': 'https://www.nzbindex.com/rss/?q=%s town.ag&max=25&sort=sizedesc&complete=1&hidespam=1&nzblink=1',
		'name':'nzbindex-townag',
	}
	site_list.append(nzbindex_townag)
	nzbindex = {
		'url': 'https://www.nzbindex.com/rss/?q=%s&max=25&sort=sizedesc&complete=1&hidespam=1&more=1&nzblink=1',
		'name':'nzbindex',
	}
	site_list.append(nzbindex)
	if 'nzbplanet' in config_dict:
		nzbplanet = {
			'url': 'http://www.nzbplanet.net/api?apikey=%s&t=search&q=%s',
			'key': config_dict['nzbplanet']['key'],
			'name':'nzbplanet',
		}
		site_list.append(nzbplanet)

	for site in site_list:
		if 'key' in site:
			site['rss'] = site['url'] % (site['key'], dirname, )
		else:
			site['rss'] = site['url'] % (dirname, )

	i = 1
	for site in site_list:
		print '%d. try: %s' % (i, site['name'])
		#print site['rss']
		i += 1
		ret_val = search_nzb(dirname, site['rss'], silent_dl)
		if (ret_val[0] in (0, 3)):
			ret_val.append(site['name'])
			return ret_val
	return [2,'nothing found for: ' + dirname]


def open_json(full):

	try:
		fav_dict = json.loads(full)
	except ValueError:
		print full
		exit(-1)

	return fav_dict[0]
