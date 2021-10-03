from tinydb import TinyDB, Query


""" Base de données des tournois """
DB = TinyDB(
    "../data/Tournaments_reports.json",
    indent=4,
    separators=(",", ": "),
)
TOURNAMENTS_TABLE = DB.table("Tournaments")
USER = Query()
