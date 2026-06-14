# 📱 Comunity - UI Screens & Wireframes

## Índice de Pantallas

```
Autenticación:
  1. Splash Screen
  2. Login
  3. Sign Up (Registro)
  4. Verify Phone/Email

Principal (Logged In):
  5. Home/Discover (Feed)
  6. Announce (Crear Oferta)
  7. Map View
  8. Search Results

Social:
  9. Chat/Conversations
  10. Chat Detail (Conversación Abierta)
  11. Notifications

Transaccional:
  12. Oferta Detail
  13. Confirm Transaction
  14. Payment/Escrow
  15. Transaction Complete

Perfil:
  16. My Profile
  17. Edit Profile
  18. My Offers
  19. Transaction History
  20. Reviews/Ratings

Settings:
  21. Settings
  22. Preferences
  23. Help & Support
  24. About
```

---

## 1️⃣ SPLASH SCREEN

```
┌─────────────────────┐
│                     │
│      🚀 Comunity    │
│                     │
│  Economía Local en  │
│  Tiempo Real        │
│                     │
│    [Cargando...]    │
│                     │
└─────────────────────┘

Color: Negro (#0F0F0F)
Tiempo: 2 segundos
Transición: Fade a Login
```

---

## 2️⃣ LOGIN SCREEN

```
┌─────────────────────────────┐
│  ← Back                     │
├─────────────────────────────┤
│                             │
│    🚀 Comunity              │
│                             │
│    Inicia Sesión            │
│                             │
│  ┌─────────────────────┐    │
│  │ Email o Teléfono    │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Contraseña          │    │
│  └─────────────────────┘    │
│                             │
│  [ Olvidé mi contraseña ]   │
│                             │
│  ┌─────────────────────┐    │
│  │ Inicia Sesión       │    │
│  │ [Gradiente Cian]    │    │
│  └─────────────────────┘    │
│                             │
│  ¿No tienes cuenta?         │
│  [ Crear nueva cuenta ]      │
│                             │
└─────────────────────────────┘

Elementos:
- Input fields con validación
- Error messages
- "Remember me" checkbox
- Social login (Google, Facebook)
```

---

## 3️⃣ SIGN UP SCREEN

```
┌─────────────────────────────┐
│  ← Back                     │
├─────────────────────────────┤
│                             │
│    Crear Cuenta             │
│                             │
│  ┌─────────────────────┐    │
│  │ Nombre Completo     │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Email               │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Teléfono            │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Contraseña          │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Confirmar Contraseña│    │
│  └─────────────────────┘    │
│                             │
│  ☐ Acepto términos          │
│                             │
│  ┌─────────────────────┐    │
│  │ Crear Cuenta        │    │
│  │ [Gradiente]         │    │
│  └─────────────────────┘    │
│                             │
│  ¿Ya tienes cuenta?         │
│  [ Inicia Sesión ]          │
│                             │
└─────────────────────────────┘

Pasos:
- Seleccionar tipo de usuario (comprador/vendedor)
- Verificar email/teléfono
- Crear perfil básico
```

---

## 4️⃣ VERIFY PHONE/EMAIL

```
┌─────────────────────────────┐
│                             │
│    Verificar Identidad      │
│                             │
│  ┌─────────────────────┐    │
│  │  Enviamos código a: │    │
│  │  +56 9 1234 5678    │    │
│  └─────────────────────┘    │
│                             │
│  Ingresa código (6 dígitos) │
│                             │
│  ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐  │
│  │ │ │ │ │ │ │ │ │ │ │ │  │
│  └─┘ └─┘ └─┘ └─┘ └─┘ └─┘  │
│                             │
│  Resend in 59s              │
│                             │
│  ┌─────────────────────┐    │
│  │ Verificar           │    │
│  └─────────────────────┘    │
│                             │
│  ¿Número equivocado?        │
│  [ Cambiar número ]          │
│                             │
└─────────────────────────────┘

Funcionalidad:
- Auto-focus en inputs
- Paste support
- Countdown timer
- Resend button
```

---

## 5️⃣ HOME / DISCOVER (FEED)

