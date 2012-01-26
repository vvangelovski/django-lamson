django-lamson
===================

The purpose of this django application is to integrate The Lamson Mail Server(TM) within existing django projects. It is currently geared towards projects that need to receive email. It provides management commands for starting/stopping the lamson daemon and the ability to configure the daemon from your django project settings module. The purpose is to eliminate multiple configuration points and to ease off the deployment and distribution of your django project.


Installation
===================

Install with pip or easy_install:

    pip install django-lamson

    easy_install django-lamson

Add ``django-lamson`` to your installed apps list in your settings.py



Usage example
===================

For an example project using this application please look at the ``testproject`` folder within the app sourcecode.