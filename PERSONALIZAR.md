# Tu perfil, a tu manera

La presentación pública está en [README.md](README.md). Para editarla desde GitHub, abre el archivo y pulsa el lápiz. Usa **Preview** antes de guardar.

## Completar tu información

Busca **COMPLETAR** en el README. Dejé espacios para tu proyecto actual, aprendizaje, metas, colaboración, aportes a cada proyecto e intereses personales. Están en secciones desplegables: puedes rellenarlas a tu ritmo sin desarmar el diseño.

Tu nombre, formación, correo y herramientas parten de tu portafolio; el enlace de LinkedIn corresponde al perfil público de GitHub. Las descripciones de los proyectos parten de sus README. Actualiza estos datos cuando cambien.

## Qué hay en cada archivo

| Archivo | Qué cambia |
| --- | --- |
| `README.md` | Presentación, enlaces, proyectos y datos personales. |
| `assets/studio-banner.png` | Portada original del estudio frente a la costa. |
| `assets/intro.svg` | Terminal con tres frases animadas. Edita el texto dentro de las etiquetas `text`. |
| `assets/project-*.svg` | Portadas vectoriales animadas de los cuatro proyectos. |
| `assets/contact-*.svg` | Aspecto de los botones. El destino de cada botón se cambia en el README. |
| `assets/stack-*.svg` | Filas de iconos de tecnologías. |
| `assets/footer.svg` | Cierre con estrellas y una pequeña órbita animada. |
| `.github/workflows/contributions.yml` | Generación automática de Snake y Pac-Man. |

Todos los elementos visuales se sirven desde este repositorio. Las ilustraciones de proyectos son diagramas decorativos; no representan capturas reales ni métricas de uso.

## Animaciones de contribuciones

Se generan a partir de **Juan2246**, con versiones para fondo claro y oscuro. El workflow está programado una vez al día, a las 06:23 de Perú (11:23 UTC). GitHub puede retrasar las ejecuciones programadas.

También puedes abrir **Actions → Actualizar animaciones del perfil → Run workflow** para regenerarlas. No necesitas crear un token personal: utiliza el permiso de contenido del token automático del repositorio.

Los cuatro SVG resultantes se guardan en `assets/`. Si un día la generación falla, el perfil conserva las últimas imágenes publicadas. Para comprobarlo, entra en la pestaña Actions.

GitHub puede pausar los workflows programados de repositorios públicos después de 60 días sin actividad. En ese caso, vuelve a habilitar el workflow desde Actions.

Las animaciones propias de la terminal, las tarjetas y el pie respetan la preferencia de movimiento reducido. Los gráficos de contribuciones los generan herramientas externas y pueden comportarse de otra manera. Pac-Man es una animación, no un juego interactivo dentro del README.

## Colores

- Azul de fondo: `#0b1020`
- Violeta: `#a78bfa`
- Cian: `#67e8f9`
- Melocotón: `#fda4af`

Los SVG se pueden editar como texto sin instalar herramientas. Conserva las etiquetas y cambia textos o códigos de color. Los cambios del PNG requieren editar o generar otra imagen.

## Recursos y créditos

- Portada creada para este perfil con la herramienta integrada de generación de imágenes. [Prompt de creación](assets/PORTADA.md).
- Terminal, botones, tarjetas y pie: gráficos SVG originales de este perfil.
- [Skill Icons](https://github.com/tandpfun/skill-icons): iconos de tecnologías. [Licencia MIT conservada](assets/LICENSE-skill-icons.txt).
- [Platane/snk](https://github.com/Platane/snk): Snake sobre las contribuciones.
- [Arcade Contribution Graph](https://github.com/abozanona/pacman-contribution-graph): Pac-Man sobre las contribuciones.

Referencias de composición: [DenverCoder1](https://github.com/DenverCoder1), [Rafa Ballerini](https://github.com/rafaballerini), [Caneco](https://github.com/caneco) y [Thaiane](https://github.com/Thaiane). La composición y los textos de esta presentación se prepararon para Juan; no se copian biografías ajenas.