```
┌─────────────────────────────┐
│ 🚀 Comunity                │
│ Economía Local en Tiempo Real
├─────────────────────────────┤
│ 🟢 En vivo: 12 personas    │
├─────────────────────────────┤
│                             │
│  [Stats: 28 Personas]       │
│  [42 Ofertas Activas]       │
│  [24 Activos Ahora]         │
│  [5km Tu Radio]             │
│                             │
│  [Todos] [Comida] [Servicios]
│  [Refacciones] [Clases]     │
│                             │
│  ┌──────────────────────┐   │
│  │ 🍜 Doña Carmen       │   │
│  │ 0.8km               │   │
│  │ Tamales Caseros     │   │
│  │ Docena de oaxaq...  │   │
│  │ ─────────────────   │   │
│  │ $50/docena  ⭐4.8   │   │
│  │ Disponible 4h 🟢    │   │
│  │ [💬 Contactar]      │   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │ 🔧 Don Roberto      │   │
│  │ 1.2km               │   │
│  │ Reparación de Autos │   │
│  │ Mecánica general... │   │
│  │ ─────────────────   │   │
│  │ $40/h   ⭐4.9       │   │
│  │ Disponible 8h 🟢    │   │
│  │ [💬 Contactar]      │   │
│  └──────────────────────┘   │
│                             │
│  [Más ofertas...]           │
│                             │
├─────────────────────────────┤
│ 🏠  📢  🗺️  👤             │
│ Inicio Anunciar Mapa Perfil │
└─────────────────────────────┘

Características:
- Pull to refresh
- Infinite scroll
- Filter/search
- Save favorites
- Share offers
```

---

## 6️⃣ ANNOUNCE / CREATE OFFER

```
┌─────────────────────────────┐
│ ← Back                      │
├─────────────────────────────┤
│                             │
│  📢 Anuncia Tu Oferta       │
│                             │
│  ┌─────────────────────┐    │
│  │ ¿Qué ofreces?       │    │
│  │ Ej: Diseño web...   │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Precio / Tarifa     │    │
│  │ $40/hora...         │    │
│  └─────────────────────┘    │
│                             │
│  ┌──────────┬──────────┐    │
│  │Precio    │Disponible│    │
│  │$40/hora  │3 horas   │    │
│  └──────────┴──────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Descripción         │    │
│  │ (Cuéntale más...)   │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Tipo de Oferta:     │    │
│  │ ▼ Servicio          │    │
│  │   - Comida Casera   │    │
│  │   - Servicio        │    │
│  │   - Vender          │    │
│  │   - Trabajo         │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ 📡 Anunciar 5km     │    │
│  │ [Gradiente]         │    │
│  └─────────────────────┘    │
│                             │
└─────────────────────────────┘

Validación:
- Campos obligatorios
- Prevista del anuncio
- Auto-localización
- Timer de expiración
```

---

## 7️⃣ MAP VIEW

```
┌─────────────────────────────┐
│ ← Back                      │
├─────────────────────────────┤
│                             │
│      [  MAP WITH DOTS  ]    │
│      ┌─────────────────┐    │
│      │   ┌────────┐    │    │
│      │   │   MY   │    │    │
│      │   │LOCATION│    │    │
│      │   │ (5km)  │    │    │
│      │   └────────┘    │    │
│      │  • 🟢 🟡 🔴     │    │
│      │  • 🟦 🟨 🟩     │    │
│      │  • 🟪 🟥 🟦     │    │
│      └─────────────────┘    │
│                             │
│  Leyenda:                   │
│  🍜 Comida   🔧 Servicios   │
│  📦 Vender   💼 Trabajo     │
│  📚 Clases   🙏 Buscar      │
│                             │
├─────────────────────────────┤
│  [Stats Cards]              │
│  Total: 42  Distancia: 2.1km
│  Rating: 4.8 Comunidad: 1.2k
│                             │
└─────────────────────────────┘

Funcionalidad:
- Click en punto = ver oferta
- Zoom in/out
- Filter por categoría
- My location
- Routing
```

---

## 8️⃣ SEARCH RESULTS

```
┌─────────────────────────────┐
│ ← Back   [Buscar...]    🔍  │
├─────────────────────────────┤
│                             │
│  Resultados para            │
│  "diseño"                   │
│                             │
│  8 resultados encontrados   │
│                             │
│  Filtros:                   │
│  [Todos] [Cercano] [Rating] │
│  [Precio] [Disponible]      │
│                             │
│  ┌──────────────────────┐   │
│  │ 🎨 Sofia Pérez      │   │
│  │ 2.1km               │   │
│  │ Diseño Gráfico      │   │
│  │ Branding digital... │   │
│  │ ─────────────────   │   │
│  │ $40/h   ⭐4.9       │   │
│  │ Disponible 6h 🟢    │   │
│  │ [💬 Contactar]      │   │
│  └──────────────────────┘   │
│                             │
│  [Más resultados...]        │
│                             │
└─────────────────────────────┘

Características:
- Busca por texto
- Filtros avanzados
- Ordenamiento
- Guardados
```

