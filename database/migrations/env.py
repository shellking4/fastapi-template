from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from app.core import settings
from app.helper.functions.utilities import combine_metadata
from app.user.models import user_model


config = context.config
fileConfig(config.config_file_name)

target_metadata = combine_metadata(user_model.BaseModel.metadata, )

def run_migrations_offline():
    url = settings.SQLALCHEMY_DATABASE_URI
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True,
                      dialect_opts={"paramstyle": "named"}, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = settings.SQLALCHEMY_DATABASE_URI
    connectable = engine_from_config(configuration, prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
