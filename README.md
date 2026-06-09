# Leyes estatales 🇲🇽

Texto vigente de leyes de las entidades federativas, un archivo por artículo,
versionado en git para dejar un **rastro auditable de las reformas**.

> Repo de **datos**. La lógica que genera estos archivos vive en
> [`constitucion-extractor`](https://github.com/OpenCodice/constitucion-extractor)
> (un *perfil de fuente* por documento). Aquí no hay código: cada commit
> corresponde a una versión del texto, idealmente a una reforma publicada en el
> periódico oficial del estado.

Complementa al repo federal
[`constitucion-mexicana`](https://github.com/OpenCodice/constitucion-mexicana):
juntos alimentan el RAG, que responde **federal + tu estado en una sola
respuesta**.

## Estructura: `{estado}/{ley}/`

```
{estado}/
└── {ley}/
    ├── fuente/constitucion.pdf   ← PDF oficial (para citar y resaltar)
    ├── articulos/NNN.md          ← capa 1: texto fiel, fuente de verdad
    └── metadata/                 ← capa 3: índice derivado, regenerable
        ├── articulos.json        ·  índice + versión + fuente
        ├── reformas.json         ·  mapa reforma → artículos
        ├── pasajes.jsonl         ·  bloques citables para el RAG (con `ambito`)
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

| Estado | Ley | Artículos | Perfil | Fuente oficial |
|--------|-----|-----------|--------|----------------|
| Jalisco | Constitución | 122 | `jalisco` | [Biblioteca Virtual — Congreso del Estado de Jalisco](https://congresoweb.congresojal.gob.mx/bibliotecavirtual/busquedasleyes/Listado%272.cfm) |
| Ciudad de México | Constitución | 71 | `cdmx` | [Congreso de la Ciudad de México](https://www.congresocdmx.gob.mx/archivos/legislativas/constitucion_politica_de_la_ciudad_de_mexico.pdf) |

### Vínculos en uso (resueltos automáticamente)

El watcher no usa URLs fijas: las resuelve [`scripts/resolver_pdf.py`](https://github.com/OpenCodice/constitucion-extractor/blob/main/scripts/resolver_pdf.py)
del extractor, porque los congresos estatales no exponen una URL estable.

| Estado | Cómo se resuelve | Vínculo |
|--------|------------------|---------|
| Jalisco | **índice** (auto) — el PDF lleva la fecha embebida (`…-DDMMYY.pdf`) y rota en cada reforma; se lee el "Listado Completo" y se toma el más reciente | [Listado Completo](https://congresoweb.congresojal.gob.mx/bibliotecavirtual/busquedasleyes/Listado%272.cfm) |
| CDMX | **directo** (auto) — URL de nombre estable | [constitucion_politica_de_la_ciudad_de_mexico.pdf](https://www.congresocdmx.gob.mx/archivos/legislativas/constitucion_politica_de_la_ciudad_de_mexico.pdf) |

> Mantén esta tabla al día: si un estado cambia su sitio, se ajusta el registro
> `RESOLVERS` en `resolver_pdf.py` y se actualiza el vínculo de arriba.

## Regenerar

```bash
# desde constitucion-extractor
python -m extractor build \
  --pdf  ../leyes-estatales/jalisco/constitucion/fuente/constitucion.pdf \
  --out  ../leyes-estatales/jalisco/constitucion \
  --perfil jalisco
python -m extractor validar --out ../leyes-estatales/jalisco/constitucion --perfil jalisco
```

## Enriquecimiento (capa generada, no canónica)

`metadata/generado/NNN.json` es metadata de búsqueda generada por LLM (temas,
términos coloquiales, preguntas) para mejorar el *recall* del RAG. **No es texto
oficial ni fuente de cita**; está cuarentenada y se regenera por hash solo
cuando cambia el texto del artículo.

```bash
# desde constitucion-extractor (requiere OPENAI_API_KEY)
python -m extractor enriquecer \
  --pdf ../leyes-estatales/jalisco/constitucion/fuente/constitucion.pdf \
  --out ../leyes-estatales/jalisco/constitucion --perfil jalisco
```

## Automatización (GitHub Actions)

Los workflows en `.github/workflows/` iteran los estados presentes (matriz/loop
`estado:perfil:directorio`):

| Workflow | Disparo | Qué hace |
|----------|---------|----------|
| `revisar-pr.yml` | cada PR | valida invariantes por estado (GATE) + resumen LLM de los estados que cambiaron |
| `enriquecer.yml` | manual | (re)genera `metadata/generado/` de uno o todos los estados |
| `vigilar-estatales.yml` | lunes / manual | resuelve la URL vigente (`resolver_pdf.py`), regenera y abre PR si hubo reforma |
| `notificar-web.yml` | push a `main` | avisa a `constitucion-web` para reingestar el namespace estatal |

El watcher es **autónomo**: cada lunes resuelve el PDF vigente de cada estado y,
si el texto cambió, abre un PR (uno por estado). Si un estado cambia su sitio y
el resolver falla, ese job avisa en rojo y puedes relanzarlo a mano con los
inputs `estado` + `pdf_url`.

### Secrets requeridos (en este repo)

| Secret | Para qué | Workflows |
|--------|----------|-----------|
| `OPENAI_API_KEY` | enriquecimiento por LLM | `enriquecer`, `vigilar-estatales`, `revisar-pr` |
| `WEB_DISPATCH_TOKEN` | PAT con scope `repo` sobre `constitucion-web` para el `repository_dispatch` | `notificar-web` |
