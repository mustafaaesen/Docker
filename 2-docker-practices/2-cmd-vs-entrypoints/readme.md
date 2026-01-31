# Docker Pratik 2 – CMD ve ENTRYPOINT Davranışı

Bu pratikte Docker container’ların nasıl çalıştırıldığını ve çalışma davranışının
Dockerfile içindeki CMD ve ENTRYPOINT tanımlarına göre nasıl değiştiği
uygulamalı olarak incelenmiştir.

Amaç, bir container’ın neden “program gibi” davrandığını ve docker run komutu ile
bu davranışın nasıl yönlendirilebildiğini anlamaktır.

---

## Kullanılan Uygulama

Bu pratikte container içinde çalıştırılan Python uygulaması, çalıştığında
kendisine iletilen parametreleri terminale yazdırmaktadır.

Bu sayede docker run komutu ile gönderilen argümanların container içinde
nasıl ele alındığı net şekilde gözlemlenmiştir.

---

## CMD Kullanımı

İlk aşamada Dockerfile içinde CMD tanımı kullanılmıştır.

CMD, container başlatıldığında çalışacak varsayılan komutu ifade eder.
docker run komutu ile yeni bir komut verildiğinde CMD tamamen override edilir.

Bu durumda Dockerfile içindeki CMD devre dışı kalır ve docker run ile verilen
komut çalıştırılır.

CMD kullanımı ile yapılan çalışmada:
- Container varsayılan komut ile çalıştırılmış
- Ardından docker run ile yeni komut verilerek davranış değiştirilmiştir

CMD override davranışını gösteren terminal çıktısı aşağıdaki görselde yer almaktadır:

screenshots/dockercmd-cmdoverride.png

---

## ENTRYPOINT Kullanımı

İkinci aşamada Dockerfile içindeki CMD tanımı ENTRYPOINT ile değiştirilmiştir.

ENTRYPOINT, container’ın ana çalıştırma sürecini tanımlar.
docker run ile verilen argümanlar ENTRYPOINT’i değiştirmez, yalnızca parametre
olarak eklenir.

Bu yapı sayesinde container, her zaman aynı ana program ile çalışır.

ENTRYPOINT kullanımı ile yapılan çalışmada:
- Container sabit bir program ile çalıştırılmış
- docker run ile verilen argümanlar program parametresi olarak eklenmiştir

ENTRYPOINT davranışını gösteren terminal çıktısı aşağıdaki görselde yer almaktadır:

screenshots/docker-entrypoint.png

---

