webscreensaver
==============

A screen hack which uses WebKit and works with XScreensaver or XFCE.

Dependencies
------------

 * Python 3
 * xscreensaver or xfce4-screensaver
 * GTK3
 * WebKit2 gtk

On Ubuntu, try this command:

```
    sudo apt install python3 python3-gi gir1.2-webkit2-4.0 gir1.2-gtk-3.0
```

Install (XScreensaver)
----------------------

Copy `webscreensaver` into `/usr/lib/xscreensaver` and then edit `~/.xscreensaver`:

```
    programs:
                  webscreensaver                  \n\
```

If you wish to set the url:

```
    -url <url_to_the_page_you_want>
```

Otherwise it will choose a random one.

You can persist cookies by specifying a cookie file:

```
    -cookie-file <path_to_cookie_file>
```

*NOTE:* All parameters should be all on the same line as `webscreensaver`

Install (XFCE)
--------------

 1. Copy `webscreensaver` into `/usr/lib/xscreensaver`.
 2. Copy `webscreensaver.desktop` into `/usr/share/applications/screensavers`.

Sites List
----------

The list of sites chosen can be customised via a configuration file (TOML).

The format of the file is series of sections (one per site) as follows:

```
    [thisisasite]
    url = "http://abcd.efg"
    inject_css = "body { color: black }"
    remove_tags = ["header", "hullo"]
    remove_ids = ["hellohello", "heyhey"]
```

The `inject_css`, `remove_tags` and `remove_ids` keys are used to apply
customisations to the page after it has loaded. The value can be either
a single string or a list of strings.

 * `inject_css`  - the CSS string will be injected into the page.
 * `remove_tags` - all tags matching the specified tag name will be removed.
 * `remove_ids`  - all tags with the specified IDs will be removed.
