import click
import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@click.group()
def cli():
    pass


@cli.command()
def init():
    sqlfile = 'ddl.sql'
    sqldb = 'techblog.sqlite'

    conn = sqlite3.connect(sqldb)

    with open(sqlfile, "r", encoding="utf-8") as script:
        rawsql = script.read().strip()
        conn.executescript(rawsql)

    click.echo("init done!")


if __name__ == "__main__":
    cli()
