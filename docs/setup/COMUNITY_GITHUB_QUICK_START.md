# 🚀 Comunity - Quick Start Guide (GitHub Setup)

## Paso a Paso para Iniciar tu Proyecto

### PASO 1: Crear Repositorio en GitHub (5 min)

1. Ve a [github.com/new](https://github.com/new)
2. **Nombre del repo**: `comunity`
3. **Descripción**: "Plataforma de economía local en tiempo real - 5km radius"
4. **Tipo**: Public
5. **Agregar .gitignore**: Node
6. **Licencia**: MIT
7. **Crear repository**

### PASO 2: Clonar y Configurar Local (10 min)

```bash
# Clonar
git clone https://github.com/TU_USUARIO/comunity.git
cd comunity

# Crear rama develop
git checkout -b develop
git push -u origin develop

# Configurar como default
# En GitHub → Settings → Branches → Default branch → develop
```

### PASO 3: Crear Estructura Base (15 min)

```bash
# Crear carpetas principales
mkdir -p frontend backend database docs scripts .github/workflows .github/ISSUE_TEMPLATE

# Crear archivos base
touch README.md CONTRIBUTING.md LICENSE .gitignore .env.example
touch docker-compose.yml package.json

# Copiar archivos de plantillas (ver más abajo)
```

### PASO 4: Agregar Archivos Principales (10 min)

**Copia estos contenidos:**

#### `README.md`
```markdown
# 🚀 Comunity

Plataforma de economía local en tiempo real. 5km radius para transacciones inmediatas.

## Quick Start

```bash
# Docker (recomendado)
docker-compose up -d

# Manual
npm run dev
```

Ver [documentación completa](docs/SETUP.md)

## 🤝 Contribuir

Lee [CONTRIBUTING.md](CONTRIBUTING.md)
```

#### `.gitignore`
[Copiar el contenido del archivo .gitignore-template arriba]

#### `LICENSE`
Usar MIT license (copiar de GitHub)

#### `docker-compose.yml`
[Copiar del GITHUB_SETUP.md]

#### `package.json` (root)
```json
{
  "name": "comunity",
  "version": "0.1.0",
  "description": "Plataforma de economía local en tiempo real",
  "private": true,
  "scripts": {
    "dev": "echo 'Run: cd backend && npm run dev (in one terminal) then cd frontend && npm run dev (in another)'",
    "setup": "bash scripts/setup.sh",
    "test": "echo 'Tests coming soon'"
  }
}
```

### PASO 5: Crear Carpetas Backend (10 min)

```bash
# Backend estructura
cd backend
mkdir -p src/{config,controllers,models,routes,middleware,services,socket,workers,utils}
mkdir -p migrations seeds tests/{unit,integration}

# Backend package.json
cat > package.json << 'EOF'
{
  "name": "comunity-backend",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "node src/server.js",
    "start": "NODE_ENV=production node src/server.js",
    "test": "jest",
    "lint": "eslint src/"
  },
  "dependencies": {
    "express": "^4.18.0",
    "dotenv": "^16.0.0",
    "pg": "^8.8.0",
    "redis": "^4.0.0",
    "socket.io": "^4.5.0",
    "jsonwebtoken": "^9.0.0",
    "bcryptjs": "^2.4.0"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "eslint": "^8.0.0"
  }
}
EOF

# Backend server básico
cat > src/server.js << 'EOF'
import express from 'express';

const app = express();
app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok' });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Backend running on port ${PORT}`);
});
EOF

# Backend .env.example
cat > .env.example << 'EOF'
NODE_ENV=development
PORT=5000
DATABASE_URL=postgresql://user:password@localhost:5432/comunity_dev
REDIS_URL=redis://localhost:6379
JWT_SECRET=tu_secreto_super_secreto
MAPBOX_TOKEN=tu_token
EOF

cd ..
```

### PASO 6: Crear Carpetas Frontend (10 min)

```bash
# Frontend estructura
cd frontend
mkdir -p src/{components,pages,hooks,services,styles}

# Frontend package.json
cat > package.json << 'EOF'
{
  "name": "comunity-frontend",
  "version": "0.1.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "test": "vitest"
  },
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "socket.io-client": "^4.5.0"
  },
  "devDependencies": {
    "vite": "^4.0.0",
    "@vitejs/plugin-react": "^3.0.0"
  }
}
EOF

# Frontend .env.example
cat > .env.example << 'EOF'
VITE_API_URL=http://localhost:5000
VITE_MAPBOX_TOKEN=tu_token
EOF

cd ..
```

### PASO 7: Crear Documentación (10 min)

```bash
# Crear docs
mkdir docs

cat > docs/SETUP.md << 'EOF'
# Setup Local

## Con Docker

```bash
docker-compose up -d
```

## Manual

### Backend
```bash
cd backend
npm install
npm run dev
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
EOF

cat > docs/API.md << 'EOF'
# API Documentation

## Base URL
`http://localhost:5000/api`

## Endpoints

### Health Check
- GET `/health` - Status de la API
EOF
```

### PASO 8: Primer Commit (5 min)

```bash
# Agregar todo
git add .
git commit -m "[SETUP] Estructura inicial del proyecto

- Carpetas base para backend y frontend
- Archivos de configuración
- Documentación inicial
- Docker setup"

