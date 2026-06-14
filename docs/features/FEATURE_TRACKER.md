# ✅ Comunity - Feature Tracker

**Última actualización**: Junio 2025
**Estado General**: MVP Development
**Versión Actual**: 0.1.0

---

## 📊 RESUMEN EJECUTIVO

```
Total Features: 67
Completadas: 0 (0%)
En Progreso: 0 (0%)
Por Hacer: 67 (100%)
Bloqueadas: 0 (0%)

Sprint Actual: Phase 1 - Backend Foundation
Fecha Inicio: Junio 2025
Fecha Fin Estimada: Julio 2025
```

---

## 🗂️ FASES DEL PROYECTO

### FASE 0: SETUP (Semana 1) ✅ COMPLETADA

| ID | Feature | Estado | Prioridad | Responsable | Fecha |
|----|---------|--------|-----------|-------------|-------|
| S-001 | Estructura GitHub | ✅ Done | Alta | Team | 6/12 |
| S-002 | Documentación inicial | ✅ Done | Alta | Team | 6/13 |
| S-003 | Prototipo HTML | ✅ Done | Media | Team | 6/13 |
| S-004 | Brand Guidance | ✅ Done | Media | Design | 6/13 |
| S-005 | UI Screens | ✅ Done | Media | Design | 6/13 |
| S-006 | Database Schema | ✅ Done | Alta | Backend | 6/13 |

---

### FASE 1: BACKEND FOUNDATION (Semana 2-3) 🔵 EN PROGRESO

#### 1.1 Autenticación

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| B-101 | User Registration | POST /api/auth/register | ⬜ Todo | Alta | 8h | Backend |
| B-102 | User Login | POST /api/auth/login | ⬜ Todo | Alta | 6h | Backend |
| B-103 | Email Verification | Enviar email de confirmación | ⬜ Todo | Alta | 4h | Backend |
| B-104 | Phone Verification | Enviar SMS/WhatsApp | ⬜ Todo | Alta | 5h | Backend |
| B-105 | Password Reset | Recuperar contraseña | ⬜ Todo | Media | 6h | Backend |
| B-106 | JWT Token Management | Token generation & validation | ⬜ Todo | Alta | 8h | Backend |
| B-107 | Refresh Token | Extender sesión | ⬜ Todo | Media | 4h | Backend |
| B-108 | Social Login | Google & Facebook auth | ⬜ Todo | Baja | 12h | Backend |

**Criterios de Aceptación (B-101)**:
- [ ] Usuario puede registrarse con email/teléfono
- [ ] Password se hashea correctamente
- [ ] Email de confirmación se envía
- [ ] Validación de email duplicado
- [ ] Validación de campos requeridos
- [ ] Tests unitarios (95% coverage)
- [ ] Error handling completo

---

#### 1.2 User Management

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| B-201 | User Profile | GET/PUT /api/users/:id | ⬜ Todo | Alta | 6h | Backend |
| B-202 | User Avatar Upload | Subir imagen de perfil | ⬜ Todo | Media | 5h | Backend |
| B-203 | User Verification | Badge de usuario verificado | ⬜ Todo | Media | 8h | Backend |
| B-204 | User Preferences | Guardar preferencias | ⬜ Todo | Baja | 4h | Backend |
| B-205 | User Location | GET/PUT ubicación del usuario | ⬜ Todo | Alta | 4h | Backend |
| B-206 | User Online Status | Actualizar estado online | ⬜ Todo | Media | 3h | Backend |
| B-207 | Deactivate Account | Desactivar cuenta | ⬜ Todo | Baja | 3h | Backend |

---

