import subprocess
import os

# Şifremizi belirliyoruz (bu şifreyi istediğiniz gibi değiştirebilirsiniz)
dogrusifre = "3535"

# Kullanıcıdan şifre alıyoruz
def ask_for_sifre():
    print("Şifre isteniyor...")  # Kontrol mesajı
    sifre = input("Uygulamayı açmak için şifreyi girin: ")
    return sifre

# Şifre kontrolü yapıyoruz
def sifre_denetle(sifre):
    return sifre == dogrusifre

# Masaüstündeki WhatsApp kısayolunu kullanarak uygulamayı başlatıyoruz
def launch_application():
    try:
        print("WhatsApp açılıyor...")  # Kontrol mesajı
        subprocess.run([r"C:\Users\derin\Desktop\app\WhatsApp.lnk"], shell=True)  # Masaüstündeki kısayolun tam yolunu yazın ya da uygulama neredeyse
    except FileNotFoundError:
        print("Uygulama bulunamadı.")
    except Exception as e:
        print(f"Uygulama başlatılamadı: {e}")

# Ana fonksiyon
def main():
    sifre = ask_for_sifre()
    if sifre_denetle(sifre):
        print("Şifre doğru, uygulama açılıyor...")
        launch_application()
    else:
        print("Hatalı şifre! Uygulama açılmadı.")

if __name__ == "__main__":
    main()