# 🚀 Comunity

**Plataforma de economía local en tiempo real**

Conecta personas en un radio de 5km para transacciones inmediatas: comida casera, servicios, refacciones, venta de artículos y mucho más.

![Status](https://img.shields.io/badge/status-MVP%20Development-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Node](https://img.shields.io/badge/node-18+-green)
![React](https://img.shields.io/badge/react-18+-blue)

## ✨ Características

- 📍 **Búsqueda en 5km radius** - Encuentra todo lo que necesitas cerca
- ⚡ **Ofertas en tiempo real** - Anunciam y contacta instantáneamente  
- 💬 **Chat directo** - Comunicación inmediata con WebSocket
- 🌙 **Tema oscuro profesional** - Interfaz moderna y legible
- 📱 **Responsive design** - Funciona en mobile, tablet y desktop
- 🔐 **Autenticación segura** - JWT + encriptación
- 🗺️ **Mapa interactivo** - Visualiza ofertas en el área
- 💳 **Sistema de pagos** - Escrow opcional con Stripe
- ⭐ **Sistema de reputación** - Calificaciones y reviews

## 🏗️ Estructura del Proyecto

```
comunity/
├── frontend/          # React + Vite
├── backend/           # Node.js + Express
├── database/          # Schemas SQL
├── docs/              # Documentación
└── scripts/           # Scripts útiles
```

## 🚀 Quick Start

### Requisitos
- Node.js 18+
- PostgreSQL 13+
- Redis 6+
- Docker (opcional)

### Instalación Local

```bash
# 1. Clonar repositorio
git clone https://github.com/tuuser/comunity.git
cd comunity

# 2. Instalar dependencias (opción A - manual)
cd backend && npm install && cd ..
cd frontend && npm install && cd ..

# 3. Configurar variables de entorno
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# 4. Configurar base de datos
createdb comunity_dev
psql comunity_dev < database/schema.sql

# 5. Iniciar desarrollo
npm run dev
```

### Con Docker (opción B - recomendado)

```bash
# Instalar y correr todo
docker-compose up -d

# Ejecutar migraciones
docker exec comunity-backend npm run db:migrate

# Ver logs
docker-compose logs -f
```

## 📚 URLs Locales

- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:5000
- **API Docs**: http://localhost:5000/api/docs
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

## 📖 Documentación

- [API Documentation](docs/API.md) - Endpoints y ejemplos
- [Architecture](docs/ARCHITECTURE.md) - Diseño del sistema
- [Database Schema](docs/DATABASE.md) - Estructura BD
- [Setup Guide](docs/SETUP.md) - Instalación detallada
- [Deployment](docs/DEPLOYMENT.md) - Cómo deployar
- [Contributing](CONTRIBUTING.md) - Guía para contribuir

## 🛠️ Stack Tecnológico

### Frontend
- React 18
- Vite
- TailwindCSS / Custom CSS
- Socket.io (cliente)
- Mapbox GL

### Backend
- Node.js + Express
- PostgreSQL + PostGIS
- Redis
- Socket.io
- JWT Authentication

### DevOps
- Docker + Docker Compose
- Railway (producción)
- Vercel (frontend)
- GitHub Actions (CI/CD)

## 📋 Roadmap

### Fase 0: Setup (Semana 1) ✅
- [x] Estructura GitHub
- [x] Prototipo HTML
- [x] Documentación inicial

### Fase 1: Backend (Semana 2-3) 🔵
- [ ] Autenticación JWT
- [ ] User management
- [ ] Broadcasts CRUD
- [ ] Location queries
- [ ] WebSocket setup

### Fase 2: Frontend (Semana 4-5) 🟢
- [ ] Login/Signup
- [ ] Feed de ofertas
- [ ] Crear broadcast
- [ ] Mapa
- [ ] Perfil

### Fase 3: Tiempo Real (Semana 6) ⚡
- [ ] Chat
- [ ] Notificaciones
- [ ] Feed live

### Fase 4: Pagos (Semana 7) 💳
- [ ] Stripe integration
- [ ] Escrow
- [ ] Transacciones

### Fase 5: Deploy (Semana 8) 🚀
- [ ] Railway
- [ ] Vercel
- [ ] Monitoreo

### Fase 6+: Mejoras (v1.0) 🔄
- [ ] AI Agents
- [ ] Mobile app
- [ ] Verificación
- [ ] Multi-ciudad

Ver [Roadmap completo](docs/ROADMAP.md)

## 🤝 Contribuir

Nos encanta recibir contribuciones! 

1. Fork el repositorio
2. Crea rama: `git checkout -b feature/mi-feature`
3. Commit: `git commit -m "[FEATURE] Descripción"`
4. Push: `git push origin feature/mi-feature`
5. Abre Pull Request

Lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

### Estándares de Código

- ESLint + Prettier
- Commits convencionales
- Tests para features nuevos
- Comentarios en español

## 🧪 Testing

```bash
# Backend
cd backend
npm test
npm run test:watch
npm run coverage

# Frontend
cd frontend
npm test
npm run test:watch
```

## 🚀 Deployment

### Railway (Recomendado)

```bash
railway login
railway init
railway link
railway up --detach
```

### Vercel (Frontend)

```bash
cd frontend
vercel --prod
```

Ver [Deployment Guide](docs/DEPLOYMENT.md) para más opciones.

## 🐛 Reportar Bugs

1. Busca si ya existe el issue
2. Abre nuevo issue con plantilla
3. Proporciona: pasos para reproducir, comportamiento esperado, captura de pantalla

## 📄 Licencia

MIT © 2025 Comunity

## 👥 Autores

- Tu Nombre
- Contribuidores

## 🙏 Agradecimientos

- Comunidad open source
- Usuarios testers
- Collaboradores

---

**¡Únete a nosotros en construir la economía local!** 🌍💪

Síguenos:
- Twitter: [@ComunityApp](https://twitter.com)
- Email: team@comunity.app
- Discord: [Comunidad](https://discord.gg)
