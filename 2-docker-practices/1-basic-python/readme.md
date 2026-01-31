# Docker Pratik 1 – Basic Python Container

Bu pratikte Docker’ın temel çalışma zinciri olan Dockerfile → Image → Container
akışı uygulanmıştır.

Amaç, Dockerfile yazarak basit bir Python uygulamasını image haline getirmek
ve bu image’dan çalışan bir container oluşturmaktır.

Bu aşamada herhangi bir framework veya ek servis kullanılmamıştır.
Odak noktası Docker’ın temel çalışma mantığıdır.

---

## Kullanılan Uygulama

Bu pratikte container içinde çalıştırılmak üzere basit bir Python script’i
kullanılmıştır.

Amaç, Python kodunun Docker container içinde doğru şekilde çalıştığını
doğrulamaktır. Uygulama çalıştığında terminale tek satırlık bir çıktı verir.

---

## Dockerfile Mantığı

Dockerfile, Python uygulamasının çalışacağı image’ın nasıl üretileceğini
tanımlar.

Bu dosyada sırasıyla şu adımlar uygulanmıştır:

- Python runtime içeren hafif bir base image seçilmiştir
- Container içinde çalışma dizini tanımlanmıştır
- Python dosyası image içine kopyalanmıştır
- Container başlatıldığında çalışacak varsayılan komut belirlenmiştir

Dockerfile satırları strict syntax’a sahiptir ve her satır image içinde
ayrı bir katman (layer) oluşturur.

---

## Kullanılan Docker Komutları

### Image Oluşturma (Build)

Dockerfile’ın bulunduğu dizinde aşağıdaki komut çalıştırılmıştır:

docker build -t python-basic .

Bu komut ile:
- Dockerfile okunur
- Image katman katman oluşturulur
- python-basic adında bir image üretilir

Build işlemi sonunda image hazır hale gelir ancak çalıştırılmaz.

---

### Container Çalıştırma (Run)

Oluşturulan image’dan container başlatmak için aşağıdaki komut kullanılmıştır:

docker run python-basic

Bu komut ile:
- Image’dan yeni bir container oluşturulur
- Dockerfile içindeki CMD talimatı çalıştırılır
- Python script’i container içinde çalışır

---

## Sonuç

Container başarıyla çalıştırıldığında terminalde aşağıdaki çıktı alınmıştır:

Hello from Docker Container!

Bu çıktı:
- Docker Engine’in doğru çalıştığını
- Image’ın başarıyla oluşturulduğunu
- Container’ın çalıştığını
- Python kodunun container içinde çalıştırıldığını

doğrulamaktadır.

---


Bu pratiğin çıktısını gösteren ekran görüntüsü aşağıdaki dosyada yer almaktadır:

screenshots/docker1.png

Bu ekran görüntüsünde Docker container’ın çalıştırılması ve çıktının terminalde
görülmesi yer almaktadır.

---


