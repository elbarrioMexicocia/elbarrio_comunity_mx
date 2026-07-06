# 📁 Comunity - Project Structure

## Árbol de Carpetas

```
comunity/
├── 📄 README.md                      # Descripción principal
├── 📄 CONTRIBUTING.md                # Guía para contribuidores
├── 📄 LICENSE                        # Licencia MIT
├── 📄 package.json                   # Root dependencies
├── 📄 docker-compose.yml             # Docker setup
├── 📄 .env.example                   # Variables de ejemplo
├── 📄 .gitignore                     # Ignorar archivos
│
├── 📚 docs/                          # DOCUMENTACIÓN COMPLETA
│   ├── INDEX.md                      # Índice de documentación
│   ├── 🎨 brand/
│   │   └── BRAND_GUIDANCE.md         # Guía de marca
│   ├── 📱 design/
│   │   ├── UI_SCREENS.md             # 24 pantallas detalladas
│   │   ├── comunity-dark-prototype.html
│   │   └── comunity-prototype.html
│   ├── 🗄️ database/
│   │   └── DATABASE_SCHEMA.md        # Schema + queries
│   ├── ✅ features/
│   │   └── FEATURE_TRACKER.md        # Tracker de 67 features
│   ├── 🏗️ setup/
│   │   ├── COMUNITY_GITHUB_SETUP.md
│   │   └── COMUNITY_GITHUB_QUICK_START.md
│   └── 📖 guides/
│       ├── COMUNITY_SAME_DAY_ECONOMY_GUIDE.md
│       ├── COMUNITY_QUICK_START.md
│       └── COMUNITY_FINAL_SUMMARY.md
│
├── 💻 frontend/                      # REACT APPLICATION
│   ├── package.json
│   ├── public/
│   ├── src/
│   │   ├── components/               # Componentes reutilizables
│   │   ├── pages/                    # Páginas principales
│   │   ├── hooks/                    # Custom hooks
│   │   ├── services/                 # API calls
│   │   ├── styles/                   # Estilos globales
│   │   ├── App.jsx
│   │   └── index.js
│   └── .env.example
│
├── 🔌 backend/                       # FastAPI API (Python)
│   ├── app/
│   │   ├── api/                      # Rutas HTTP
│   │   ├── core/                     # Configuración
│   │   ├── db/                       # Conexión a BD
│   │   └── main.py                   # Entry point FastAPI
│   ├── alembic/                      # Migraciones
│   ├── scripts/                      # Comandos de desarrollo Python
│   ├── tests/
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   ├── pyproject.toml
│   └── .env.example
│
├── 🗄️ database/                      # DATABASE SCHEMAS
│   ├── migrations/                   # SQL migration files
│   │   ├── 001_create_users.sql
│   │   ├── 002_create_broadcasts.sql
│   │   ├── 003_create_conversations.sql
│   │   └── 004_create_transactions.sql
│   └── seeds/                        # Test data
│
├── 🔧 scripts/                       # UTILITY SCRIPTS
│   ├── setup.sh                      # Setup inicial
│   ├── db-migrate.sh                 # Correr migraciones
│   ├── seed-db.sh                    # Seed test data
│   └── deploy.sh                     # Deploy a producción
│
└── .github/                          # GITHUB CONFIG
    ├── workflows/                    # CI/CD workflows
    │   ├── test.yml
    │   ├── deploy.yml
    │   └── lint.yml
    └── ISSUE_TEMPLATE/               # Issue templates
        ├── bug_report.md
        └── feature_request.md
```

---

## 📂 Qué va en cada carpeta