---

## 9️⃣ CHAT / CONVERSATIONS

```
┌─────────────────────────────┐
│ Mensajes                    │
├─────────────────────────────┤
│                             │
│  🟢 Reciente                │
│  ┌──────────────────────┐   │
│  │👤 Carlos Martinez    │   │
│  │   Reparaciones de... │   │
│  │   Hace 2 horas       │   │
│  │   "Dale, te espero.."│   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │👤 Ana López         │   │
│  │   Limpieza de Casas  │   │
│  │   Hace 1 día         │   │
│  │   "Perfecto, gracias"│   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │👤 Juan Rodríguez    │   │
│  │   Reparación de...   │   │
│  │   Hace 3 días        │   │
│  │   "Me das tu dirección?"
│  └──────────────────────┘   │
│                             │
│  ⚫ Archivados               │
│  ┌──────────────────────┐   │
│  │👤 Sofia Pérez       │   │
│  │   Hace 2 semanas     │   │
│  └──────────────────────┘   │
│                             │
│  [Ver más conversaciones]   │
│                             │
└─────────────────────────────┘

Acciones:
- Buscar conversación
- Archivar/Desarchivar
- Eliminar
- Notificaciones
```

---

## 🔟 CHAT DETAIL

```
┌─────────────────────────────┐
│ ← Back   Carlos Martinez   👤│
│ 🟢 Activo ahora             │
├─────────────────────────────┤
│                             │
│  Reparación de Plomería     │
│  $30/hora                   │
│  ────────────────────────   │
│                             │
│  [Oferta guardada]          │
│                             │
│  ────────────────────────   │
│                             │
│  Tú:                        │
│  "Hola, tengo una fuga..."  │
│                             │
│  Carlos:                    │
│  "Cuál es la dirección?"    │
│                             │
│  Tú:                        │
│  "Reforma 450, depto 12"    │
│                             │
│  Carlos:                    │
│  "Dale, en 30 min estoy!"   │
│  ⭐ 4.8  ✔ Leído             │
│                             │
│  ────────────────────────   │
│  ┌─────────────────────┐    │
│  │ Escribe mensaje...  │  📎│
│  └─────────────────────┘    │
│                             │
│  [📍 Compartir ubicación]   │
│  [💳 Iniciar pago]          │
│  [⭐ Calificar]             │
│                             │
└─────────────────────────────┘

Características:
- Typing indicator
- Seen receipts
- Emoji picker
- Share location
- Initiate payment
- Block user
```

---

## 1️⃣1️⃣ NOTIFICATIONS

```
┌─────────────────────────────┐
│ Notificaciones              │
├─────────────────────────────┤
│                             │
│  🟢 Hoy                     │
│  ┌──────────────────────┐   │
│  │ 💬 Carlos respondió  │   │
│  │    Tu oferta: ...    │   │
│  │    "Dale, en 30 min" │   │
│  │    Hace 5 min        │   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │ 🔥 Oferta Popular   │   │
│  │    Tamales Caseros   │   │
│  │    11 personas interes│   │
│  │    Hace 30 min       │   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │ ⭐ Nuevo Rating      │   │
│  │    Carlos (5.0 ⭐)    │   │
│  │    "Rápido y seguro" │   │
│  │    Hace 2 horas      │   │
│  └──────────────────────┘   │
│                             │
│  ⚫ Esta semana              │
│  ┌──────────────────────┐   │
│  │ 💰 Pago Completado  │   │
│  │    Reparación auto   │   │
│  │    Carlos Martinez   │   │
│  └──────────────────────┘   │
│                             │
│  [Marcar todo como leído]   │
│                             │
└─────────────────────────────┘

Tipos:
- New message
- Offer matching
- New review
- Payment confirmation
- Milestone (10 transactions)
```

---

## 1️⃣2️⃣ OFERTA DETAIL

