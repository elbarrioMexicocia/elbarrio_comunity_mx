# 🚀 Comunity

**Plataforma de economía local en tiempo real**

Conecta personas en un radio de 5km para transacciones inmediatas: comida casera, servicios, refacciones, venta de artículos y mucho más.

![Status](https://img.shields.io/badge/status-MVP%20Development-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.12-green)
![React](https://img.shields.io/badge/react-18+-blue)

## ✨ Características

- 📍 **Búsqueda en 5km radius** - Encuentra todo lo que necesitas cerca
- ⚡ **Ofertas en tiempo real** - Anunciam y contacta instantáneamente  
- 💬 **Chat directo** - Comunicación inmediata con WebSocket
- 🌙 **Tema oscuro profesional** - Interfaz moderna y legible
- 📱 **Mobile-first / Web nativa** - Optimizado para mobile como web app (responsive + PWA), con posible evolución a app nativa más adelante
- 🔐 **Autenticación segura** - JWT + encriptación
- 🗺️ **Mapa interactivo** - Visualiza ofertas en el área
- 💳 **Sistema de pagos** - Escrow opcional con Stripe
- ⭐ **Sistema de reputación** - Calificaciones y reviews

## 🏗️ Estructura del Proyecto

```
comunity/
├── frontend/          # React + Vite
├── backend/           # Fast API (Python) 
├── database/          # Schemas SQL (Supabase) 
├── docs/              # Documentación 
└── scripts/           # Scripts útiles
```

## 🚀 Quick Start

### Requisitos


### Instalación Local

```bash
# 1. Clonar repositorio
git clone https://github.com/tuuser/comunity.git
cd comunity

# 2. Instalar backend (Python)
cd backend
python3.12 scripts/dev.py install
source .venv/bin/activate
cp .env.example .env
cd ..

# 3. Configurar frontend cuando exista
cp frontend/.env.example frontend/.env

# 4. Levantar PostGIS local y migrar
docker-compose up -d postgres
cd backend
python scripts/dev.py migrate

# 5. Iniciar backend
python scripts/dev.py run
```

### Docker Local

```bash
# Docker se usa para dependencias locales, no para producción del backend
docker-compose up -d postgres

# Ejecutar migraciones desde el backend venv
cd backend
source .venv/bin/activate
python scripts/dev.py migrate

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

## 🛠️ Stack Tecnológico

### DevOps
- Railway (producción)
- Supabase (base de datos hosted)
- Vercel/ClaudeFlare (frontend)
- GitHub Actions (CI/CD)
- Didit (seguridad)

## Licencias
- Railway
- ClaudeFlare
- Notion
- Supabase
- App de Comunicación 
- Stitch / posible Design

## Roles 
- Jose Armando - Product, Front & Design
- Ivan - Backend, DevOps
- Ricardo - Backend, DevOps

## Tipo de Usuario
- Full view (Ops)
- Ofertante
- Clientes

- HTML DE PROPOTOTIPO DE DISEÑO

## 📱 Estrategia Mobile

La prioridad es **web nativa para mobile**: una experiencia responsive/PWA que funcione perfecto en el navegador del celular (sin fricción de instalación, deploy rápido vía Vercel). Una vez validado el producto y con tracción de usuarios, se evaluará migrar a una **app nativa** (iOS/Android, ej. React Native o Capacitor) reusando la mayor parte de la lógica del frontend.

## 📋 Roadmap

### Fase 0: Setup (Semana 1) ✅
- [x] Estructura GitHub
- [x] Prototipo HTML
- [x] Documentación inicial

### Fase 1: Frontend/Backend(Semana 2-6)  🟢
- [ ] Autenticación JWT
- [ ] Fraud / Security 
- [ ] Creacion de Usuarios 
- [ ] Funnel / Onboarding 
- [ ] Set up Canales de Comunicación
- [ ] Home
- [ ] Login/Signup
- [ ] Feed de ofertas
- [ ] Mapa
- [ ] Perfil
- [ ] Primer prototipo /Página HTML
- [ ] Conexión Digital de Negocios/Usuarios

### Fase 2: Tiempo Real (Semana 6) ⚡
- [ ] Chat
- [ ] Notificaciones
- [ ] Feed live
- [ ] Agente AI API (sCRAPING)

### Fase 4: Pagos (Semana 7) 💳
- [ ] Stripe integration
- [ ] Escrow
- [ ] Transacciones

### Fase 5: Deploy (Semana 8) 🚀
- [ ] Monitoreo
- [ ] Testing 

### Fase 6+: Mejoras (v1.0) 🔄
- [ ] AI Agents
- [ ] Mobile app nativa (post web-mobile, ver estrategia mobile abajo)
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

### Estándares de Código

- ESLint + Prettier
- Commits convencionales
- Tests para features nuevos
- Comentarios en español

## 🧪 Testing

```bash
# Backend
cd backend
source .venv/bin/activate
python scripts/dev.py check

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

La base de datos hosted será Supabase. Docker/PostGIS queda para desarrollo local y verificación de migraciones.

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
