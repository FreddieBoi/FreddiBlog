FreddiBlog
==========
FreddiBlog is a simple Django test app.

Coffeescript
------------
Note: I've been having some troubles with autocompiling coffeescript (on Windows 7). Code that should work is still there, but out-commented.

Instead I have created a command called `compile_coffee`. This will compile all `static/coffee/*.coffee` files into javascript and move them to `static/js/*.js`.

To run the command, type:
``python manage.py compile_coffee``
