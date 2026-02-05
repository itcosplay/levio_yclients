-- Создание роли из переменных окружения
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '${POSTGRES_USER}') THEN
        CREATE ROLE "${POSTGRES_USER}" LOGIN PASSWORD '${POSTGRES_PASSWORD}';
    END IF;
END
$$;

-- Создание базы данных
CREATE DATABASE "${POSTGRES_DB}" OWNER "${POSTGRES_USER}";

-- Назначение привилегий для ${POSTGRES_USER}
GRANT ALL PRIVILEGES ON DATABASE "${POSTGRES_DB}" TO "${POSTGRES_USER}";
