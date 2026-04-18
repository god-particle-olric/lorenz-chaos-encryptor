import numpy as np

# lorenz'in kurallarını tanımlayalım
def lorenz_adim(x, y, z):
    s, r, b = 10, 28, 2.667
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot

# Başlangıç değerleri dif denk başlangıç değerleri gibi 
x0 = 0.1
y0 = 0.11
z0 = 0.1
dt = 0.01  # zaman adımı

mesaj = "Merhaba Olric!"  # şifrelenecek mesaj ve fyi olric is my lovely orange cat and one day if I had another cat I would name it Schrödinger because I love cats and Schrödinger's cat is a famous thought experiment in quantum mechanics that illustrates the concept of superposition and the uncertainty principle. It would be a fun and fitting name for a cat, especially one that has a mysterious or playful personality :))

# --- ŞİFRELEME ---
print(f"\n---Şifreleme Başlıyor ('{mesaj}' için)---")
x, y, z = x0, y0, z0
sifreli_mesaj_listesi = []

# burn-in: ilk 100 adımı atla (transient)
for _ in range(100):
    dx, dy, dz = lorenz_adim(x, y, z)
    x += dx * dt
    y += dy * dt
    z += dz * dt

# her karakter için bir adım ilerlet ve anahtar üret
for karakter in mesaj:
    dx, dy, dz = lorenz_adim(x, y, z)
    x += dx * dt
    y += dy * dt
    z += dz * dt

    anahtar = int(abs(x * 1000)) % 256
    ascii_degeri = ord(karakter)
    sifreli_sayi = (ascii_degeri ^ anahtar) % 256
    sifreli_mesaj_listesi.append(sifreli_sayi)
    print(f"Karakter '{karakter}' (ASCII: {ascii_degeri}) -> Anahtar: {anahtar} -> Şifreli Değer: {sifreli_sayi}")

# --- DEŞİFRELEME ---
print(f"\n---Deşifreleme Başlıyor---")
x, y, z = x0, y0, z0
cozulen_mesaj = ""

# aynı burn-in adımlarını uygula
for _ in range(100):
    dx, dy, dz = lorenz_adim(x, y, z)
    x += dx * dt
    y += dy * dt
    z += dz * dt

# şifreli listedeki her değeri aynı anahtarla XOR'la
for sifreli_deger in sifreli_mesaj_listesi:
    dx, dy, dz = lorenz_adim(x, y, z)
    x += dx * dt
    y += dy * dt
    z += dz * dt

    anahtar = int(abs(x * 1000)) % 256
    ascii_degeri = (sifreli_deger ^ anahtar) % 256
    harf_geri = chr(ascii_degeri) #chr fonksiyonu, verilen ASCII değerine karşılık gelen karakteri döndürür. misal, chr(65) 'A' karakterini verecek

    cozulen_mesaj += harf_geri
    print(f"Şifreli Değer: {sifreli_deger} -> Anahtar: {anahtar} -> ASCII Değeri: {ascii_degeri} -> Karakter: '{harf_geri}'")

# Final sonucu
print(f"\nOrijinal Mesaj: '{cozulen_mesaj}'")