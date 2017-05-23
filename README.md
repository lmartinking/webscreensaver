webscreensaver
==============

A screen hack which uses WebKit and works with XScreensaver

dependencies
------------

 * python 2.7
 * xscreensaver
 * GTK3
 * webkitgtk

in ubuntu following should be sufficient:

    apt install python2.7 gir1.2-webkit-0.3 xscreensaver python-gtk2

install
-------

Copy `webscreensaver` into `/usr/lib/xscreensaver` and then edit `~/.xscreensaver`:

    programs:                                       \
                  webscreensaver                  \n\

If you wish to set the url:

    -url <url_to_the_page_you_want>

Otherwise it will choose a random one.

You can persist cookies by specifying a cookie file:

    -cookie-file <path_to_cookie_file>

*NOTE:* All parameters should be all on the same line as `webscreensaver`

