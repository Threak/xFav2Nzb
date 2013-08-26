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

Default directory for the config (get_fav.cfg, stores all Api-keys) and nzb download location is ~/.get_fav. On first run you are asked to authenticate to xRel.to using OAuth2 (no need to enter your password in this application).
You can easily create accounts for the other sites if needed and paste their Api-key into the application. Afterwards they are queried until a result is found.

If more than one matching result is found you will get a prompt (silent_dl set to False) or the first result is chosen automatically (silent_dl set to True).