```
┌─────────────────────────────┐
│ ← Back       ⭐ Guardar    │
├─────────────────────────────┤
│                             │
│  [HERO IMAGE o COLOR]       │
│                             │
│  🍜 Tamales Caseros         │
│  Doña Carmen  0.8km         │
│  ⭐ 5.0 (28 reviews)        │
│  Activa 🟢                  │
│                             │
│  Descripción:               │
│  "Oaxaqueños, rajas con     │
│   queso, verdes. Hechizo   │
│   de la abuela. Docena."    │
│                             │
│  ┌────────────────────┐     │
│  │ $50 / docena       │     │
│  │ Disponible 3h      │     │
│  │ Distancia: 0.8km   │     │
│  └────────────────────┘     │
│                             │
│  Vendedor:                  │
│  👤 Doña Carmen             │
│  ⭐ 5.0 (125 transacciones) │
│  "Comida casera de calidad" │
│                             │
│  Reviews:                   │
│  ┌────────────────────┐     │
│  │ ⭐⭐⭐⭐⭐ "Riquísimos!" │
│  │ Juan M. - 2 días ago     │
│  └────────────────────┘     │
│  ┌────────────────────┐     │
│  │ ⭐⭐⭐⭐⭐ "La verdad..." │
│  │ María L. - 1 semana      │
│  └────────────────────┘     │
│                             │
│  ┌────────────────────┐     │
│  │ 💬 Contactar       │     │
│  │ [Gradiente]        │     │
│  └────────────────────┘     │
│                             │
│  [📍 Ver en mapa] [📞Llamar]
│                             │
│  [🚫 Reportar] [✉️ Compartir]
│                             │
└─────────────────────────────┘

Secciones:
- Imágenes gallery
- Descripción
- Precio
- Disponibilidad
- Información vendedor
- Reviews
- CTA contacto
```

---

## 1️⃣3️⃣ CONFIRM TRANSACTION

```
┌─────────────────────────────┐
│ Confirmar Transacción       │
├─────────────────────────────┤
│                             │
│  Revisemos los detalles:    │
│                             │
│  ┌────────────────────┐     │
│  │ 🍜 Tamales Caseros │     │
│  │ Doña Carmen         │     │
│  │ Precio: $50         │     │
│  │ Cantidad: 1 docena  │     │
│  │ ────────────────────│     │
│  │ Subtotal: $50       │     │
│  │ Comisión: $5        │     │
│  │ ────────────────────│     │
│  │ TOTAL: $55          │     │
│  └────────────────────┘     │
│                             │
│  Ubicación de entrega:      │
│  📍 Reforma 450, Depto 12   │
│  ────────────────────────   │
│                             │
│  Fecha y hora:              │
│  Hoy a las 3:30 PM          │
│  ────────────────────────   │
│                             │
│  Método de pago:            │
│  ☐ Efectivo                 │
│  ☑ Escrow (Seguro)          │
│  "El dinero se retiene      │
│   hasta confirmar entrega"  │
│                             │
│  ☐ Acepto términos y        │
│     condiciones             │
│                             │
│  ┌────────────────────┐     │
│  │ Confirmar          │     │
│  │ [Gradiente]        │     │
│  └────────────────────┘     │
│                             │
│  ← Atrás                    │
│                             │
└─────────────────────────────┘

Seguridad:
- Confirmar detalles
- Elegir método de pago
- Aceptar términos
- Protección de comprador
```

---

## 1️⃣4️⃣ PAYMENT / ESCROW

```
┌─────────────────────────────┐
│ Finalizar Pago              │
├─────────────────────────────┤
│                             │
│  Detalles de Pago:          │
│  ────────────────────────   │
│                             │
│  ☐ Tarjeta de Crédito       │
│  ☑ Google Pay               │
│  ☐ Apple Pay                │
│  ☐ Transferencia Bancaria   │
│                             │
│  Google Pay:                │
│                             │
│  Tu perfil: Juan Pérez      │
│  Tarjeta: ••••••••••4242    │
│                             │
│  [Cambiar método]           │
│                             │
│  ┌────────────────────┐     │
│  │ $55.00 USD         │     │
│  │                    │     │
│  │ Seguro con Escrow: │     │
│  │ 🔒 Tu dinero está  │     │
│  │    protegido hasta │     │
│  │    confirmar       │     │
│  │    entrega         │     │
│  └────────────────────┘     │
│                             │
│  ☐ Guardar para futuros      │
│     pagos                   │
│                             │
│  ┌────────────────────┐     │
│  │ Confirmar Pago     │     │
│  │ [Gradiente]        │     │
│  └────────────────────┘     │
│                             │
│  ← Atrás                    │
│                             │
│  [🔒 Conexión segura]       │
│                             │
└─────────────────────────────┘

Características:
- Múltiples métodos de pago
- Escrow automático
- Protección de datos
- Confirmación SSL
```

