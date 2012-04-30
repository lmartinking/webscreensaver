webscreensaver
==============

A screen hack which uses WebKit and works with XScreensaver

dependencies
------------

 * python 2.7
 * pywebkitgtk
 * pygtk (gtk 2)
 * xscreensaver

install
-------

Copy `webscreensaver` into `/usr/lib/xscreensaver` and then edit `~/.xscreensaver`:

    programs:
                  webscreensaver                  \n\

If you wish to set the url:

    -url <url_to_the_page_you_want>
    
Otherwise it will choose a random one.