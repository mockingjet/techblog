import sqlalchemy

engine = sqlalchemy.create_engine(
    'sqlite3:///techblog.db'
    poolclass=sqlalchemy.pool.QueuePool,
    max_overflow=1,
    pool_size=2,
    pool_timeout=2
)