---

## 1️⃣5️⃣ TRANSACTION COMPLETE

```
┌─────────────────────────────┐
│                             │
│        ✅ ¡Completado!      │
│                             │
│  Tu transacción ha sido     │
│  confirmada.                │
│                             │
│  ┌────────────────────┐     │
│  │ 🍜 Tamales Caseros │     │
│  │ Doña Carmen        │     │
│  │ Precio: $55        │     │
│  │ ID: #TXN-12345     │     │
│  └────────────────────┘     │
│                             │
│  📍 Entrega en:             │
│  Reforma 450, Depto 12      │
│  Hoy, 3:30 PM              │
│                             │
│  💬 Chat disponible         │
│  [Contactar vendedor]       │
│                             │
│  ⭐ Calificar Transacción   │
│  (disponible después)       │
│                             │
│  📧 Confirmación enviada a  │
│  tu email                   │
│                             │
│  ┌────────────────────┐     │
│  │ Volver al Inicio   │     │
│  │ [Secundario]       │     │
│  └────────────────────┘     │
│                             │
│  [📞 Soporte 24/7]          │
│                             │
│  Próximas sugerencias:      │
│  • [Otra oferta similar]    │
│  • [Perfil del vendedor]    │
│                             │
└─────────────────────────────┘

Confirmación:
- Resumen de transacción
- Información de entrega
- Chat abierto
- Opciones siguientes
```

---

## 1️⃣6️⃣ MY PROFILE

```
┌─────────────────────────────┐
│ ← Back      [⚙️ Settings]   │
├─────────────────────────────┤
│                             │
│  ┌────────────────────┐     │
│  │   [Avatar Círculo] │     │
│  │   MC               │     │
│  └────────────────────┘     │
│                             │
│  Maria Campos               │
│  Diseñadora Freelance       │
│  🟢 Activa ahora            │
│  2.1km del centro           │
│                             │
│  ┌────────────────────┐     │
│  │ ⭐ 4.9 | 28 trans. │     │
│  │ $2,840 esta semana │     │
│  │ 96% respuesta      │     │
│  │ Nivel 5 🏆         │     │
│  └────────────────────┘     │
│                             │
│  ────────────────────────   │
│  Ofertas Actuales:          │
│  • Diseño Gráfico: $40/h    │
│  • Logo Design: $150-300    │
│  • Talleres Arte: $25       │
│                             │
│  [✏️ Editar Ofertas]        │
│  [➕ Agregar Oferta]        │
│                             │
│  ────────────────────────   │
│  Transacciones Hoy:         │
│  ✓ Logo design - $200       │
│  ✓ Gráficos redes - $150    │
│                             │
│  [📊 Ver Historial]         │
│                             │
│  ────────────────────────   │
│  Calificaciones:            │
│  ⭐⭐⭐⭐⭐ "¡Excelente!"      │
│  "Rápida y profesional"     │
│  Juan M. - Ayer             │
│                             │
│  [Ver todas (28)]           │
│                             │
│  ────────────────────────   │
│  Badges & Achievements:     │
│  🗺️  🍽️  🎉 💼 ⭐ 🚀        │
│                             │
└─────────────────────────────┘

Secciones:
- Avatar + info básica
- Stats y métricas
- Ofertas activas
- Transacciones recientes
- Calificaciones
- Badges
```

---

## 1️⃣7️⃣ EDIT PROFILE

