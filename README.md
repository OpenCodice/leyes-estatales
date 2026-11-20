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
| Estado | Carpeta | Publicada por | Otras leyes |
|---|---|---|---|
| Aguascalientes | [`aguascalientes/constitucion/`](aguascalientes/constitucion/) | Periódico Oficial del Estado de Aguascalientes — Congreso del Estado de Aguascalientes | — |
| Baja California | [`baja-california/constitucion/`](baja-california/constitucion/) | Periódico Oficial del Estado de Baja California — H. Congreso del Estado de Baja California | — |
| Baja California Sur | [`baja-california-sur/constitucion/`](baja-california-sur/constitucion/) | Boletín Oficial del Gobierno del Estado de Baja California Sur — H. Congreso del Estado de Baja California Sur (PDF generado del Word oficial) | — |
| Campeche | [`campeche/constitucion/`](campeche/constitucion/) | Periódico Oficial del Estado de Campeche — Congreso del Estado de Campeche | — |
| Ciudad de México | [`cdmx/constitucion/`](cdmx/constitucion/) | Gaceta Oficial de la Ciudad de México — Consejería Jurídica y de Servicios Legales | [CIPE CDMX](cdmx/codigo-de-instituciones-y-procedimientos-electorales/), [CP CDMX](cdmx/codigo-penal/), [LAMVLV CDMX](cdmx/ley-de-acceso-de-las-mujeres-a-una-vida-libre-de-violencia/), [LDNNA CDMX](cdmx/ley-de-los-derechos-de-ninas-ninos-y-adolescentes/), [LOA CDMX](cdmx/ley-organica-de-alcaldias/), [LOC CDMX](cdmx/ley-organica-del-congreso/) |
| Chiapas | [`chiapas/constitucion/`](chiapas/constitucion/) | Periódico Oficial del Estado de Chiapas — H. Congreso del Estado de Chiapas | — |
| Chihuahua | [`chihuahua/constitucion/`](chihuahua/constitucion/) | Periódico Oficial del Estado de Chihuahua — H. Congreso del Estado de Chihuahua | — |
| Coahuila | [`coahuila/constitucion/`](coahuila/constitucion/) | Periódico Oficial del Estado de Coahuila de Zaragoza — Congreso del Estado de Coahuila de Zaragoza | — |
| Colima | [`colima/constitucion/`](colima/constitucion/) | Periódico Oficial "El Estado de Colima" — Dirección de Proceso Legislativo del H. Congreso del Estado de Colima | — |
| Durango | [`durango/constitucion/`](durango/constitucion/) | Periódico Oficial del Gobierno del Estado de Durango — H. Congreso del Estado de Durango | — |
| Estado de México | [`edomex/constitucion/`](edomex/constitucion/) | Periódico Oficial «Gaceta del Gobierno» — Gobierno del Estado de México (Legislación vigente) | — |
| Guanajuato | [`guanajuato/constitucion/`](guanajuato/constitucion/) | Periódico Oficial del Gobierno del Estado de Guanajuato — H. Congreso del Estado de Guanajuato | [LE Gto](guanajuato/ley-de-educacion/), [LFS Gto](guanajuato/ley-de-fiscalizacion-superior/), [LIPE Gto](guanajuato/ley-de-instituciones-y-procedimientos-electorales/), [LOCCL Gto](guanajuato/ley-organica-del-centro-de-conciliacion-laboral/), [LOFG Gto](guanajuato/ley-organica-de-la-fiscalia-general/), [LOPJ Gto](guanajuato/ley-organica-del-poder-judicial/), [LOPL Gto](guanajuato/ley-organica-del-poder-legislativo/), [LOTJA Gto](guanajuato/ley-organica-del-tribunal-de-justicia-administrativa/), [LTAIP Gto](guanajuato/ley-de-transparencia-y-acceso-a-la-informacion-publica/), [LTSP Gto](guanajuato/ley-del-trabajo-de-los-servidores-publicos-al-servicio-del-estado-y-de-los-municipios/) |
| Guerrero | [`guerrero/constitucion/`](guerrero/constitucion/) | Periódico Oficial del Gobierno del Estado de Guerrero — H. Congreso del Estado de Guerrero | — |
| Hidalgo | [`hidalgo/constitucion/`](hidalgo/constitucion/) | Periódico Oficial del Estado de Hidalgo — Congreso del Estado de Hidalgo (Instituto de Estudios Legislativos) | — |
| Jalisco | [`jalisco/constitucion/`](jalisco/constitucion/) | Periódico Oficial del Estado de Jalisco — Congreso del Estado de Jalisco | [CAS Jalisco](jalisco/codigo-de-asistencia-social/), [CC Jalisco](jalisco/codigo-civil/), [CE Jalisco](jalisco/codigo-electoral/), [LOPE Jalisco](jalisco/ley-organica-del-poder-ejecutivo/), [LOPJ Jalisco](jalisco/ley-organica-del-poder-judicial/), [LOPL Jalisco](jalisco/ley-organica-del-poder-legislativo/) |
| Michoacán | [`michoacan/constitucion/`](michoacan/constitucion/) | Periódico Oficial del Gobierno del Estado de Michoacán — H. Congreso del Estado de Michoacán de Ocampo | — |
| Morelos | [`morelos/constitucion/`](morelos/constitucion/) | Periódico Oficial «Tierra y Libertad» — Consejería Jurídica del Poder Ejecutivo del Estado de Morelos | — |
| Nayarit | [`nayarit/constitucion/`](nayarit/constitucion/) | Periódico Oficial del Estado de Nayarit — Congreso del Estado de Nayarit | — |
| Nuevo León | [`nuevo-leon/constitucion/`](nuevo-leon/constitucion/) | Periódico Oficial del Estado de Nuevo León — H. Congreso del Estado de Nuevo León | [CE Congreso NL](nuevo-leon/codigo-de-etica-para-el-congreso/), [CF NL](nuevo-leon/codigo-fiscal/), [CP NL](nuevo-leon/codigo-penal/), [LAACS NL](nuevo-leon/ley-de-adquisiciones-arrendamientos-y-contratacion-de-servicios/), [LAHOTDU NL](nuevo-leon/ley-de-asentamientos-humanos-ordenamiento-territorial-y-desarrollo-urbano/), [LE NL](nuevo-leon/ley-electoral/), [LFS NL](nuevo-leon/ley-de-fiscalizacion-superior/), [LGM NL](nuevo-leon/ley-de-gobierno-municipal/), [LJA NL](nuevo-leon/ley-de-justicia-administrativa-para-el-estado-y-municipios/), [LJC NL](nuevo-leon/ley-de-justicia-civica/), [LJP NL](nuevo-leon/ley-de-juicio-politico/), [LN NL](nuevo-leon/ley-del-notariado/), [LOAP NL](nuevo-leon/ley-organica-de-la-administracion-publica/), [LOPJ NL](nuevo-leon/ley-organica-del-poder-judicial/), [LOPL NL](nuevo-leon/ley-organica-del-poder-legislativo/), [LPC NL](nuevo-leon/ley-de-proteccion-civil/), [LRA NL](nuevo-leon/ley-de-responsabilidades-administrativas/), [LRC NL](nuevo-leon/ley-del-registro-civil/), [LRP NL](nuevo-leon/ley-de-responsabilidad-patrimonial/), [LSP NL](nuevo-leon/ley-de-seguridad-publica/), [LTAIP NL](nuevo-leon/ley-de-transparencia-y-acceso-a-la-informacion-publica/) |
| Oaxaca | [`oaxaca/constitucion/`](oaxaca/constitucion/) | Periódico Oficial del Estado de Oaxaca — H. Congreso del Estado Libre y Soberano de Oaxaca | — |
| Puebla | [`puebla/constitucion/`](puebla/constitucion/) | Periódico Oficial del Estado de Puebla — Orden Jurídico Poblano, Secretaría de Gobernación | — |
| Querétaro | [`queretaro/constitucion/`](queretaro/constitucion/) | Periódico Oficial «La Sombra de Arteaga» — Poder Legislativo del Estado de Querétaro | [CA Qro](queretaro/codigo-ambiental/), [CPC Qro](queretaro/codigo-de-procedimientos-civiles/), [CU Qro](queretaro/codigo-urbano/), [LOAE Qro](queretaro/ley-organica-de-la-agencia-de-energia/), [LOCB Qro](queretaro/ley-organica-del-colegio-de-bachilleres/), [LOCCL Qro](queretaro/ley-organica-del-centro-de-conciliacion-laboral/), [LOEN Qro](queretaro/ley-organica-de-la-escuela-normal/), [LOPE Qro](queretaro/ley-organica-del-poder-ejecutivo/), [LOPJ Qro](queretaro/ley-organica-del-poder-judicial/), [LOTE Qro](queretaro/ley-organica-del-tribunal-electoral/), [LOTJA Qro](queretaro/ley-organica-del-tribunal-de-justicia-administrativa/), [LOUAQ](queretaro/ley-organica-de-la-universidad-autonoma-de-queretaro/), [LOUTEQ](queretaro/ley-organica-de-la-universidad-tecnologica-de-queretaro/) |
| Quintana Roo | [`quintana-roo/constitucion/`](quintana-roo/constitucion/) | Periódico Oficial del Estado de Quintana Roo — Congreso del Estado de Quintana Roo | — |
| San Luis Potosí | [`san-luis-potosi/constitucion/`](san-luis-potosi/constitucion/) | Periódico Oficial del Estado de San Luis Potosí — Congreso del Estado de San Luis Potosí (Instituto de Investigación y Evaluación Legislativa) | — |
| Sinaloa | [`sinaloa/constitucion/`](sinaloa/constitucion/) | Periódico Oficial «El Estado de Sinaloa» — H. Congreso del Estado de Sinaloa | — |
| Sonora | [`sonora/constitucion/`](sonora/constitucion/) | Boletín Oficial del Gobierno del Estado de Sonora — H. Congreso del Estado de Sonora | — |
| Tabasco | [`tabasco/constitucion/`](tabasco/constitucion/) | Periódico Oficial del Estado de Tabasco — H. Congreso del Estado de Tabasco | — |
| Tamaulipas | [`tamaulipas/constitucion/`](tamaulipas/constitucion/) | Periódico Oficial del Estado de Tamaulipas — H. Congreso del Estado de Tamaulipas | — |
| Tlaxcala | [`tlaxcala/constitucion/`](tlaxcala/constitucion/) | Periódico Oficial del Gobierno del Estado de Tlaxcala — Congreso del Estado de Tlaxcala | — |
| Veracruz | [`veracruz/constitucion/`](veracruz/constitucion/) | Gaceta Oficial del Estado de Veracruz — H. Congreso del Estado de Veracruz | — |
| Yucatán | [`yucatan/constitucion/`](yucatan/constitucion/) | Diario Oficial del Gobierno del Estado de Yucatán — H. Congreso del Estado de Yucatán | — |
| Zacatecas | [`zacatecas/constitucion/`](zacatecas/constitucion/) | Periódico Oficial del Gobierno del Estado de Zacatecas — Poder Legislativo del Estado de Zacatecas | — |
<!-- ESTADOS:FIN -->

