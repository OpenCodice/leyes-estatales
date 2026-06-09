# leyes-estatales — guía para agentes

Texto vigente de las constituciones estatales de México, un archivo por
artículo, versionado para que el historial de git sea el registro de sus
reformas. Hoy: las 32 entidades; su situación está en `estados.json` del
extractor. Es un repo de datos: el único código es la validación de los PR
(`revisar-pr.yml`).

**No edites a mano nada de `{estado}/constitucion/articulos/` ni de su
`metadata/`.** Todo se genera con
[`constitucion-extractor`](https://github.com/OpenCodice/constitucion-extractor)
a partir de `{estado}/constitucion/fuente/constitucion.pdf`. Si un artículo está
mal, el arreglo va en el extractor.

## Estructura

`{estado}/constitucion/` con la misma forma que `constitucion-mexicana`:
`articulos/NNN.md` (el texto), `metadata/` (derivada) y `fuente/` (el PDF).

## Cómo cambia este repo

La vigilancia no vive aquí: es el workflow `vigilar-estatales.yml` de
[`constitucion-extractor`](https://github.com/OpenCodice/constitucion-extractor),
y la lanza cada lunes 09:00 UTC el Worker `scheduler` de Cloudflare (o a mano:
`gh workflow run vigilar-estatales.yml -R OpenCodice/constitucion-extractor`). Así el historial
de este repo solo tiene cambios de texto legal. Descarga el PDF oficial,
regenera con el extractor y, si cambió texto, lanza un agente (Claude Code) que
compara cada unidad cambiada contra el PDF y repara el extractor si hace falta.
Después abre aquí un PR:

- Con la etiqueta `verificado`, `revisar-pr` corre los invariantes (`validar`)
  y lo fusiona solo, con squash.
- Si no quedó verificado, no se abre PR: el texto vigente se queda como está,
  lo no publicado se anota en el resumen de la corrida y la siguiente vigilancia
  lo reintenta. Nada se asigna a una persona.

El título del commit lo declara el agente y distingue una **reforma** (cambió la
ley) de una **corrección de extracción** (misma ley, mejor lectura del PDF). No
lo cambies a mano al fusionar: la bitácora dependerá de él.

Si la vigilancia falla, se relanza una vez; si el reintento también falla,
deja un issue (sin asignar) en el extractor como constancia, y el vigilante del
`scheduler` la relanza si pasan más de 8 días sin correr.

La vigilancia corre un job por estado. La lista sale del registro del
extractor (`scripts/resolver_pdf.py --matriz`). Los congresos estatales cambian
la URL de su PDF con cada reforma; la resuelve el mismo script.

## Agregar un estado

El perfil y el resolver se agregan en el extractor (ver su `AGENTS.md`), y la
carpeta `{estado}/constitucion/` se construye con él. Nada más se toca:
la vigilancia toma los estados del resolver y `revisar-pr` valida cada carpeta
`*/constitucion` con el perfil del mismo nombre.

## Lo único que se edita aquí

`revisar-pr.yml` (la validación de los PR) y la documentación (el README fuera
de su bloque generado, que regenera `scripts/readme_estatales.py` del extractor
al dar de alta un estado). Trabaja en `main`,
con `git pull --ff-only` antes.
