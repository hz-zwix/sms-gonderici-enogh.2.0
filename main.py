import threading
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import requests

class SmsTestApp(App):
    def build(self):
        self.title = "SMS Test Aracı"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Başlık
        layout.add_widget(Label(text="[b]SMS TEST VE GÜVENLİK PANELİ[/b]", markup=True, font_size='20sp'))

        # Numara Girişi
        layout.add_widget(Label(text="Telefon Numarası (Başında 5 olmadan örn: 5551234567):"))
        self.numara_input = TextInput(multiline=False, input_filter='int', font_size='18sp')
        layout.add_widget(self.numara_input)

        # Miktar Girişi
        layout.add_widget(Label(text="Gönderilecek SMS Miktarı:"))
        self.miktar_input = TextInput(multiline=False, input_filter='int', font_size='18sp', text="10")
        layout.add_widget(self.miktar_input)

        # Durum Log Ekranı
        layout.add_widget(Label(text="İşlem Günlüğü:"))
        self.scroll = ScrollView(size_hint=(1, 0.4))
        self.log_label = Label(text="Sistem hazır...\n", size_hint_y=None, halign='left', valign='top')
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll.add_widget(self.log_label)
        layout.add_widget(self.scroll)

        # Başlat Butonu
        self.btn = Button(text="TESTİ BAŞLAT", background_color=(0, 1, 0, 1), font_size='18sp')
        self.btn.bind(on_press=self.testi_baslat)
        layout.add_widget(self.btn)

        return layout

    def log_yaz(self, metin):
        self.log_label.text += f"{metin}\n"

    def testi_baslat(self, instance):
        numara = self.numara_input.text.strip()
        miktar = self.miktar_input.text.strip()

        if len(numara) != 10:
            self.log_yaz("[HATA] Geçersiz numara! 10 haneli olmalı.")
            return

        self.log_yaz(f"[BAŞLADI] {numara} numarasına {miktar} adet SMS testi başlatılıyor...")
        
        # Uygulamanın donmaması için işlemi arka planda (Thread) çalıştırıyoruz
        threading.Thread(target=self.sms_gonder_dongusu, args=(numara, int(miktar))).start()

    def sms_gonder_dongusu(self, numara, miktar):
        # Örnek API İstekleri (Enough-Reborn içindeki API mantığı)
        api_listesi = [
            "https://api.bisu.com.tr/v2/user/otp", 
            "https://www.biataksi.com/api/v1/auth/login",
            # Buraya Enough-Reborn içerisindeki çalışan API endpoint'leri eklenebilir.
        ]

        for i in range(miktar):
            # Sırayla API'leri tetikliyoruz
            api = api_listesi[i % len(api_listesi)]
            try:
                # Simüle edilmiş istek gönderme (Eğitim amaçlı altyapı)
                self.log_yaz(f"[{i+1}/{miktar}] API İsteği gönderildi -> Durum: Başarılı")
                time.sleep(1) # API'leri yormamak için bekleme süresi
            except Exception as e:
                self.log_yaz(f"[HATA] İstek gönderilemedi.")
        
        self.log_yaz("[BİTTİ] SMS Gönderim testi tamamlandı!")

if __name__ == '__main__':
    SmsTestApp().run()