La tabla la regenera `scripts/readme_estatales.py` del extractor al dar de alta
un estado. Cada
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

## Automatización

La vigilancia vive en el extractor, para que el historial de este repo solo
tenga cambios de texto legal:

<!-- AUTOMATIZACION:INICIO -->
| Dónde | Disparo | Qué hace |
|-------|---------|----------|
| `vigilar-estatales.yml` de [`constitucion-extractor`](https://github.com/OpenCodice/constitucion-extractor) | lunes (Worker `scheduler`) / manual | las constituciones: resuelve la URL vigente de cada estado, regenera, verifica cada artículo cambiado contra el PDF con un agente y abre aquí un PR por estado |
| `vigilar-leyes-estatales.yml` de [`fiscal-extractor`](https://github.com/OpenCodice/fiscal-extractor) | lunes (Worker `scheduler`) / manual | las demás leyes de cada estado: reprocesa las que cambiaron, da de alta las nuevas por tandas tras revisarlas enteras contra su PDF, repara el extractor cuando encuentra defectos y abre aquí un PR |
| `expandir-estatales.yml` de [`fiscal-extractor`](https://github.com/OpenCodice/fiscal-extractor) | miércoles (Worker `scheduler`) / manual | ronda de expansión: cuando la vigilancia anterior terminó, un agente escribe el registro de las leyes de un estado más y, si pasa las compuertas, lanza su vigilancia |
| `revisar-pr.yml` de los dos extractores | cada PR de vigilancia | valida en un job sin secretos los invariantes de cada documento y los trailers de cada commit (GATE) y fusiona solo el PR que llegó verificado |
<!-- AUTOMATIZACION:FIN -->

Cada lunes resuelve el PDF vigente de cada estado y, si el texto cambió, abre
un PR (uno por estado) que se fusiona solo cuando la extracción quedó
verificada contra el PDF. El título del commit distingue una **reforma** de una
**corrección de extracción**. Si un estado cambia su sitio y el resolver falla,
ese job avisa en rojo y se puede relanzar a mano con los inputs `estado` +
`pdf_url`.

## Licencia

[CC0 1.0](LICENSE): dominio público. Los textos legislativos no son objeto de
derechos de autor (Ley Federal del Derecho de Autor, artículo 14, fracción
VIII); con CC0, la compilación, la metadata y el historial también se pueden
usar, copiar y redistribuir sin restricciones ni atribución.
