import oauth2 as oauth
import time
import json

def decode_json (resp):

	fav_dict = json.loads(resp)

	fav_list = []

	for fav in fav_dict['payload']:
		#print fav
		#if there are no releases in any list, the key 'releases' does not exist
		if ('releases' not in fav):
			continue
		if (fav['releases']):
			#print fav['releases']
			for dirname in fav['releases']:
				fav_list.append(dirname['dirname'])

	return fav_list

def get_new(list_id, config_file):
	with open(config_file, 'r') as f:
		config_dict = json.loads(f.read())

	config_xrel = config_dict['xrel']

	consumer_key = config_xrel['consumer_key']
	consumer_secret = config_xrel['consumer_secret']

	oauth_token = config_xrel['oauth_token']
	oauth_token_secret = config_xrel['oauth_token_secret']
	
	url = "http://api.xrel.to/api/favs/list_entries.json?id=%s&get_releases=true" % str(list_id)
	
	consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
	     
	token = oauth.Token(key=oauth_token, secret=oauth_token_secret)
	
	client = oauth.Client(consumer, token)
	
	resp, content = client.request(url)
	favs = content[11:-3]
	#print '---->' + favs + '<----'
	return decode_json(favs)

#print get_new(39)

#print decode_json(open('favs_list_entries', 'r').read()[11:-4])
