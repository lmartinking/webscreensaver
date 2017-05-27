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

    sudo apt install python2.7 gir1.2-webkit-0.3 xscreensaver python-gtk2

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

config
------
You can create the config file `~/.config/webscreensaver` where you have even more options and you can also arrange _multiple_ web pages.
e.g.
```
{ "move" : true
, "force_reload_time": 120
, "cookie_file_readonly": true
, "cookie_file": "~/.webscreensaver-cookies"
, "url" : "https://c.xkcd.com/random/comic"
}

```

or two web pages

```
{ "move" : true
, "force_reload_time": 120
, "cookie_file_readonly": true
, "cookie_file": "~/.webscreensaver-cookies"
, "url" : { "vertical": true
          , "split_percentage": 50
          , "url1": "https://c.xkcd.com/random/comic/"
          , "url2": "http://www.nichtlustig.de"
          }
}
```

or even three
```
{ "move" : true
, "force_reload_time": 120
, "cookie_file_readonly": true
, "cookie_file": "~/.webscreensaver-cookies"
, "url" : { "vertical": true
          , "split_percentage": 50
          , "url1": { "vertical": false
                    , "split_percentage": 50
                    , "url1": "https://c.xkcd.com/random/comic/"
                    , "url2": "https://en.wikipedia.org"
                    }
          , "url2": "http://www.nichtlustig.de"
          }
}
```