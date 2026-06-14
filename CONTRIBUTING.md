# 🤝 Guía para Contribuidores

¡Gracias por tu interés en contribuir a Comunity! Este documento te guiará en el proceso.

## 📋 Antes de Comenzar

- Lee el [README](README.md)
- Revisa [issues abiertos](https://github.com/tuuser/comunity/issues)
- Revisa [pull requests en progreso](https://github.com/tuuser/comunity/pulls)
- Cumple con el [Código de Conducta](#código-de-conducta)

## 🔧 Configuración del Entorno Local

### 1. Fork y Clonar

```bash
# Haz fork en GitHub primero, luego:
git clone https://github.com/TU_USUARIO/comunity.git
cd comunity
git remote add upstream https://github.com/USUARIO_ORIGINAL/comunity.git
```

### 2. Crear Rama

```bash
# Actualizar main
git fetch upstream
git checkout develop
git pull upstream develop

# Crear rama de feature
git checkout -b feature/nombre-descriptivo
```

**Nombra ramas así:**
- `feature/login-screen`
- `fix/broadcast-crash`
- `docs/api-guide`
- `refactor/auth-service`

### 3. Instalar Dependencias

```bash
# Backend
cd backend
npm install
cp .env.example .env
# Editar .env con tu configuración local

# Frontend
cd frontend
npm install
cp .env.example .env
# Editar .env

# Volver al root
cd ../..
```

### 4. Iniciar el Desarrollo

```bash
# Con Docker (recomendado)
docker-compose up -d

# O manual
npm run dev
```

## 📝 Hacer Cambios

### Estándares de Código

#### JavaScript/React

```javascript
// ✅ BIEN
function fetchBroadcasts(location, radius) {
  // Comenta código complejo
  const nearbyOffers = calculateDistance(location, radius);
  return nearbyOffers;
}

// ❌ MAL
function f(l, r) { return d(l, r); }
```

#### Nombrado de Variables

```javascript
// ✅ Descriptivos
const userLocation = getUserLocation();
const broadcastsWithinRadius = filterByDistance(broadcasts, 5);

// ❌ Ambiguos
const loc = getLocation();
const bcasts = filter(b, 5);
```

#### Commits

```bash
# ✅ BIEN - Conventional Commit
git commit -m "[FEATURE] Agregar búsqueda por categoría

- Agrega filtro por tipo de oferta
- Actualiza API endpoint
- Añade tests"

# ❌ MAL
git commit -m "fix stuff"
git commit -m "wip"
```

**Formato de Commit:**

```
[TYPE] Descripción breve

Descripción detallada si es necesario.
Explica el qué y el por qué.

Closes #123
```

**Tipos permitidos:**
- `[FEATURE]` - Nueva funcionalidad
- `[FIX]` - Bug fix
- `[DOCS]` - Documentación
- `[STYLE]` - Formato/estilos
- `[REFACTOR]` - Refactorización de código
- `[TEST]` - Tests
- `[PERF]` - Performance
- `[DEVOPS]` - CI/CD, deploy, etc.

### Testing

```bash
# Escribir tests para nuevo código
npm test

# Ver cobertura
npm run coverage

# Watch mode durante desarrollo
npm run test:watch
```

**Ejemplo de test:**

```javascript
describe('fetchBroadcasts', () => {
  it('debería retornar ofertas dentro del radio', async () => {
    const broadcasts = await fetchBroadcasts(
      { lat: 19.43, lng: -99.13 }, 
      5
    );
    expect(broadcasts.length).toBeGreaterThan(0);
    expect(broadcasts[0].distance).toBeLessThan(5);
  });
});
```

### Linting y Formatting

```bash
# Lint - Encontrar problemas
npm run lint

# Format - Arreglar automáticamente
npm run format

# Husky (pre-commit hooks)
npm run prepare  # Setup husky
```

## 🔄 Crear un Pull Request

### 1. Rebase antes de pushear

```bash
git fetch upstream
git rebase upstream/develop

# Si hay conflictos
git rebase --abort  # Si cambias de opinión
# O resolver conflictos manualmente
git rebase --continue
```

### 2. Push a tu fork

```bash
git push origin feature/nombre-descriptivo
```

### 3. Abrir PR en GitHub

- **Título**: `[FEATURE] Descripción clara`
- **Descripción**:

```markdown
## 📝 Descripción

Qué hace este PR (sé específico).

## 🎯 Tipo de Cambio

- [ ] Nueva funcionalidad
- [x] Bug fix
- [ ] Breaking change
- [ ] Actualización de documentación

## ✅ Checklist

- [x] Mi código sigue los estándares del proyecto
- [x] He hecho selfcheck de mi código
- [x] He agregado comentarios para código complejo
- [x] He actualizado documentación relevante
- [x] No hay warnings en la consola
- [x] He agregado tests
- [x] Tests nuevos pasan

## 🔗 Issues Relacionados

Closes #123
Related to #456

## 📸 Screenshots (si aplica)

[Agrega capturas de pantalla o GIFs]
```

## 📚 Estructura de Carpetas Explicada

```
frontend/
├── src/
│   ├── components/    # Componentes reutilizables
│   ├── pages/         # Componentes de página
│   ├── hooks/         # Custom hooks
│   ├── services/      # Llamadas API
│   ├── styles/        # Estilos globales
│   └── App.jsx

backend/
├── src/
│   ├── controllers/   # Lógica de rutas
│   ├── models/        # Modelos de BD
│   ├── routes/        # Definición de rutas
│   ├── middleware/    # Middleware
│   ├── services/      # Lógica de negocio
│   └── app.js
```

## 🐛 Reportar Bugs

Usa [Bug Report Template](https://github.com/tuuser/comunity/issues/new?template=bug_report.md)

```markdown
## 🐛 Descripción del Bug

[Descripción clara y concisa]

## 📝 Pasos para Reproducir

1. Ir a...
2. Hacer clic en...
3. Observar error...

## 🤔 Comportamiento Esperado

[Lo que debería pasar]

## 😢 Comportamiento Actual

[Lo que realmente ocurre]

## 📸 Screenshots

[Si es aplicable]

## 🖥️ Ambiente

- OS: [Windows/Mac/Linux]
- Browser: [Chrome/Firefox/Safari]
- Node: [versión]
```

## 💡 Sugerir Mejoras

Usa [Feature Request Template](https://github.com/tuuser/comunity/issues/new?template=feature_request.md)

```markdown
## 📋 Descripción de la Mejora

[Descripción clara]

## 🎯 Problema que Resuelve

[Por qué es necesario]

## 💡 Solución Propuesta

[Cómo debería implementarse]

## 🤔 Alternativas Consideradas

[Otras opciones]
```

## 📖 Documentación

### Actualizar Documentación

1. Los cambios en código deben acompañarse de cambios en docs
2. Actualizar [API.md](docs/API.md) si cambias endpoints
3. Actualizar [ARCHITECTURE.md](docs/ARCHITECTURE.md) si cambias arquitectura
4. Agregar comentarios al código complejo

### Escribir Documentación

```markdown
## Título en H2

Párrafo descriptivo.

### Subtítulo en H3

Más detalles con ejemplos de código:

\`\`\`javascript
// Ejemplo de código
\`\`\`

- Punto 1
- Punto 2
```

## 🚀 Proceso de Revisión

1. **Revisión automática**: Tests y linting
2. **Revisión de código**: Mínimo 1 reviewer
3. **Feedback**: Solicitud de cambios
4. **Aprobación**: Se aprueba PR
5. **Merge**: Se fusiona a develop
6. **Deploy**: Automático a staging
7. **Producción**: Manual o automático

### Responder a Reviews

```bash
# Haz cambios locales
git add .
git commit -m "[FEEDBACK] Cambios solicitados"
git push origin feature/nombre-descriptivo

# NO es necesario hacer push force (-f) en PRs normales
```

## 🎯 Áreas de Contribución Buscadas

- ✨ Frontend features (UI/UX)
- 🔌 Backend APIs
- 🧪 Tests
- 📚 Documentación
- 🐛 Bug fixes
- 🌍 Traducción a otros idiomas
- 🎨 Diseño y UX
- ⚙️ DevOps/Infraestructura

## 📞 Necesitas Ayuda?

- Preguntas en [GitHub Discussions](https://github.com/tuuser/comunity/discussions)
- Chat en [Discord](https://discord.gg)
- Email: developers@comunity.app

## 📜 Código de Conducta

### Nuestro Compromiso

Estamos comprometidos con proporcionar un ambiente acogedor y respetuoso.

### Comportamiento Esperado

- Sé respetuoso
- Acepta crítica constructiva
- Enfócate en lo mejor para la comunidad
- Respeta la privacidad

### Comportamiento Inaceptable

- Acoso de cualquier forma
- Discriminación
- Spam
- Violencia o amenazas

### Reportar Infracciones

Email: conduct@comunity.app

---

## ✨ Gracias por Contribuir!

Tu tiempo y esfuerzo hacen que Comunity sea mejor. ¡Apreciamos tu ayuda!

**Pequeña contribución = Gran impacto** 🌟
