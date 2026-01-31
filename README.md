# Docker Learning Repository

Bu repository, Docker öğrenme sürecinde yapılan **temel çalışmalar, pratik alıştırmalar ve gerçek dünyaya yakın bir dockerization örneğini** tek bir yapı altında toplamak amacıyla oluşturulmuştur.

Amaç; Docker’ın yalnızca teorik değil, **backend projelerde nasıl kullanıldığını** gösteren, sade ve anlaşılır bir referans repo oluşturmaktır.

---

## Repository Yapısı

Repository üç ana bölümden oluşur:

```
Docker/
├── 1-docker-fundamentals/
├── 2-docker-practices/
└── 3-dockerization/
    └── FastAPI/
```

---

## 1 Docker Fundamentals

Bu bölümde Docker’ın temel kavramları üzerine odaklanılmıştır:

- Docker nedir, neden kullanılır
- Image ve container kavramları
- Dockerfile mantığı
- Container lifecycle
- Temel Docker komutları

Amaç, Docker’ın çalışma mantığını kavrayarak sonraki pratiklere sağlam bir zemin oluşturmaktır.

---

## 2 Docker Practices

Bu bölüm, öğrenilen temel kavramların **küçük pratiklerle pekiştirildiği** alandır.

- Basit container çalıştırma
- Dockerfile yazma denemeleri
- Image build süreçleri
- Küçük test senaryoları

Bu kısım, Docker komutlarına ve yapılandırmasına alışmak için hazırlanmıştır.

---

## 3 Dockerization – FastAPI Project

Bu bölümde FastAPI ile geliştirilen bir backend uygulaması **tam anlamıyla dockerize edilmiştir**.

### Bu projede:

- FastAPI API servisi
- PostgreSQL veritabanı
- SQLAlchemy ORM
- Alembic migration sistemi
- Docker ve Docker Compose
- Environment-based configuration (.env)

birlikte kullanılmıştır.

FastAPI ve PostgreSQL servisleri Docker Compose ile tanımlanmış, aynı network üzerinde haberleştirilmiştir.  
Veritabanı migration’ları Alembic üzerinden yönetilmiştir.

Bu kısım, Docker’ın **gerçek bir backend projesinde** nasıl kullanıldığını göstermeyi amaçlayan ana örnektir.

Detaylı bilgi için:
```
3-dockerization/FastAPI/README.md
```

---

