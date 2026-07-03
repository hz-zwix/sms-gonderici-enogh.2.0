[app]

# (string) Uygulamanın telefonda görünecek adı
title = EnoughReborn Mobile

# (string) Uygulamanın paket adı (sadece küçük harf ve İngilizce karakterler)
package.name = enoughreborn

# (string) Uygulamanın domain adresi (paket kimliği için)
package.domain = org.tingirifistik

# (string) Ana kodların bulunduğu dizin (. geçerli dizindir)
source.dir = .

# (list) Projene dahil edilecek dosya uzantıları
source.include_exts = py,png,jpg,kv,atlas

# (string) Uygulama versiyonu
version = 1.0

# (list) Uygulamanın çalışması için gerekli kütüphaneler (KRİTİK ALAN)
# Python içindeki 'requests' kütüphanesinin Android'de çalışması için alt bağımlılıkları da eklenmelidir.
requirements = python3,kivy,requests,urllib3,idna,certifi,charset-normalizer

# (string) Ekran yönü (landscape, portrait veya all)
orientation = portrait

# (bool) Uygulama tam ekran mı olsun? (0 = Hayır, 1 = Evet)
fullscreen = 0

# ==========================================
# Android'e Özel Ayarlar
# ==========================================

# (list) Uygulamanın isteyeceği izinler (İnternet bağlantısı için şarttır)
android.permissions = INTERNET

# (int) Hedef Android API seviyesi (Boş bırakılırsa Buildozer en güncelini seçer)
# android.api = 33

# (int) Minimum desteklenen Android API seviyesi
android.minapi = 21

# (list) Desteklenecek işlemci mimarileri (Modern telefonlar için arm64-v8a şarttır)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Uygulama verilerinin Google Drive'a yedeklenmesine izin verilsin mi?
android.allow_backup = True

# (string) Uygulama ikonu (Eğer elinde bir icon.png varsa başındaki # işaretini kaldırabilirsin)
# icon.filename = %(source.dir)s/icon.png

[buildozer]
# (int) Log seviyesi (2 = Her şeyi gösterir, hata çözmek için en iyisidir)
log_level = 2

# (int) Buildozer hata durumunda işlemi durdursun mu?
warn_on_root = 1