#### 1.3 Broadcasts CRUD

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| B-301 | Create Broadcast | POST /api/broadcasts | ⬜ Todo | Alta | 8h | Backend |
| B-302 | List Broadcasts | GET /api/broadcasts | ⬜ Todo | Alta | 6h | Backend |
| B-303 | Get Broadcast Detail | GET /api/broadcasts/:id | ⬜ Todo | Alta | 4h | Backend |
| B-304 | Update Broadcast | PUT /api/broadcasts/:id | ⬜ Todo | Alta | 5h | Backend |
| B-305 | Delete Broadcast | DELETE /api/broadcasts/:id | ⬜ Todo | Alta | 3h | Backend |
| B-306 | Pause Broadcast | Pausar oferta temporalmente | ⬜ Todo | Media | 3h | Backend |
| B-307 | Broadcast Images | Subir múltiples imágenes | ⬜ Todo | Media | 6h | Backend |
| B-308 | Broadcast Expiration | Auto-expirar después de tiempo | ⬜ Todo | Alta | 5h | Backend |

**Criterios de Aceptación (B-301)**:
- [ ] Usuario puede crear broadcast con todos los campos
- [ ] Validación de campos requeridos
- [ ] Ubicación se guarda con PostGIS
- [ ] Broadcast_until se calcula correctamente
- [ ] Usuario recibe confirmación
- [ ] Auto-expira después del tiempo
- [ ] Tests de integración

---

#### 1.4 Location & Search

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| B-401 | Search Nearby | GET /api/broadcasts/nearby?lat&lng | ⬜ Todo | Alta | 10h | Backend |
| B-402 | Filter by Category | Filtrar por categoría | ⬜ Todo | Alta | 4h | Backend |
| B-403 | Filter by Price Range | Filtrar por rango de precio | ⬜ Todo | Media | 3h | Backend |
| B-404 | Full Text Search | Búsqueda por palabra clave | ⬜ Todo | Media | 8h | Backend |
| B-405 | Distance Calculation | Calcular distancia PostGIS | ⬜ Todo | Alta | 6h | Backend |
| B-406 | Geofencing | Alertas en área específica | ⬜ Todo | Baja | 10h | Backend |

**Criterios de Aceptación (B-401)**:
- [ ] Retorna ofertas dentro de 5km
- [ ] Ordena por distancia
- [ ] Performance < 200ms
- [ ] Incluye información del usuario
- [ ] Paginación funciona
- [ ] Tests de carga

---

#### 1.5 WebSocket Setup

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| B-501 | WebSocket Server | Setup Socket.io | ⬜ Todo | Alta | 6h | Backend |
| B-502 | User Connection | Conectar usuario al socket | ⬜ Todo | Alta | 4h | Backend |
| B-503 | Room Management | Rooms por conversación | ⬜ Todo | Alta | 5h | Backend |
| B-504 | Connection Events | Connect/disconnect events | ⬜ Todo | Media | 3h | Backend |
| B-505 | Ping/Pong | Keep-alive mechanism | ⬜ Todo | Media | 2h | Backend |

---

#### 1.6 Testing & Quality

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| B-601 | Unit Tests | Tests para lógica | ⬜ Todo | Alta | 15h | Backend |
| B-602 | Integration Tests | Tests de APIs | ⬜ Todo | Alta | 12h | Backend |
| B-603 | Linting | ESLint configurado | ⬜ Todo | Media | 2h | Backend |
| B-604 | Error Handling | Manejo de errores | ⬜ Todo | Alta | 8h | Backend |
| B-605 | Logging | Sistema de logs | ⬜ Todo | Media | 4h | Backend |

---

### FASE 2: FRONTEND (Semana 4-5) 🟢 TODO

#### 2.1 Autenticación UI

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| F-101 | Splash Screen | Pantalla de carga inicial | ⬜ Todo | Media | 2h | Frontend |
| F-102 | Login Screen | UI de login | ⬜ Todo | Alta | 6h | Frontend |
| F-103 | Sign Up Screen | UI de registro | ⬜ Todo | Alta | 8h | Frontend |
| F-104 | Email Verification UI | Verificar email visual | ⬜ Todo | Media | 4h | Frontend |
| F-105 | Password Reset UI | Recuperar contraseña visual | ⬜ Todo | Media | 4h | Frontend |
| F-106 | Session Management | Mantener sesión activa | ⬜ Todo | Alta | 4h | Frontend |

---

