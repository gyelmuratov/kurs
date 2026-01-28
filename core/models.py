

users = """CREATE TABLE IF NOT EXISTS users
(
    id              BIGSERIAL PRIMARY KEY,
    telegram_id     BIGINT UNIQUE,
    first_name      VARCHAR(50),
    last_name       VARCHAR(50),
    phone_number    VARCHAR(50),
    age             SMALLINT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at      TIMESTAMP NULL
    );
    """


courses = """CREATE TABLE IF NOT EXISTS courses
(
    course_id           BIGSERIAL PRIMARY KEY,
    course_name         VARCHAR(50) UNIQUE,
    course_description  TEXT,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at          TIMESTAMP NULL
    );
"""

registrations = """CREATE TABLE IF NOT EXISTS registrations
(
    registration_id    BIGSERIAL PRIMARY KEY,
    course_id          BIGINT REFERENCES courses(course_id) ON DELETE SET NULL,
    user_id            BIGINT REFERENCES users(telegram_id) ON DELETE SET NULL,
    created_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""