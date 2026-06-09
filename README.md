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

| Estado | Ley | Artículos | Fuente |
|--------|-----|-----------|--------|
| Jalisco | Constitución | 122 | Periódico Oficial del Estado de Jalisco |
| Ciudad de México | Constitución | 71 | Gaceta Oficial de la Ciudad de México |

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
| `vigilar-estatales.yml` | lunes / manual | descarga el PDF oficial, regenera y abre PR si hubo reforma |
| `notificar-web.yml` | push a `main` | avisa a `constitucion-web` para reingestar el namespace estatal |

> ⚠️ `vigilar-estatales` es *best-effort*: varios estados no publican el PDF en
> una URL fija (la de Jalisco lleva la fecha embebida y rota en cada reforma).
> Los estados sin URL descargable quedan en vigilancia manual; cuando una URL
> rota, relánzalo con el input `pdf_url`.