#### 2.2 Main UI

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| F-201 | Home/Discover | Feed de ofertas | ⬜ Todo | Alta | 10h | Frontend |
| F-202 | Offer Cards | Componente de tarjeta | ⬜ Todo | Alta | 6h | Frontend |
| F-203 | Filter Bar | Filtros en UI | ⬜ Todo | Alta | 5h | Frontend |
| F-204 | Search Bar | Búsqueda en UI | ⬜ Todo | Media | 4h | Frontend |
| F-205 | Pull to Refresh | Actualizar pull-down | ⬜ Todo | Baja | 2h | Frontend |
| F-206 | Infinite Scroll | Cargar más ofertas | ⬜ Todo | Media | 3h | Frontend |

---

#### 2.3 Announce Feature

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| F-301 | Announce Form | Formulario de oferta | ⬜ Todo | Alta | 8h | Frontend |
| F-302 | Form Validation | Validar campos | ⬜ Todo | Alta | 4h | Frontend |
| F-303 | Image Upload | Subir imágenes | ⬜ Todo | Media | 6h | Frontend |
| F-304 | Category Select | Seleccionar categoría | ⬜ Todo | Alta | 3h | Frontend |
| F-305 | Location Picker | Seleccionar ubicación | ⬜ Todo | Media | 5h | Frontend |
| F-306 | Preview Broadcast | Ver preview antes | ⬜ Todo | Baja | 2h | Frontend |

---

#### 2.4 Map View

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| F-401 | Map Component | Mapbox integration | ⬜ Todo | Alta | 8h | Frontend |
| F-402 | User Location | Mostrar mi ubicación | ⬜ Todo | Alta | 4h | Frontend |
| F-403 | Offer Markers | Marcadores de ofertas | ⬜ Todo | Alta | 5h | Frontend |
| F-404 | Map Zoom | Zoom in/out | ⬜ Todo | Media | 2h | Frontend |
| F-405 | Click Marker | Ver oferta al hacer click | ⬜ Todo | Alta | 3h | Frontend |

---

#### 2.5 Profile UI

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| F-501 | Profile Page | Ver mi perfil | ⬜ Todo | Alta | 8h | Frontend |
| F-502 | Edit Profile | Editar perfil | ⬜ Todo | Alta | 6h | Frontend |
| F-503 | Avatar Upload | Cambiar avatar | ⬜ Todo | Media | 4h | Frontend |
| F-504 | My Offers | Ver mis ofertas | ⬜ Todo | Alta | 6h | Frontend |
| F-505 | Transaction History | Ver historial | ⬜ Todo | Media | 6h | Frontend |
| F-506 | Reviews Section | Ver calificaciones | ⬜ Todo | Media | 4h | Frontend |
| F-507 | Settings | Configuración del usuario | ⬜ Todo | Media | 6h | Frontend |

---

### FASE 3: REAL-TIME (Semana 6) ⚡ TODO

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| RT-101 | Chat Component | UI del chat | ⬜ Todo | Alta | 8h | Frontend/Backend |
| RT-102 | Message Sending | Enviar mensajes WebSocket | ⬜ Todo | Alta | 6h | Backend |
| RT-103 | Message Receiving | Recibir mensajes | ⬜ Todo | Alta | 4h | Backend |
| RT-104 | Typing Indicator | "X está escribiendo..." | ⬜ Todo | Media | 3h | Full Stack |
| RT-105 | Online Status | Ver quién está online | ⬜ Todo | Media | 3h | Backend |
| RT-106 | Push Notifications | Notificaciones en tiempo real | ⬜ Todo | Alta | 8h | Backend |
| RT-107 | Notification Center | Centro de notificaciones | ⬜ Todo | Media | 5h | Frontend |

---

### FASE 4: PAGOS (Semana 7) 💳 TODO

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| PAY-101 | Stripe Integration | Conectar Stripe API | ⬜ Todo | Alta | 8h | Backend |
| PAY-102 | Escrow System | Sistema de retención | ⬜ Todo | Alta | 10h | Backend |
| PAY-103 | Payment Form | UI del pago | ⬜ Todo | Alta | 6h | Frontend |
| PAY-104 | Transaction Management | Gestionar transacciones | ⬜ Todo | Alta | 8h | Backend |
| PAY-105 | Receipt Generation | Generar recibos | ⬜ Todo | Media | 4h | Backend |
| PAY-106 | Refund System | Procesar reembolsos | ⬜ Todo | Alta | 6h | Backend |

