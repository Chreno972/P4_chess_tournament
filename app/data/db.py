"""Importe la librairie tinydb
"""
from tinydb import TinyDB, Query


DB = TinyDB(
    "app/data/Tournaments_reports.json",
    indent=4,
    separators=(",", ": "),
)
TOURNAMENTS_TABLE = DB.table("Tournaments")
USER = Query()
