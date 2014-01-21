import xbmc
import xbmcaddon
 
__addon__       = xbmcaddon.Addon(id='plugin.video.helloworld')
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
 
title = "Hello World 2"
text = "This is some text 2"
time = 5000  # ms
 
xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(title, text, time, __icon__))
