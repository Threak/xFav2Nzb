xFav2Nzb
========

Retrieve your xRel.to favorite lists and search for all new releases on Usenet indexing sites. (xRel and some other providers require you to sign up)
Unfortunately the xRel-Api does not allow to mark individual releases as read (, or unread). Therefore you will have to manually untick each release after you are happy with the result.

*	The following indexing sites are currently used:
	*	NZBZombie.com
	*	NZBIndex.nl (no registration needed)
	*	NZBPlanet.net
*	Previusly supported and removed due to unavailability:
	*	nzbX.co

Please let me know if there are any sites which should be added. An Search-Api (json, xml/rss) providing nzb-links is mandatory.
Usage
-----
On first run you are asked to authenticate to xRel.to using OAuth2 (no need to enter your password in this application).
*	run auth_xrel.py one time and sign-in in your webbrowser, the generated keys get stored automatically
*	run get_fav.py every time you want to download nzbs for your releases, will ask for some api-keys as well

Settings
--------
Default directory for the config (get_fav.cfg, stores all Api-keys) and nzb download location is:
*	~/.get_fav

You can easily create accounts for the other sites if needed and paste their Api-key into the application. Afterwards they are queried until a result is found.
Uncomment those you don't want or which provide bogus results.

If more than one matching result is found you will get either a prompt if:
*	silent_dl is set to False,

or the first result is chosen automatically if:
*	silent_dl is set to True.
*	

NFO-Downloading
---------------
It is now possible to batch download missing nfo files. Two modus operanti are available:

*	get_nfo.py is called wihtout arguments
	*	it will search for media files in the current directory based on their extension (.avi, .mkv, .iso)
	*	names of matching files are used to search and retrieve their nfos
*	get_nfo.py is called directly with a space seperated list of dir names
*	*	e.g. get_nfo.py my.super.rel.2042.4000p.bluray.x264-platin your.crap.rel.1990.480p.tv.x264-wood

Todo
----
*	add more sites
*	cli for settings, maybe ask at first run
