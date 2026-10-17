# JULIETA VA AL COLE

Videojuego móvil en HTML: Isaías o Nacho empujan el carrito de Julieta desde la puerta principal hasta Taberna Torneo (Sevilla).

## Reglas del proyecto
- Conservar el escenario original, la salida desde la puerta principal, las puertas intermedias y la llegada a Taberna Torneo.
- Pantalla inicial para elegir **Isaías** (mayor, sin gafas) o **Nacho** (menor, gafas rojas).
- Avance automático lateral; tocar la pantalla para saltar.
- Animación al caminar mediante dos fotogramas de piernas alternas por niño.
- **No cambiar el fondo, la escala ni las mecánicas** al retocar los sprites.
- No usar ilustraciones de interfaz generadas como sustitutos del juego.
- Mantener una versión estable y otra en desarrollo; guardar versiones antes de cada modificación.

## Estado 2026-10-17
- Versión estable de referencia: `carrito_taberna_v10_recortes_y_fondo_corregidos.html`.
- Versión con selección y personajes: `julieta_va_al_cole_personajes_integrados.html`.
- Versión en desarrollo: `JULIETA_VA_AL_COLE_animacion_corregida.html`.
- Problema pendiente: limpiar los recortes de los fotogramas; se aprecian artefactos y transparencias.
- Los HTML y PNG completos aún están en la copia de seguridad local, **no en este repositorio**.

## Estructura prevista
`index.html`: versión jugable estable.
`dev/`: pruebas de animación.
`assets/personajes/`: PNG originales y fotogramas.
`assets/escenario/`: escenario aprobado.
`backups/`: hitos anteriores.

**No sustituir la versión estable sin validar la nueva.**
