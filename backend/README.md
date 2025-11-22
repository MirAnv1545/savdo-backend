# Savdo � Marketplace API

**Savdo**  tadbirkorlar uchun mahsulotlarni boshqarish va buyurtmalarni qabul qilish imkonini beruvchi backend API.  

U Django REST Framework asosida ishlab chiqilgan, JWT orqali autentifikatsiya qiladi, Docker konteynerlarida ishlaydi va AWS EC2 da deploy qilingan.

--- swaggerda Bearer siz faqat Access Token
serverda settings da postgres. localda db

## Texnologiyalar

- Python 3.12
- Django + Django REST Framework
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)
- Docker + Docker Compose
- Nginx reverse proxy
- AWS EC2 deploy
- Certbot (HTTPS)
- Swagger dokumentatsiya (drf-spectacular)

---

##  Loyiha strukturas

savdo/
�
+-- backend/
� +-- config/
� +-- users/
� +-- products/
� L-- orders/
� +-- requirements.txt
� L-- manage.py
�
+-- docker/
� +-- Dockerfile
� L-- nginx.conf
�
L-- docker-compose.yml

---

## ?? Foydalanuvchi rollari

| Role      | Tavsif |
|-----------|--------|
| customer  | Xaridor, mahsulot buyurtma qiladi |
| seller    | Tadbirkor, mahsulot qoshadi va oz buyurtmalarini boshqaradi |
| admin     | Barcha buyurtmalar va foydalanuvchilarni boshqaradi |

---

## ?? API Endpointlar

### Auth (JWT)
| Method | Endpoint | Tavsif |
|--------|---------|--------|
| POST | `/api/users/register/` | Royxatdan otish |
| POST | `/api/users/login/` | JWT token olish |
| POST | `/api/users/refresh/` | Access token yangilash |
| GET/PUT | `/api/users/profile/` | Profilni korish/tahrirlash |

### Products
| Method | Endpoint | Tavsif |
|--------|---------|--------|
| GET | `/api/products/` | Barcha mahsulotlar |
| POST | `/api/products/` | Mahsulot qoshish (seller) |
| GET | `/api/products/<id>/` | Mahsulot detali |
| PUT | `/api/products/<id>/` | Tahrirlash (seller) |
| DELETE | `/api/products/<id>/` | Ochirish (seller) |

### Orders
| Method | Endpoint | Tavsif |
|--------|---------|--------|
| POST | `/api/orders/create/` | Buyurtma yaratish (customer) |
| GET | `/api/orders/` | Oz buyurtmalari (customer/seller/admin) |
| PUT | `/api/orders/<id>/status/` | Status update (seller/admin) |

---

## ?? Docker bilan ishga tushirish

```bash
docker-compose up --build
�	Backend: http://localhost:8000/
�	Swagger: http://localhost:8000/api/docs/
�	Nginx: http://localhost/
________________________________________
AWS Deploy
�	EC2 instance: Amazon Linux 2023
�	Domain: Ahosts orqali boglangan
�	HTTPS: Certbot bilan faollashtirilgan
Swagger: https://ecombgroup.uz/api/docs/
________________________________________
Swagger Dokumentatsiya
�	/api/schema/ � OpenAPI schema
�	/api/docs/ � Swagger UI
Bu orqali barcha endpointlarni test qilishingiz mumkin.
--- swaggerda Bearer siz faqat Access Token
________________________________________
Yakuniy holat
�	Users: Register, Login, Profile
�	Products: CRUD + Seller permission
�	Orders: Buyurtma yaratish, status, seller/admin view
�	Docker: Backend + PostgreSQL + Nginx
�	AWS: EC2 + Domain + HTTPS