```
┌─────────────────────────────┐
│ ← Back  Editar Perfil   ✓   │
├─────────────────────────────┤
│                             │
│  ┌────────────────────┐     │
│  │  [📸 Cambiar Avatar]     │
│  │        MC               │
│  └────────────────────┘     │
│                             │
│  ┌─────────────────────┐    │
│  │ Nombre Completo     │    │
│  │ Maria Campos        │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Biografía           │    │
│  │ "Diseñadora con 5+ │    │
│  │ años de experiencia"     │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │ Ubicación           │    │
│  │ 📍 Centro, 2.1km    │    │
│  └─────────────────────┘    │
│                             │
│  ────────────────────────   │
│  Sobre Mí:                  │
│                             │
│  Especialidades:            │
│  ☑ Diseño Gráfico          │
│  ☑ Branding                │
│  ☑ Ilustración             │
│  ☐ UX/UI Design            │
│  [+ Agregar]               │
│                             │
│  ────────────────────────   │
│  Disponibilidad:            │
│  Lunes: 9:00 AM - 6:00 PM   │
│  Martes: 9:00 AM - 6:00 PM  │
│  Miércoles: Descansa        │
│  ...                        │
│                             │
│  ────────────────────────   │
│  Información de Contacto:   │
│  Email: maria@mail.com      │
│  Teléfono: +56 9 1234 5678  │
│  WhatsApp: Habilitado ☑     │
│                             │
│  ┌─────────────────────┐    │
│  │ Guardar Cambios     │    │
│  │ [Gradiente]         │    │
│  └─────────────────────┘    │
│                             │
└─────────────────────────────┘
```

---

## 1️⃣8️⃣ MY OFFERS

```
┌─────────────────────────────┐
│ ← Back   Mis Ofertas        │
├─────────────────────────────┤
│                             │
│  Filtro: [Activas] [Pausadas]
│  [Completadas] [Canceladas] │
│                             │
│  ┌──────────────────────┐   │
│  │ 🟢 Activas (3)       │   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │ 🎨 Diseño Gráfico    │   │
│  │ $40/hora             │   │
│  │ 6h disponibles       │   │
│  │ ⭐ 4.9 (28 transacc) │   │
│  │ ────────────────────│   │
│  │ [✏️ Editar] [⏸ Pausar]   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │ 🏆 Diseño de Logos   │   │
│  │ $150-300 por proyecto    │
│  │ 2 vistas esta semana     │
│  │ ────────────────────│   │
│  │ [✏️ Editar] [⏸ Pausar]   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │ 🎨 Talleres Arte     │   │
│  │ $25/sesión           │   │
│  │ 5h disponibles       │   │
│  │ Próx: Viernes 10 AM  │   │
│  │ ────────────────────│   │
│  │ [✏️ Editar] [⏸ Pausar]   │
│  └──────────────────────┘   │
│                             │
│  ┌────────────────────┐     │
│  │ ➕ Agregar Oferta  │     │
│  │ [Secundario]       │     │
│  └────────────────────┘     │
│                             │
│  ⚫ Completadas (47)         │
│  [Mostrar anteriores]       │
│                             │
└─────────────────────────────┘
```

---

## 1️⃣9️⃣ TRANSACTION HISTORY

```
┌─────────────────────────────┐
│ ← Back  Historial           │
├─────────────────────────────┤
│                             │
│  Filtro: [Todo] [Compra]    │
│  [Venta] [Completadas]      │
│                             │
│  Rango de Fecha:            │
│  [Desde] [Hasta]  [Limpiar] │
│                             │
│  ────────────────────────   │
│  📊 Esta Semana:            │
│  Ganancias: $580            │
│  Transacciones: 7           │
│  ────────────────────────   │
│                             │
│  🟢 Hoy                     │
│  ┌──────────────────────┐   │
│  │ ✓ Venta              │   │
│  │ Tamales Caseros (2)  │   │
│  │ Doña Carmen          │   │
│  │ +$100  2 horas atrás │   │
│  │ [Calificar]          │   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │ ✓ Venta              │   │
│  │ Tamales Caseros (1)  │   │
│  │ Juan Pérez           │   │
│  │ +$50  5 horas atrás  │   │
│  │ [Calificar]          │   │
│  └──────────────────────┘   │
│                             │
│  ⚫ Ayer                     │
│  ┌──────────────────────┐   │
│  │ ✓ Venta              │   │
│  │ Tamales Caseros (1)  │   │
│  │ María López          │   │
│  │ +$50                 │   │
│  │ [Ver Detalles]       │   │
│  └──────────────────────┘   │
│                             │
│  [Mostrar más...]           │
│                             │
└─────────────────────────────┘

Funcionalidad:
- Filtrar por tipo
- Rango de fechas
- Búsqueda
- Exportar CSV
- Ver detalles
```

---