---

### FASE 5: DEPLOY (Semana 8) 🚀 TODO

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| DEP-101 | Railway Deploy | Deploy backend a Railway | ⬜ Todo | Alta | 4h | DevOps |
| DEP-102 | Vercel Deploy | Deploy frontend a Vercel | ⬜ Todo | Alta | 3h | DevOps |
| DEP-103 | Database Setup | BD en producción | ⬜ Todo | Alta | 6h | DevOps |
| DEP-104 | Environment Vars | Variables de ambiente | ⬜ Todo | Alta | 2h | DevOps |
| DEP-105 | SSL/TLS | Certificados SSL | ⬜ Todo | Alta | 2h | DevOps |
| DEP-106 | Monitoring | Monitoring & alerts | ⬜ Todo | Media | 6h | DevOps |
| DEP-107 | CI/CD Pipeline | GitHub Actions | ⬜ Todo | Alta | 8h | DevOps |
| DEP-108 | Backup System | Backups automáticos | ⬜ Todo | Alta | 4h | DevOps |

---

### FASE 6: MEJORAS V1.0 (Semana 9+) 🔄 TODO

| ID | Feature | Descripción | Estado | Prioridad | Estimación | Responsable |
|----|---------|-------------|--------|-----------|------------|-------------|
| V1-101 | Mobile App | Aplicación React Native | ⬜ Todo | Media | 40h | Mobile |
| V1-102 | AI Recommendations | Recomendaciones personalizadas | ⬜ Todo | Media | 16h | Backend |
| V1-103 | User Verification | Verificación de usuario | ⬜ Todo | Media | 12h | Backend |
| V1-104 | Advanced Analytics | Dashboard de analytics | ⬜ Todo | Baja | 12h | Frontend |
| V1-105 | Multi-language | Soporte multiidioma | ⬜ Todo | Baja | 20h | Full Stack |
| V1-106 | Multi-city | Soporte multi-ciudad | ⬜ Todo | Baja | 16h | Backend |

---

## 📈 TRACKER POR RESPONSABLE

### Backend Team

| Responsable | Total | Done | In Progress | Todo | % Completo |
|------------|-------|------|-------------|------|-----------|
| Carlos (Lead) | 18 | 0 | 0 | 18 | 0% |
| Juan (Junior) | 15 | 0 | 0 | 15 | 0% |
| **TOTAL** | **33** | **0** | **0** | **33** | **0%** |

### Frontend Team

| Responsable | Total | Done | In Progress | Todo | % Completo |
|------------|-------|------|-------------|------|-----------|
| María (Lead) | 20 | 0 | 0 | 20 | 0% |
| Alex (Junior) | 18 | 0 | 0 | 18 | 0% |
| **TOTAL** | **38** | **0** | **0** | **38** | **0%** |

### DevOps Team

| Responsable | Total | Done | In Progress | Todo | % Completo |
|------------|-------|------|-------------|------|-----------|
| Roberto | 8 | 0 | 0 | 8 | 0% |
| **TOTAL** | **8** | **0** | **0** | **8** | **0%** |

---

## 🎯 MILESTONES

### M1: Backend Foundation (Target: Julio 15)
- [ ] Autenticación completa
- [ ] User management
- [ ] Broadcasts CRUD
- [ ] Location search
- [ ] WebSocket básico
- [ ] Tests 95%+ coverage

**Status**: 0/6 ⬜

### M2: Frontend UI (Target: Agosto 15)
- [ ] Auth screens
- [ ] Home/Feed
- [ ] Announce feature
- [ ] Map view
- [ ] Profile section
- [ ] Responsive design

**Status**: 0/6 ⬜

### M3: Real-Time Features (Target: Agosto 29)
- [ ] Chat funcional
- [ ] Notifications
- [ ] Live updates
- [ ] Typing indicators

**Status**: 0/4 ⬜

