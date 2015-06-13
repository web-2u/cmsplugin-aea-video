# -*- coding: utf-8 -*-

from django.conf import settings

VIDEO_WIDTH = getattr(settings, "VIDEO_WIDTH", 600)
VIDEO_HEIGHT = getattr(settings, "VIDEO_HEIGHT", 450)

VIDEO_AUTOPLAY = getattr(settings, "VIDEO_AUTOPLAY", False)
VIDEO_AUTOHIDE = getattr(settings, "VIDEO_AUTOHIDE", False)
VIDEO_FULLSCREEN = getattr(settings, "VIDEO_FULLSCREEN", True)
VIDEO_LOOP = getattr(settings, "VIDEO_LOOP", False)
ASPECT_RATIO = getattr(settings, "ASPECT_RATIO", (('16by9', '16:9'), ('4by3', '4:3'),))
