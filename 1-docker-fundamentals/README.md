# Docker Temelleri – Faz 2

Bu doküman, Faz 2 kapsamında Docker teknolojisinin temel kavramlarını ve yapısını
teorik olarak anlamak amacıyla hazırlanmıştır.

Bu aşamada amaç, Docker komutlarını ezberlemek değil; Docker’ın hangi bileşenlerden
oluştuğunu, bu bileşenlerin ne işe yaradığını ve sistemin genel çalışma mantığını
kavramaktır.

Docker, bu dokümanda uygulamalardan ve framework’lerden bağımsız olarak ele alınır.

---

## Docker Nedir?

Docker, uygulamaların izole ve tekrar üretilebilir çalışma ortamları içinde
çalıştırılmasını sağlayan bir container platformudur.

Uygulama kodu, bağımlılıklar ve çalıştırma talimatları tek bir yapı altında
paketlenir. Docker, sanal makine kullanmaz; host işletim sisteminin kernel’ini
paylaşarak çalışır.

---

## Temel Kavramlar

### Container

Container, bir uygulamanın çalışma zamanındaki izole örneğidir.

Kendi dosya sistemi, process alanı ve network alanına sahiptir.
Container’lar geçicidir; silinebilir ve yeniden oluşturulabilir.

---

### Image

Image, bir container oluşturmak için kullanılan değiştirilemez (read-only)
dosya sistemi şablonudur.

Uygulama kodunu, bağımlılıkları ve çalıştırma talimatlarını içerir.
Image tek başına çalışmaz, yalnızca container üretmek için kullanılır.

---

### Dockerfile

Dockerfile, bir image’ın nasıl üretileceğini tanımlayan yapı dosyasıdır.

Her talimat, image içinde yeni bir katman (layer) oluşturur.
Dockerfile, image üretim sürecinin kaynağıdır.

---

### Layer

Layer, image’ın değiştirilemez dosya sistemi katmanıdır.

Docker, katmanlı yapı sayesinde cache mekanizmasını kullanır ve
ortak katmanları birden fazla image arasında paylaşabilir.

---

### Docker Engine

Docker Engine, image oluşturma, container çalıştırma ve
container yaşam döngüsünü yöneten arka plan servisidir.

Container’ların gerçek çalışması bu servis tarafından gerçekleştirilir.

---

### Docker Client

Docker Client, Docker Engine ile iletişim kuran komut satırı arayüzüdür.

Kullanıcı tarafından girilen komutlar Docker Engine’e iletilir.

---

### Docker Registry

Docker Registry, image’ların saklandığı ve dağıtıldığı merkezi depodur.

Public registry’ler ve private registry yapıları mevcuttur.

---

### Volume

Volume, container yaşam döngüsünden bağımsız kalıcı veri alanıdır.

Container silinse bile volume üzerindeki veriler korunur.

---

### Network

Docker Network, container’lar arasında izole iletişim sağlayan ağ katmanıdır.

Container’lar aynı network içinde servis adı üzerinden haberleşebilir.

---

## Çalışma Dizini ve Dosya Yapısı

### WORKDIR

WORKDIR, container içinde aktif çalışma dizinini tanımlar.

Sonraki işlemler bu dizin altında gerçekleştirilir.

---

### COPY

COPY, host dosya sisteminden image içine dosya kopyalamak için kullanılır.

---

## Container Çalıştırma Tanımları

### CMD

CMD, container başlatıldığında varsayılan olarak çalıştırılacak komutu tanımlar.

Bir Dockerfile içinde yalnızca bir CMD bulunmalıdır.

---

### ENTRYPOINT

ENTRYPOINT, container’ın ana çalıştırma sürecini belirler.

CMD ile birlikte parametre alacak şekilde yapılandırılabilir.

---

## Image ve Container Süreçleri

### Build

Build, Dockerfile kullanılarak image oluşturma sürecidir.

---

### Run

Run, bir image’dan yeni bir container başlatma işlemidir.

---

## Port ve Ağ Yapısı

### EXPOSE

EXPOSE, container’ın dinlediği portu belgelemek için kullanılır.
Gerçek port açma işlemi yapmaz.

---

### Port Mapping

Port mapping, host portu ile container portu arasında yönlendirme yapılmasını sağlar.

---

## Stateless Container Yaklaşımı

Stateless container, kendi içinde kalıcı veri tutmayan container modelidir.

Kalıcı veriler volume veya harici servislerde tutulur.

---

## Kavramsal Akış

Dockerfile image’ı tanımlar.  
Image container oluşturmak için kullanılır.  
Container, çalıştırılan uygulamadır.

---

## Özet

Docker, uygulamayı çalıştığı ortamdan ayırarak izole ve tekrar üretilebilir
bir çalışma birimi haline getirir.

Bu yapı, microservice mimarileri, container orchestration sistemleri ve
cloud tabanlı uygulamalar için temel altyapıyı oluşturur.