# Push a develop
git push origin develop
```

### PASO 9: GitHub Configuración Avanzada (10 min)

#### Crear Branch Protection Rules

1. **Settings → Branches**
2. **Add rule**
3. **Branch name pattern**: `main`
4. Activa:
   - ✅ Require pull request reviews before merging
   - ✅ Require status checks to pass
   - ✅ Require branches to be up to date
   - ✅ Include administrators

Repetir para rama `develop` (menos strict)

#### Crear GitHub Project (Kanban)

1. **Projects → New Project**
2. **Nombre**: "MVP Development"
3. **Template**: Table o Board
4. **Agregar columnas**: Backlog, Todo, In Progress, Review, Done

#### Crear Labels

```bash
# Crear labels en GitHub UI:
- priority:high (rojo)
- priority:medium (amarillo)
- priority:low (gris)
- type:bug (rojo)
- type:feature (azul)
- type:docs (verde)
- area:frontend (azul)
- area:backend (verde)
- status:ready (verde)
- status:blocked (rojo)
```

#### Crear Issue Templates

**Settings → Issues → Set up templates**

Crear `bug_report.md`:
```markdown
---
name: Bug Report
about: Reportar un bug
labels: type:bug
---

## 🐛 Descripción
[Tu descripción aquí]

## 📝 Pasos para Reproducir
1. ...
2. ...

## 🤔 Comportamiento Esperado
[Lo que debería pasar]

## 😢 Comportamiento Actual
[Lo que realmente ocurre]
```

Crear `feature_request.md`:
```markdown
---
name: Feature Request
about: Sugerir una mejora
labels: type:feature
---

## 📋 Descripción
[Tu idea aquí]

## 🎯 Problema que Resuelve
[Por qué es necesario]

## 💡 Solución Propuesta
[Cómo debería implementarse]
```

### PASO 10: Crear Issues Iniciales (10 min)

```markdown
## Backend Setup

# [BACKEND] Autenticación JWT

Necesitamos implementar autenticación segura.

- [ ] Endpoint POST /api/auth/register
- [ ] Endpoint POST /api/auth/login
- [ ] JWT token generation
- [ ] Middleware de validación
- [ ] Tests

**Criterios de aceptación:**
- Usuario puede registrarse
- Usuario puede login
- Token se genera correctamente
- Middleware valida tokens

**Estimación**: 5-8 horas
**Prioridad**: Alta

---

## Frontend Setup

# [FRONTEND] Login Screen

Diseñar e implementar pantalla de login.

- [ ] Componente LoginForm
- [ ] Validación de formulario
- [ ] Integración con API
- [ ] Error handling
- [ ] Responsive design

**Criterios de aceptación:**
- Pantalla se ve bien en mobile
- Validación funciona
- Errores se muestran claramente

**Estimación**: 4-6 horas
**Prioridad**: Alta
```

### PASO 11: Crear Milestones

**Issues → Milestones → New Milestone**

```
🔵 MVP Phase 1: Backend Foundation
Fecha: 2 semanas
Issues: 5-7 (auth, broadcasts, users)

🟢 MVP Phase 2: Frontend UI
Fecha: 2 semanas
Issues: 4-5 (login, feed, broadcast)

⚡ MVP Phase 3: Real-time
Fecha: 1 semana
Issues: 3 (websocket, chat, notifications)

💳 MVP Phase 4: Payments
Fecha: 1 semana
Issues: 2 (stripe, escrow)

🚀 MVP Phase 5: Deploy
Fecha: 1 semana
Issues: 2 (railway, vercel)
```

### PASO 12: Invitar Colaboradores (5 min)

**Settings → Collaborators → Invite a collaborator**

O crear equipo: **Settings → Teams**

---

## ✅ Checklist de Configuración

```
GitHub Repo:
- [x] Crear repositorio público
- [x] Agregar descripción
- [x] Agregar topics: comunidad, economia-local, marketplace
- [x] Agregar README
- [x] Agregar LICENSE (MIT)
- [x] Agregar .gitignore

Estructura:
- [x] Backend carpetas
- [x] Frontend carpetas
- [x] Database carpetas
- [x] Docs carpetas
- [x] Docker compose

Configuración GitHub:
- [x] Branch protection rules
- [x] Default branch: develop
- [x] Issue templates
- [x] GitHub Project
- [x] Labels
- [x] Milestones

Documentación:
- [x] README.md
- [x] CONTRIBUTING.md
- [x] docs/SETUP.md
- [x] docs/API.md

Primer Commit:
- [x] Commit inicial
- [x] Push a develop
```

---

## 🎯 Próximos Pasos

1. **Crear issues** para cada feature del roadmap
2. **Asignar issues** a colaboradores
3. **Crear pull request template**
4. **Setup CI/CD** (GitHub Actions)
5. **Crear primera rama de feature**

---

## 📚 Referencias

- [GitHub Docs](https://docs.github.com)
- [GitHub Workflow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**¡Felicidades! Tu proyecto Comunity está configurado profesionalmente en GitHub!** 🎉

Ahora puedes:
1. Crear issues
2. Invitar colaboradores
3. Empezar a desarrollar
4. Trackear progreso
5. Colaborar efectivamente
