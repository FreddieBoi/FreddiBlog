FreddiBlog
==========
FreddiBlog is a simple Django test app.

South Migrations
----------------
[South](http://south.aeracode.org/ "South") is used for schema and data migrations. The documentation is over [here](http://south.aeracode.org/docs/index.html "South docs").

django-debug-toolbar
--------------------
The [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar "django-debug-toolbar") is used, except the `SQLDebugPanel` which gives me errors.

coffeescript
------------
_**Note**: I've been having some troubles with autocompiling **coffeescript** (on Windows 7). Code that should work should still be there, but is probably out-commented. See [django-coffeescript](https://github.com/andreyfedoseev/django-coffeescript "django-coffeescript") for this approach._

I've created a command called `compile_coffee`. This will compile all **coffeescript** files from `static/coffee/*.coffee` into **javascript** files outputted to `static/js/*.js`.

To run the command: `python manage.py compile_coffee`
