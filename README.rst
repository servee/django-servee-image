Django-servee-image is a more complete image application than the one in the django-servee example project

It requires django-easy-thumbnails so that images can easily be resized on the fly.  It also very simple ways
of overwriting the upload_to and the default_storage via these two options in your settings.py

Also note, the default settings should suffice, and these are not required.

SERVEE_INSERT_STORAGE_CLASS
SERVEE_IMAGE_INSERT_UPLOAD_TO

There are no views or URLS for this project, it uses the default views, urls, and forms of the Servee ModelInsert class.


To try it out:

1.   Download the project.
2.   run python setup.py develop [requires django-servee=>0.6 which is trunk, not in PyPI]
3.   cd example_project
4.   python manage.py syncdb
5.   python manage.py runserver
6.   http://localhost:8000/login/
7.   Click "edit flatpage"
8.   Put your cursor in the wysiwyg window
9.   Click the "add button" at the bottom left of the wysiwyg toolbar and click "image"
10.  Upload an image from your computer
11.  Click the image, then place it in your editor.