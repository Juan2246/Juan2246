# Tu perfil, a tu manera

La presentación pública está en [README.md](README.md). Para editarla desde GitHub, abre el archivo y pulsa el lápiz. Usa **Preview** antes de guardar.

## Completar tu información

Busca **COMPLETAR** en el README. Los aportes y aprendizajes de cada proyecto conservan espacios desplegables para rellenar. La presentación y la sección «Hacia dónde apunto» contienen tus propios textos.

Tu nombre, formación, correo y herramientas parten de tu portafolio; el enlace de LinkedIn corresponde al perfil público de GitHub. Las descripciones de los proyectos parten de sus README. Actualiza estos datos cuando cambien.

## Qué hay en cada archivo

| Archivo | Qué cambia |
| --- | --- |
| `README.md` | Presentación, enlaces, proyectos y datos personales. |
| `assets/studio-banner-rye.png` | Portada actual del estudio, con letras ornamentales. La original se conserva en `studio-banner.png`. |
| `assets/headings/` | Títulos con Caveat Brush, en versiones clara y oscura. |
| `assets/icons/` | Pequeños GIF originales junto a los títulos. |
| `assets/contact-*.svg` | Iconos de portafolio, LinkedIn y correo. El destino se cambia en el README. |
| `assets/stack-*.svg` | Filas de iconos de tecnologías. |
| `assets/footer.svg` | Postal crema y lavanda con «¡Gracias!» grande, en Rye. |
| `.github/workflows/contributions.yml` | Generación automática de Snake y Pac-Man. |

Todos los elementos visuales se sirven desde este repositorio. Los proyectos se presentan con texto y enlaces, sin ilustraciones de portada.

## Tipografías y títulos

GitHub no permite aplicar una fuente personalizada al texto normal del README. Por eso los títulos se dibujan como SVG con **Caveat Brush**, una alternativa manuscrita a Scratchy. El pie utiliza **Rye**, de estilo ornamental. Las letras están convertidas en trazos: no hace falta que el visitante tenga esas fuentes instaladas. Cada imagen conserva un texto alternativo legible por lectores de pantalla.

La portada es una edición de imagen con un estilo parecido a Rye/Barnule, no una aplicación exacta del archivo de fuente. El resto del contenido sigue siendo texto normal, seleccionable y adaptable a la pantalla.

Para cambiar un título, edita el diccionario `HEADINGS` de `scripts/build-typography.py` y ejecuta `python scripts/build-typography.py` con `fonttools` instalado. Los GIF se pueden regenerar con `python scripts/build-icons.py`, que requiere Pillow. Los archivos de fuente y sus licencias OFL están en `assets/fonts/`.

## Animaciones de contribuciones

Se generan a partir de **Juan2246**, con versiones para fondo claro y oscuro. El workflow está programado una vez al día, a las 06:23 de Perú (11:23 UTC). GitHub puede retrasar las ejecuciones programadas.

También puedes abrir **Actions → Actualizar animaciones del perfil → Run workflow** para regenerarlas. No necesitas crear un token personal: utiliza el permiso de contenido del token automático del repositorio.

Los cuatro SVG resultantes se guardan en `assets/`. Si un día la generación falla, el perfil conserva las últimas imágenes publicadas. Para comprobarlo, entra en la pestaña Actions.

GitHub puede pausar los workflows programados de repositorios públicos después de 60 días sin actividad. En ese caso, vuelve a habilitar el workflow desde Actions.

El pie respeta la preferencia de movimiento reducido. Los GIF y los gráficos de contribuciones son animaciones en bucle. Pac-Man es una animación, no un juego interactivo dentro del README.

## Colores

- Azul de fondo: `#0b1020`
- Violeta: `#a78bfa`
- Cian: `#67e8f9`
- Melocotón: `#fda4af`

Los SVG se pueden editar como texto sin instalar herramientas. Conserva las etiquetas y cambia textos o códigos de color. Los cambios del PNG requieren editar o generar otra imagen.

## Recursos y créditos

- Portada creada para este perfil con la herramienta integrada de generación de imágenes. [Prompt de creación](assets/PORTADA.md).
- Iconos, GIF y pie: gráficos originales de este perfil.
- [Caveat Brush](https://fonts.google.com/specimen/Caveat+Brush) y [Rye](https://fonts.google.com/specimen/Rye): tipografías de Google Fonts, con licencias SIL OFL conservadas en `assets/fonts/`.
- [Skill Icons](https://github.com/tandpfun/skill-icons): iconos de tecnologías. [Licencia MIT conservada](assets/LICENSE-skill-icons.txt).
- [Platane/snk](https://github.com/Platane/snk): Snake sobre las contribuciones.
- [Arcade Contribution Graph](https://github.com/abozanona/pacman-contribution-graph): Pac-Man sobre las contribuciones.

Referencias de composición: [DenverCoder1](https://github.com/DenverCoder1), [Rafa Ballerini](https://github.com/rafaballerini), [Caneco](https://github.com/caneco) y [Thaiane](https://github.com/Thaiane). La composición y los textos de esta presentación se prepararon para Juan; no se copian biografías ajenas.