## 2️⃣0️⃣ REVIEWS / RATINGS

```
┌─────────────────────────────┐
│ ← Back   Mis Calificaciones │
├─────────────────────────────┤
│                             │
│  ┌────────────────────┐     │
│  │ ⭐ 5.0             │     │
│  │ Basado en 28       │     │
│  │ calificaciones     │     │
│  │                    │     │
│  │ ████████████ 100%  │     │
│  │ 5 estrellas (28)   │     │
│  │ ████░░░░░░░░  0%   │     │
│  │ 4 estrellas (0)    │     │
│  └────────────────────┘     │
│                             │
│  ────────────────────────   │
│  Calificaciones Recientes:  │
│                             │
│  ┌──────────────────────┐   │
│  │ ⭐⭐⭐⭐⭐              │   │
│  │ "¡Riquísimos los     │   │
│  │ tamales! Exacto      │   │
│  │ como la abuela."      │   │
│  │ Juan M.              │   │
│  │ 2 horas atrás        │   │
│  │ Compra: Tamales ($50)    │
│  │ [👍 Útil] [⊙ Reportar]   │
│  └──────────────────────┘   │
│                             │
│  ┌──────────────────────┐   │
│  │ ⭐⭐⭐⭐⭐              │   │
│  │ "Entrega rápida,     │   │
│  │ producto fresco."    │   │
│  │ María L.             │   │
│  │ 1 día atrás          │   │
│  │ Compra: Tamales ($50)    │
│  │ [👍 Útil] [⊙ Reportar]   │
│  └──────────────────────┘   │
│                             │
│  [Ver todas (28)]           │
│                             │
└─────────────────────────────┘
```

---

## 2️⃣1️⃣ SETTINGS

```
┌─────────────────────────────┐
│ ← Back   Configuración      │
├─────────────────────────────┤
│                             │
│  👤 CUENTA                  │
│  ┌──────────────────────┐   │
│  │ Editar Perfil        │   │
│  │ Cambiar Contraseña   │   │
│  │ Verificar Email       │   │
│  │ Verificar Teléfono    │   │
│  │ Eliminar Cuenta       │   │
│  └──────────────────────┘   │
│                             │
│  🔔 NOTIFICACIONES          │
│  ┌──────────────────────┐   │
│  │ ☑ Mensajes           │   │
│  │ ☑ Nuevas Ofertas    │   │
│  │ ☑ Calificaciones     │   │
│  │ ☑ Recordatorios      │   │
│  │ ☑ Newsletter         │   │
│  └──────────────────────┘   │
│                             │
│  🛡️ PRIVACIDAD & SEGURIDAD │
│  ┌──────────────────────┐   │
│  │ Sesiones Activas     │   │
│  │ Apps Conectadas      │   │
│  │ Autenticación 2FA    │   │
│  │ Política de Privacidad    │
│  │ Términos de Servicio      │
│  └──────────────────────┘   │
│                             │
│  💳 PAGOS                   │
│  ┌──────────────────────┐   │
│  │ Métodos de Pago      │   │
│  │ Historial Facturas   │   │
│  │ Información Bancaria  │   │
│  │ Impuestos/1099       │   │
│  └──────────────────────┘   │
│                             │
│  📱 PREFERENCIAS            │
│  ┌──────────────────────┐   │
│  │ Idioma: Español ▼    │   │
│  │ Moneda: USD ▼        │   │
│  │ Tema: Oscuro ▼       │   │
│  │ Unidades: km ▼       │   │
│  └──────────────────────┘   │
│                             │
│  ℹ️ AYUDA & SOPORTE         │
│  ┌──────────────────────┐   │
│  │ Centro de Ayuda      │   │
│  │ Contactar Soporte    │   │
│  │ Reportar Problema    │   │
│  │ Sugerir Mejora       │   │
│  │ Acerca de Comunity   │   │
│  │ Versión: 1.0.0       │   │
│  └──────────────────────┘   │
│                             │
│  ┌────────────────────┐     │
│  │ 🚪 Cerrar Sesión   │     │
│  │ [Rojo]             │     │
│  └────────────────────┘     │
│                             │
└─────────────────────────────┘
```

---

## 2️⃣2️⃣ PREFERENCES

```
[Similar a Settings, con más detalle en preferencias personales]

- Zona horaria
- Formato de fecha
- Notificaciones por hora
- Tipos de ofertas preferidas
- Radio máximo
- Presupuesto min/max
```

