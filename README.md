# Leyes estatales 🇲🇽

Texto vigente de leyes de las entidades federativas, un archivo por artículo,
versionado en git para dejar un **rastro auditable de las reformas**.

Hoy: las constituciones de las 32 entidades.

> Repo de **datos**. La lógica que genera estos archivos vive en
> [`constitucion-extractor`](https://github.com/OpenCodice/constitucion-extractor)
> (un *perfil de fuente* por documento). Aquí no hay código: cada commit
> corresponde a una versión del texto, idealmente a una reforma publicada en el
> periódico oficial del estado.

Complementa al repo federal
[`constitucion-mexicana`](https://github.com/OpenCodice/constitucion-mexicana).

## Estructura: `{estado}/{ley}/`

```
{estado}/
└── {ley}/
    ├── fuente/constitucion.pdf   ← PDF oficial (para citar y resaltar)
    │   (Baja California Sur solo publica Word: ahí van el .doc oficial y el
    │    PDF que genera LibreOffice en la vigilancia, que es el que se lee)
    ├── articulos/NNN.md          ← capa 1: texto fiel, fuente de verdad
    └── metadata/                 ← capa 3: índice derivado, regenerable
        ├── articulos.json        ·  índice + versión + fuente
        ├── reformas.json         ·  mapa reforma → artículos
        ├── pasajes.jsonl         ·  bloques citables (con `ambito`)
        └── segmentos/NNN.json    ·  artículo descompuesto en bloques
```

El nivel `{ley}` queda explícito (hoy solo `constitucion/`) para que, más
adelante, otras leyes estatales —códigos civil/penal, leyes orgánicas— quepan
sin reorganizar el repo. `git log {estado}/{ley}/` es la historia de reformas de
esa ley en ese estado.

## Principio: texto vs. metadata

El **texto** (`articulos/*.md`) es la fuente de verdad; **git** es el detector
de cambios. La **metadata** (`metadata/`) es derivada y best-effort: se regenera
desde el texto y nunca es fuente de cita. Por eso una mejora del parser no
ensucia el historial del texto.

## Estados presentes

<!-- ESTADOS:INICIO -->
| Estado | Carpeta | Publicada por |
|---|---|---|
| Aguascalientes | [`aguascalientes/constitucion/`](aguascalientes/constitucion/) | Periódico Oficial del Estado de Aguascalientes — Congreso del Estado de Aguascalientes |
| Baja California | [`baja-california/constitucion/`](baja-california/constitucion/) | H. Congreso del Estado de Baja California |
| Baja California Sur | [`baja-california-sur/constitucion/`](baja-california-sur/constitucion/) | Boletín Oficial del Gobierno del Estado de Baja California Sur — H. Congreso del Estado de Baja California Sur (PDF generado del Word oficial) |
| Campeche | [`campeche/constitucion/`](campeche/constitucion/) | Congreso del Estado de Campeche (Compendio Jurídico, legislacion.congresocam.gob.mx) |
| Ciudad de México | [`cdmx/constitucion/`](cdmx/constitucion/) | Gaceta Oficial de la Ciudad de México — Congreso de la Ciudad de México |
| Chiapas | [`chiapas/constitucion/`](chiapas/constitucion/) | H. Congreso del Estado de Chiapas (Legislación vigente) |
| Chihuahua | [`chihuahua/constitucion/`](chihuahua/constitucion/) | H. Congreso del Estado de Chihuahua (Biblioteca Legislativa) |
| Coahuila | [`coahuila/constitucion/`](coahuila/constitucion/) | Periódico Oficial del Estado de Coahuila de Zaragoza — Congreso del Estado de Coahuila de Zaragoza |
| Colima | [`colima/constitucion/`](colima/constitucion/) | Periódico Oficial "El Estado de Colima" — Dirección de Proceso Legislativo del H. Congreso del Estado de Colima |
| Durango | [`durango/constitucion/`](durango/constitucion/) | Periódico Oficial del Gobierno del Estado de Durango — H. Congreso del Estado de Durango |
| Estado de México | [`edomex/constitucion/`](edomex/constitucion/) | Periódico Oficial «Gaceta del Gobierno» — Gobierno del Estado de México (Legislación vigente) |
| Guanajuato | [`guanajuato/constitucion/`](guanajuato/constitucion/) | Periódico Oficial del Gobierno del Estado de Guanajuato — H. Congreso del Estado de Guanajuato |
| Guerrero | [`guerrero/constitucion/`](guerrero/constitucion/) | Periódico Oficial del Gobierno del Estado de Guerrero — H. Congreso del Estado de Guerrero |
| Hidalgo | [`hidalgo/constitucion/`](hidalgo/constitucion/) | Periódico Oficial del Estado de Hidalgo — Congreso del Estado de Hidalgo (Instituto de Estudios Legislativos) |
| Jalisco | [`jalisco/constitucion/`](jalisco/constitucion/) | Periódico Oficial del Estado de Jalisco — Congreso del Estado de Jalisco |
| Michoacán | [`michoacan/constitucion/`](michoacan/constitucion/) | Periódico Oficial del Gobierno del Estado de Michoacán — H. Congreso del Estado de Michoacán de Ocampo |
| Morelos | [`morelos/constitucion/`](morelos/constitucion/) | Periódico Oficial «Tierra y Libertad» — Consejería Jurídica del Poder Ejecutivo del Estado de Morelos |
| Nayarit | [`nayarit/constitucion/`](nayarit/constitucion/) | Periódico Oficial del Estado de Nayarit — Congreso del Estado de Nayarit |
| Nuevo León | [`nuevo-leon/constitucion/`](nuevo-leon/constitucion/) | Periódico Oficial del Estado de Nuevo León — H. Congreso del Estado de Nuevo León |
| Oaxaca | [`oaxaca/constitucion/`](oaxaca/constitucion/) | Periódico Oficial del Estado de Oaxaca — H. Congreso del Estado Libre y Soberano de Oaxaca |
| Puebla | [`puebla/constitucion/`](puebla/constitucion/) | Periódico Oficial del Estado de Puebla — Orden Jurídico Poblano, Secretaría de Gobernación |
| Querétaro | [`queretaro/constitucion/`](queretaro/constitucion/) | Periódico Oficial «La Sombra de Arteaga» — Poder Legislativo del Estado de Querétaro |
| Quintana Roo | [`quintana-roo/constitucion/`](quintana-roo/constitucion/) | Periódico Oficial del Estado de Quintana Roo — Congreso del Estado de Quintana Roo |
| San Luis Potosí | [`san-luis-potosi/constitucion/`](san-luis-potosi/constitucion/) | Periódico Oficial del Estado de San Luis Potosí — Congreso del Estado de San Luis Potosí (Instituto de Investigación y Evaluación Legislativa) |
| Sinaloa | [`sinaloa/constitucion/`](sinaloa/constitucion/) | Periódico Oficial «El Estado de Sinaloa» — H. Congreso del Estado de Sinaloa |
| Sonora | [`sonora/constitucion/`](sonora/constitucion/) | Boletín Oficial del Gobierno del Estado de Sonora — H. Congreso del Estado de Sonora |
| Tabasco | [`tabasco/constitucion/`](tabasco/constitucion/) | Periódico Oficial del Estado de Tabasco — H. Congreso del Estado de Tabasco |
| Tamaulipas | [`tamaulipas/constitucion/`](tamaulipas/constitucion/) | Periódico Oficial del Estado de Tamaulipas — H. Congreso del Estado de Tamaulipas |
| Tlaxcala | [`tlaxcala/constitucion/`](tlaxcala/constitucion/) | Periódico Oficial del Gobierno del Estado de Tlaxcala — Congreso del Estado de Tlaxcala |
| Veracruz | [`veracruz/constitucion/`](veracruz/constitucion/) | Gaceta Oficial del Estado de Veracruz — H. Congreso del Estado de Veracruz |
| Yucatán | [`yucatan/constitucion/`](yucatan/constitucion/) | H. Congreso del Estado de Yucatán (Secretaría General del Poder Legislativo, Unidad de Servicios Técnico-Legislativos) |
| Zacatecas | [`zacatecas/constitucion/`](zacatecas/constitucion/) | Poder Legislativo del Estado de Zacatecas (Congreso del Estado, LXV Legislatura) |
<!-- ESTADOS:FIN -->

La tabla la regenera `scripts/gen_readme.py` al dar de alta un estado. Cada
semana, la vigilancia resuelve la URL vigente del PDF de cada estado con
[`scripts/resolver_pdf.py`](https://github.com/OpenCodice/constitucion-extractor/blob/main/scripts/resolver_pdf.py)
del extractor, porque los congresos estatales no exponen una URL estable; el
cómo de cada estado está en su módulo de
[`extractor/estados/`](https://github.com/OpenCodice/constitucion-extractor/tree/main/extractor/estados).
La situación de las 32 (incluidas las que faltan y por qué) está en
[`estados.json`](https://github.com/OpenCodice/constitucion-extractor/blob/main/estados.json).

## Regenerar

```bash
# desde constitucion-extractor
python -m extractor build \
  --pdf  ../leyes-estatales/jalisco/constitucion/fuente/constitucion.pdf \
  --out  ../leyes-estatales/jalisco/constitucion \
  --perfil jalisco
python -m extractor validar --out ../leyes-estatales/jalisco/constitucion --perfil jalisco
```

## Automatización (GitHub Actions)

Los workflows en `.github/workflows/` corren un job por estado:

| Workflow | Disparo | Qué hace |
|----------|---------|----------|
| `vigilar-estatales.yml` | lunes / manual | resuelve la URL vigente (`resolver_pdf.py`), regenera, verifica cada artículo cambiado contra el PDF con un agente y abre PR |
| `revisar-pr.yml` | cada PR | valida invariantes por estado (GATE) y fusiona solo el PR que llegó verificado |

El watcher es **autónomo**: cada lunes resuelve el PDF vigente de cada estado y,
si el texto cambió, abre un PR (uno por estado) que se fusiona solo cuando la
extracción quedó verificada contra el PDF. El título del commit distingue una
**reforma** de una **corrección de extracción**. Si un estado cambia su sitio y
el resolver falla, ese job avisa en rojo y puedes relanzarlo a mano con los
inputs `estado` + `pdf_url`.

### Secrets requeridos (de la organización)

| Secret | Para qué | Workflows |
|--------|----------|-----------|
| `CLAUDE_CODE_OAUTH_TOKEN` | token de suscripción del agente que verifica y repara | `vigilar-estatales` |
| `PR_TOKEN` | PAT que abre y fusiona los PR y publica arreglos en el extractor | `vigilar-estatales`, `revisar-pr` |

## Licencia

[CC0 1.0](LICENSE): dominio público. Los textos legislativos no son objeto de
derechos de autor (Ley Federal del Derecho de Autor, artículo 14, fracción
VIII); con CC0, la compilación, la metadata y el historial también se pueden
usar, copiar y redistribuir sin restricciones ni atribución.
