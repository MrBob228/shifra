[app]
title = Shifra
package.name = shifra_app
package.domain = org.shifra
source.dir = .
source.include_exts = py,png,ttf
version = 1.0
requirements = python3,kivy
icon.filename = icon2.png
fullscreen = 1
orientation = portrait
presplash.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 0
android.api = 33
android.minapi = 21
android.ndk = 23b
android.arch = armeabi-v7a
android.permissions = INTERNET