---

## 2️⃣3️⃣ HELP & SUPPORT

```
┌─────────────────────────────┐
│ ← Back   Ayuda y Soporte    │
├─────────────────────────────┤
│                             │
│  🔍 Buscar ayuda:           │
│  ┌─────────────────────┐    │
│  │ ¿Cómo...?          │    │
│  └─────────────────────┘    │
│                             │
│  ❓ PREGUNTAS FRECUENTES    │
│                             │
│  ┌──────────────────────┐   │
│  │ ► ¿Cómo crear       │   │
│  │   una oferta?        │   │
│  │ ► ¿Cómo contactar?  │   │
│  │ ► ¿Es seguro?        │   │
│  │ ► ¿Cuáles son       │   │
│  │   las comisiones?    │   │
│  │ ► ¿Cómo pagar?       │   │
│  │ ► ¿Cómo refundar?    │   │
│  │ ► ¿Cómo reportar?    │   │
│  └──────────────────────┘   │
│                             │
│  📞 CONTACTAR SOPORTE       │
│  ┌──────────────────────┐   │
│  │ Email: support@...   │   │
│  │ Chat: 24/7 🟢        │   │
│  │ Teléfono: +56 ...    │   │
│  │ WhatsApp: +56 ...    │   │
│  │ Redes Sociales       │   │
│  └──────────────────────┘   │
│                             │
│  📋 INFORMACIÓN LEGAL       │
│  ┌──────────────────────┐   │
│  │ Términos de Servicio │   │
│  │ Política de Privacidad    │
│  │ Política de Cookies  │   │
│  │ Política de Devoluciones  │
│  └──────────────────────┘   │
│                             │
│  [Chat con Soporte]         │
│                             │
└─────────────────────────────┘
```

---

## 2️⃣4️⃣ ABOUT

```
┌─────────────────────────────┐
│ ← Back   Acerca de Comunity │
├─────────────────────────────┤
│                             │
│  🚀 Comunity v1.0.0         │
│                             │
│  Economía Local en Tiempo   │
│  Real. Conecta personas en  │
│  un radio de 5km para       │
│  transacciones inmediatas.  │
│                             │
│  ────────────────────────   │
│  ¿Qué es Comunity?          │
│                             │
│  Somos una plataforma...    │
│  [Descripción larga]        │
│                             │
│  ────────────────────────   │
│  Nuestro Equipo             │
│  👥 +50 personas            │
│  🌍 América Latina          │
│  💪 Apasionados por la      │
│     economía local          │
│                             │
│  ────────────────────────   │
│  Recursos:                  │
│  🌐 Sitio Web: ...          │
│  🐦 Twitter: @ComunityApp   │
│  📘 Facebook: CommunityApp  │
│  📧 Email: info@...         │
│                             │
│  ────────────────────────   │
│  Créditos & Atribuciones   │
│  [Librerías, diseñadores]   │
│                             │
│  ────────────────────────   │
│  Versión Build:             │
│  1.0.0 (Build 42)           │
│  Última actualización:       │
│  Junio 2025                 │
│                             │
│  [🐞 Reportar Bug]          │
│  [⭐ Calificar App]         │
│                             │
└─────────────────────────────┘
```

---

## RESUMEN DE NAVEGACIÓN

```
Login → Home (Feed)
         ├─ Discover
         ├─ Announce (modal)
         ├─ Map
         ├─ Chat/Conversations
         │  └─ Chat Detail
         ├─ Profile
         │  ├─ Edit Profile
         │  ├─ My Offers
         │  ├─ Transaction History
         │  └─ Reviews
         └─ Notifications
             └─ Offer Detail
                 ├─ Confirm Transaction
                 ├─ Payment
                 └─ Complete

Settings:
├─ Account
├─ Notifications
├─ Privacy & Security
├─ Payment Methods
├─ Preferences
├─ Help & Support
└─ About
```

---

**Esta es la estructura completa de 24 pantallas principales del aplicativo Comunity.**

Cada pantalla está diseñada para:
- ✅ Ser clara y funcional
- ✅ Seguir la guía de marca (colores, tipografía)
- ✅ Optimizar para móvil (primero)
- ✅ Tener flujos lógicos
- ✅ Ser accesible

Próxima etapa: Crear wireframes en Figma/Adobe XD
