CREATE TABLE files (
    id INTEGER PRIMARY KEY,
    path TEXT UNIQUE
);
CREATE TABLE chunks (
    id INTEGER PRIMARY KEY,
    path TEXT,
    embedding BLOB,
    text TEXT
);
CREATE TABLE symbols (
    id INTEGER PRIMARY KEY,
    path TEXT,
    symbols TEXT
);
