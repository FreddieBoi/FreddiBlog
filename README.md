FreddiBlog
==========
FreddiBlog is a simple Django test app.

Coffeescript
------------
**Note**: I've been having some troubles with autocompiling coffeescript (on Windows 7). Code that should work should still be there, but is probably out-commented.

Instead I've created a command called `compile_coffee`. This will compile all **coffeescript** files from `static/coffee/*.coffee` into **javascript** files outputted to `static/js/*.js`.

To run the command: `python manage.py compile_coffee`

South Migrations
----------------
I haz it!

django-debug-toolbar
--------------------
The [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar "django-debug-toolbar") is used, except the `SQLDebugPanel` which gives me errors.
