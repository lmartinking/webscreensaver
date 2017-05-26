#!/usr/bin/env python
import sys
import signal

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GdkX11', '3.0')
gi.require_version('WebKit', '3.0')
gi.require_version('Soup', '2.4')
from gi.repository import Gtk, Gdk, GdkX11, GObject, Soup, WebKit

cookie_jar="/home/schueller/.webscreensaver-cookies"


view = WebKit.WebView() 
sw = Gtk.ScrolledWindow() 
sw.add(view) 

#win = Gtk.Window(Gtk.WindowType.TOPLEVEL) 
win = Gtk.Window() 
win.set_default_size(800,600)
view.set_size_request(800,600)
win.add(sw) 
win.show_all() 

#cookiejar = Soup.CookieJar.new()
cookiejar = Soup.CookieJarText.new(cookie_jar, False)
cookiejar.set_accept_policy(Soup.CookieJarAcceptPolicy.ALWAYS)
session = WebKit.get_default_session()
session.add_feature(cookiejar)

def terminate(*args):
	Gtk.main_quit()

win.connect('destroy', terminate)
win.connect('delete-event', terminate)

signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGTERM, terminate)

win.show_all()
Gdk.Window.process_all_updates()

url = sys.argv[1]
print(url)
view.open(url) 
Gtk.main()

# automatic saving with CookieJarText does not work - so I'll do it
jar = open(cookie_jar, "a")

for c in cookiejar.get_cookie_list(Soup.URI.new(url), True):
  expiry = "-1" if c.get_expires() is None else c.get_expires()
  if type(expiry) is Soup.Date:
    expiry = expiry.to_time_t()
  jar.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n".format(c.get_domain(), not c.get_secure(), c.get_path(), c.get_secure(), expiry, c.get_name(), c.get_value()))
jar.close()

