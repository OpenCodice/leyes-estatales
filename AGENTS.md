# leyes-estatales — guía para agentes

Texto vigente de las constituciones estatales de México, un archivo por
artículo, versionado para que el historial de git sea el registro de sus
reformas. Hoy: Jalisco y Ciudad de México. Es un repo de datos: aquí no hay
código.

**No edites a mano nada de `{estado}/constitucion/articulos/` ni de su
`metadata/`.** Todo se genera con
[`constitucion-extractor`](https://github.com/OpenCodice/constitucion-extractor)
a partir de `{estado}/constitucion/fuente/constitucion.pdf`. Si un artículo está
mal, el arreglo va en el extractor.

## Estructura

`{estado}/constitucion/` con la misma forma que `constitucion-mexicana`:
`articulos/NNN.md` (el texto), `metadata/` (derivada) y `fuente/` (el PDF).

## Cómo cambia este repo

El workflow `vigilar-*` corre cada lunes 09:00 UTC (y a mano con
`gh workflow run`). Descarga el PDF oficial, regenera con el extractor y, si
cambió texto, lanza un agente (Claude Code) que compara cada unidad cambiada
contra el PDF y repara el extractor si hace falta. Después abre un PR:

- Con la etiqueta `verificado`, `revisar-pr` corre los invariantes (`validar`)
  y lo fusiona solo, con squash.
- Si no quedó verificado, no se abre PR: el texto vigente se queda como está,
  lo no publicado se anota en el resumen de la corrida y la siguiente vigilancia
  lo reintenta. Nada se asigna a una persona.

El título del commit lo declara el agente y distingue una **reforma** (cambió la
ley) de una **corrección de extracción** (misma ley, mejor lectura del PDF). No
lo cambies a mano al fusionar: la bitácora dependerá de él.

Un job `salud` renueva el cron en cada corrida y, si el workflow falla, lo
relanza una vez; si el reintento también falla, deja un issue (sin asignar) como
constancia y la vigilancia de la semana siguiente lo vuelve a intentar.

`vigilar-estatales` corre un job por estado (matriz). Los congresos estatales
cambian la URL de su PDF con cada reforma; la resuelve
`scripts/resolver_pdf.py` del extractor.

## Agregar un estado

El perfil y el resolver se agregan en el extractor (ver su `AGENTS.md`). Aquí
hay que sumar el estado a la matriz de `vigilar-estatales.yml` y a `ESTADOS` en
`revisar-pr.yml`.

## Lo único que se edita aquí

Los workflows de `.github/workflows/` y la documentación. Trabaja en `main`,
con `git pull --ff-only` antes.