### M4: Payments (Target: Septiembre 12)
- [ ] Stripe integration
- [ ] Escrow system
- [ ] Payment flow completo
- [ ] Receipts

**Status**: 0/4 ⬜

### M5: Production (Target: Septiembre 26)
- [ ] Deployed a producción
- [ ] All systems monitored
- [ ] Backups funcionando
- [ ] CI/CD pipeline

**Status**: 0/4 ⬜

---

## 🚨 BLOCKERS & RISKS

### Actual Blockers
```
🔴 NONE - Proyecto iniciando
```

### Potential Risks

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|-----------|-------|
| PostGIS complexity | Medium | High | Training temprano | DevOps |
| Payment integration | Medium | High | Empezar fase 4 temprano | Backend |
| Mobile responsiveness | Medium | Medium | Test en dispositivos reales | Frontend |
| Server downtime | Low | High | Backups + redundancy | DevOps |

---

## 📅 CALENDARIO

```
Junio 2025
Su Mo Tu We Th Fr Sa
                1  2
3  4  5  6  7  8  9
10 11 [12][13][14] 15 16  ← Semana 1 (Setup DONE)
17 18 19 20 21 22 23  ← Semana 2 (Backend P1)
24 25 26 27 28 29 30

Julio 2025
              1  2  3  4  5
6  7  8  9  10 11 12  ← Semana 3 (Backend P2)
13 14[15]16 17 18 19  ← Hito M1 Objetivo
20 21 22 23 24 25 26  ← Semana 4 (Frontend P1)
27 28 29 30 31         ← Semana 5 (Frontend P2)

Agosto 2025
                   1  2
3  4  5  6  7  8  9  ← Semana 6 (Real-time)
10 11 12 13 14[15]16  ← Hito M2 Objetivo
17 18 19 20 21 22 23  ← Semana 7 (Pagos)
24 25 26 27 28 29 30  ← Buffer
31

Septiembre 2025
    1  2  3  4  5  6
7  8  9  10 11 12[13] ← Hito M4 Objetivo
14 15 16 17 18 19 20
21 22 23 24 25 26[27] ← Hito M5 - MVP Ready
```

---

## 📊 VELOCITY CHART

```
Sprint 1 (Setup):       6 features ✅
Sprint 2 (Backend P1):  9 features planned
Sprint 3 (Backend P2):  8 features planned
Sprint 4 (Frontend P1): 10 features planned
Sprint 5 (Frontend P2): 8 features planned
Sprint 6 (Real-time):   7 features planned
Sprint 7 (Pagos):       6 features planned
Sprint 8 (Deploy):      8 features planned
```

---

## 🏆 QUALITY METRICS

```
Target Metrics:
- Code Coverage: 95%+
- Performance: < 200ms API
- Uptime: 99.9%
- Bug Resolution: < 24h
- Test Pass Rate: 100%
```

---

## 📝 NOTAS IMPORTANTES

### Convenciones de ID
- `S-XXX`: Setup/Infrastructure
- `B-XXX`: Backend features
- `F-XXX`: Frontend features
- `RT-XXX`: Real-time features
- `PAY-XXX`: Payment features
- `DEP-XXX`: Deployment features
- `V1-XXX`: Version 1.0 features

### Estados
- ⬜ **Todo**: Por hacer
- 🔵 **In Progress**: En progreso
- 🟢 **Review**: En revisión
- ✅ **Done**: Completado
- 🔴 **Blocked**: Bloqueado

### Prioridades
- **Alta**: MVP crítica
- **Media**: Importante pero no crítica
- **Baja**: Nice to have

---

## 🔄 PRÓXIMAS ACCIONES

### Esta Semana
- [ ] Asignar tasks a desarrolladores
- [ ] Setup local environment
- [ ] Kickoff meeting Backend
- [ ] Crear first branches

### Próxima Semana
- [ ] Presentar progreso Phase 1
- [ ] Code review process
- [ ] Begin tests writing
- [ ] Database migrations script

---

**Documento actualizable**: Actualizar semanalmente
**Propietario**: Product Manager
**Última revisión**: 13 Junio 2025
