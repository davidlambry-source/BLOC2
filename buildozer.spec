[app]
title = MonApplication
package.name = monapplication
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,mp3,wav

version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.sdk = 35
android.ndk = 25b
android.build_tools_version = 35.0.0

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.entrypoint = org.kivy.android.PythonActivity
android.enable_androidx = True
android.copy_libs = 1
android.archs = arm64-v8a, armeabi-v7a
android.logcat_filters = *:S python:D

presplash.color = #FFFFFF

[buildozer]
log_level = 2
warn_on_root = 1
