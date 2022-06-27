# Pelican Attila Theme

A content focused responsive theme for [Pelican](https://github.com/getpelican/pelican).

It is ported from ghost theme [attila](https://github.com/zutrinken/attila)

## Demo

* [Blog](https://arulrajnet.github.io/attila-demo)
* [Post](https://arulrajnet.github.io/attila-demo/2015/11/headlines-blockquotes-images.html)
* [Tag Archive](https://arulrajnet.github.io/attila-demo/tag/general/)
* [Author Archive](https://arulrajnet.github.io/attila-demo/author/zutrinken/)
* [All archive](https://arulrajnet.github.io/attila-demo/archives.html)
* [Page](https://arulrajnet.github.io/attila-demo/pages/about/)

Demo blog [source code](https://github.com/arulrajnet/attila-demo)

## Features

* Responsive layout
* Navigation support
* Paralax cover images for posts, author archives and blog
* Author informations for posts and author archives
* Featured posts
* Reading progress for posts
* Automatic code syntax highlight
* Disqus support
* Sharing buttons

## Setup

Refer [more setting](https://github.com/arulrajnet/attila-demo/blob/master/pelicanconf.py)

All configurations about this theme.

#### Header Covers

To define custom header cover, set the property ``HEADER_COVER`` in ``pelicanconf.py``:

```python
HEADER_COVER = 'static/my_image.png'
```

#### Header Color

To define a simple header background color, set the property ``HEADER_COLOR`` in ``pelicanconf.py``:

```python
HEADER_COLOR = 'black'
```

you can use any valid css color.

#### Social URLs

Github, Twitter and Facebook URLs set these properties:

```python
SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
          ('github', 'https://github.com/myprofile'),
          ('facebook','https://facebook.com/myprofile'),
          ('flickr','https://www.flickr.com/myprofile/'),
          ('envelope','mailto:my@mail.address'))
```

#### External feed URL

You can specify an external feed URL (e.g. FeedBurner) in ``SOCIAL`` using the
``rss`` or ``rss-square`` or ``feed`` icons. A ``<link>`` tag for the external feed will be
placed in ``<head>`` instead of the default Pelican feeds.

#### Code highlights

This theme contains this color schemes:

 - Tomorrow - ``tomorrow.css``;
 - Tomorrow Night - ``tomorrow_night.css``;
 - Monokai - ``monokai.css``;
 - Github (Default) - ``github.css``;
 - Darkly - ``darkly.css``;

To customize, define ``COLOR_SCHEME_CSS`` in ``pelicanconf.py`` with css filename. Example:

```python
COLOR_SCHEME_CSS = 'monokai.css'
```

#### User defined CSS

Define ``CSS_OVERRIDE`` in ``pelicanconf.py`` to insert a user defined CSS file
after theme CSS. Example:

Array of CSS you can give

```python
CSS_OVERRIDE = ['css/myblog.css']
```

#### User defined script

```python
JS_OVERRIDE = ['']
```

#### Author Bio

```
AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken",
    "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "website": "http://blog.arulraj.net",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}
```

#### Analytics

Accept many analytics:

 - Google Analytics: ``GOOGLE_ANALYTICS``;
 - Gauges: ``GAUGES``
 - Piwik: ``PIWIK_URL`` and ``PIWIK_SITE_ID``.

#### Other configuration

 - ``GOOGLE_SITE_VERIFICATION`` - Google site verification token;
 - Set ``SHOW_FULL_ARTICLE`` to True to show full article content on index.html
 instead of summary;
 - Set ``FACEBOOK_ADMINS`` to a list of Facebook account IDs which are
 associated with this blog. For example ``['12345']``. For more info see
 https://developers.facebook.com/docs/platforminsights/domains

#### Articles

 - To customize header cover to articles, insert the metadata ``header_cover``.
 - To customize OpenGraph images, insert the metadata ``og_image``, otherwise
 ``header_cover``, ``HEADER_COVER`` or a default image is used.
 - To customize Twitter card images, insert the metadata ``twitter_image``,
 otherwise ``header_cover``, ``HEADER_COVER`` or a default image is used.
 Twitter cards are automatically generated if the ``twitter`` icon is configured
 in ``SOCIAL``!

All image paths are relative from the site root directory. You can also use
absolute URLs for ``og_image`` and ``twitter_image``.

## Development

refer this [https://github.com/arulrajnet/attila-demo](https://github.com/arulrajnet/attila-demo)

**Author Screen**
![screenshot](screenshot.png)

## Copyright & License

Copyright (c) 2015-2016 Peter Amende - Released under The MIT License.
Copyright (c) 2016 Arulraj V - Released under The MIT License.

Some background images used from https://github.com/gilsondev/pelican-clean-blog
