#!/usr/bin/env python3
"""Regenera la tabla de estados del README desde las carpetas {estado}/constitucion/.

Solo reemplaza el bloque entre `ESTADOS:INICIO` y `ESTADOS:FIN`. La tabla no
lleva cifras que cambien con cada reforma (artículos, fechas), para que los PR
de vigilancia, uno por estado, no choquen en el README: esas cifras están en
constitucion.app/leyes. Es autocontenido: no depende del extractor.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

NOMBRES = {
    "aguascalientes": "Aguascalientes", "baja-california": "Baja California",
    "baja-california-sur": "Baja California Sur", "campeche": "Campeche",
    "chiapas": "Chiapas", "chihuahua": "Chihuahua", "cdmx": "Ciudad de México",
    "coahuila": "Coahuila", "colima": "Colima", "durango": "Durango",
    "edomex": "Estado de México", "guanajuato": "Guanajuato", "guerrero": "Guerrero",
    "hidalgo": "Hidalgo", "jalisco": "Jalisco", "michoacan": "Michoacán",
    "morelos": "Morelos", "nayarit": "Nayarit", "nuevo-leon": "Nuevo León",
    "oaxaca": "Oaxaca", "puebla": "Puebla", "queretaro": "Querétaro",
    "quintana-roo": "Quintana Roo", "san-luis-potosi": "San Luis Potosí",
    "sinaloa": "Sinaloa", "sonora": "Sonora", "tabasco": "Tabasco",
    "tamaulipas": "Tamaulipas", "tlaxcala": "Tlaxcala", "veracruz": "Veracruz",
    "yucatan": "Yucatán", "zacatecas": "Zacatecas",
}


def tabla() -> str:
    filas = ["| Estado | Carpeta | Publicada por |", "|---|---|---|"]
    presentes = []
    for d in sorted(REPO.glob("*/constitucion/metadata/articulos.json")):
        slug = d.parts[-4]
        meta = json.loads(d.read_text(encoding="utf-8"))
        presentes.append(slug)
        fuente = (meta.get("fuente") or "").replace("|", "\\|")
        filas.append(f"| {NOMBRES.get(slug, slug)} | [`{slug}/constitucion/`]({slug}/constitucion/) | {fuente} |")
    faltan = [n for s, n in NOMBRES.items() if s not in presentes]
    nota = (f"\n\nFaltan {len(faltan)}: {', '.join(sorted(faltan))}. Por qué, en "
            "[constitucion.app/leyes](https://constitucion.app/leyes#estados).") if faltan else ""
    return "\n".join(filas) + nota


def main() -> None:
    readme = REPO / "README.md"
    t = readme.read_text(encoding="utf-8")
    nuevo = re.sub(r"(<!-- ESTADOS:INICIO -->).*?(<!-- ESTADOS:FIN -->)",
                   lambda m: f"{m.group(1)}\n{tabla()}\n{m.group(2)}", t, flags=re.S)
    readme.write_text(nuevo, encoding="utf-8")


if __name__ == "__main__":
    main()
