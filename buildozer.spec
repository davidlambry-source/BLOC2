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

presplash.color = #FFFFFF

log_level = 2

warn_on_root = 1

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Enable AndroidX
android.enable_androidx = True

# (bool) Copy libs
android.copy_libs = 1

# (str) Android architecture
android.archs = arm64-v8a, armeabi-v7a

# (int) Android logcat filters
android.logcat_filters = *:S python:D

[buildozer]

log_level = 2

warn_on_root = 1