### 📚 `/docs` - TODA LA DOCUMENTACIÓN
- **brand/** - Guía de marca (colores, tipografía)
- **design/** - Pantallas detalladas + prototipos
- **database/** - Schema, queries, migraciones
- **features/** - Feature tracker + roadmap
- **setup/** - GitHub setup + quick start
- **guides/** - Guías técnicas completas

### 💻 `/frontend` - REACT APP
- `src/components/` - Botones, Cards, etc (reutilizables)
- `src/pages/` - Login, Home, Profile, etc (pantallas completas)
- `src/hooks/` - useLocation, useOffers, useSocket, etc
- `src/services/` - API calls, geolocation
- `src/styles/` - CSS global, variables, responsive

### 🔌 `/backend` - FASTAPI API
- `app/api/` - Rutas HTTP
- `app/core/` - Settings y configuración
- `app/db/` - Conexión SQLAlchemy
- `alembic/` - Migraciones de base de datos
- `scripts/dev.py` - Comandos de desarrollo Python
- `.agents/skills/` - Skills para agentes que contribuyen al backend

### 🗄️ `/database` - SQL SCRIPTS
- `migrations/` - Crear/actualizar tablas
- `seeds/` - Datos de prueba

### 🔧 `/scripts` - HERRAMIENTAS
- `setup.sh` - Instalar y configurar
- `db-migrate.sh` - Correr migraciones
- `deploy.sh` - Desplegar a producción

### .github/ - INTEGRACIÓN CON GITHUB
- `workflows/` - Automated testing, linting, deployment
- `ISSUE_TEMPLATE/` - Plantillas para bugs y features

---

## 🚀 CÓMO COMENZAR

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/comunity.git
cd comunity
```

### 2. Crear rama develop
```bash
git checkout -b develop
git push -u origin develop
```

### 3. Instalar dependencias
```bash
# Backend
cd backend
python3.12 scripts/dev.py install
source .venv/bin/activate
cp .env.example .env

# Frontend
cd ../frontend
npm install
cp .env.example .env
```

### 4. Setup database local con Docker
```bash
docker-compose up -d postgres
```

### 5. Correr migraciones
```bash
cd backend
source .venv/bin/activate
python scripts/dev.py migrate
```

### 6. Iniciar desarrollo
```bash
# Terminal 1 - Backend
cd backend && source .venv/bin/activate && python scripts/dev.py run

# Terminal 2 - Frontend  
cd frontend && npm run dev
```

---

## 📖 LEER DOCUMENTACIÓN

**Para empezar:**
1. Lee `docs/INDEX.md` (índice completo)
2. Lee `docs/setup/COMUNITY_GITHUB_QUICK_START.md` (12 pasos)
3. Elige tu área y lee los docs relevantes

**Por área:**
- **Backend** → `docs/database/DATABASE_SCHEMA.md` + `docs/features/FEATURE_TRACKER.md`
- **Frontend** → `docs/design/UI_SCREENS.md` + `docs/brand/BRAND_GUIDANCE.md`
- **Design** → `docs/brand/BRAND_GUIDANCE.md` + prototipos HTML

---

## 🔄 WORKFLOW DE DESARROLLO

### Para cada feature:

1. **Crea rama**: `git checkout -b feature/nombre`
2. **Lee docs**: Revisa requirements en `FEATURE_TRACKER.md`
3. **Desarrolla**: Frontend o Backend según corresponda
4. **Testa**: Escribe tests + corre tests locales
5. **Commits**: Sigue convenciones en `CONTRIBUTING.md`
6. **PR**: Crea pull request, pide review
7. **Merge**: Merge a `develop` después de aprobación

---

## 📊 ESTRUCTURA DE DOCUMENTACIÓN

```
docs/
├── INDEX.md                    # Índice y guía de lectura
├── brand/
│   └── BRAND_GUIDANCE.md      # Colores, tipografía, componentes
├── design/
│   ├── UI_SCREENS.md          # 24 pantallas detalladas
│   ├── comunity-dark-prototype.html
│   └── comunity-prototype.html
├── database/
│   └── DATABASE_SCHEMA.md      # 10 tablas, queries, índices
├── features/
│   └── FEATURE_TRACKER.md      # 67 features, roadmap, milestones
├── setup/
│   ├── COMUNITY_GITHUB_SETUP.md
│   └── COMUNITY_GITHUB_QUICK_START.md
└── guides/
    ├── COMUNITY_SAME_DAY_ECONOMY_GUIDE.md
    ├── COMUNITY_QUICK_START.md
    └── COMUNITY_FINAL_SUMMARY.md
```

---

## ⚙️ CONFIGURACIÓN IMPORTANTE

### Backend
- Copiar `.env.example` → `.env`
- Rellenar variables de ambiente
- `python3.12 scripts/dev.py install`
- `source .venv/bin/activate`
- `python scripts/dev.py migrate`

### Frontend
- Copiar `.env.example` → `.env`
- Rellenar `REACT_APP_API_URL`
- `npm install`
- `npm run dev`

### Docker
- Instalar Docker & Docker Compose
- Usarlo para dependencias locales, especialmente PostGIS
- Correr `docker-compose up -d postgres`
- Acceder a PostgreSQL/PostGIS en localhost:5432
- La base de datos hosted será Supabase

---

## 🎯 PRÓXIMOS PASOS

1. **Setup local**: Sigue pasos en docs/setup/
2. **Crear features**: Abre issues para Phase 1 (Backend)
3. **Asignar tareas**: Usa FEATURE_TRACKER.md
4. **Trackea progreso**: Actualiza tracker semanal
5. **Deploy**: Cuando Phase 5 esté lista

---

## 📞 AYUDA

- **Setup problem?** → Lee `docs/setup/COMUNITY_GITHUB_QUICK_START.md`
- **Feature details?** → Revisa `docs/features/FEATURE_TRACKER.md`
- **Database question?** → Consulta `docs/database/DATABASE_SCHEMA.md`
- **UI requirement?** → Mira `docs/design/UI_SCREENS.md`
- **Code standards?** → Lee `CONTRIBUTING.md`

---

**Versión**: 1.0  
**Última actualización**: Junio 2025  
**Estado**: 🟢 Ready to develop
