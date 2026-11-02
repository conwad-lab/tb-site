-- & Beyond subscriber list (story 017). One row per address; nothing else about the person is stored
-- (no IP address, no name, no opens or clicks).
CREATE TABLE IF NOT EXISTS subscribers (
  email           TEXT PRIMARY KEY,                                  -- lower-cased
  status          TEXT NOT NULL CHECK (status IN ('pending', 'confirmed')),
  consent         TEXT NOT NULL,                                     -- version of the privacy text agreed to
  created_at      TEXT NOT NULL,                                     -- ISO 8601 UTC
  confirm_sent_at TEXT NOT NULL,
  confirmed_at    TEXT
);
CREATE INDEX IF NOT EXISTS subscribers_status ON subscribers (status, created_at);

-- One row per confirmation mail sent, for the hourly cap. Holds no personal data; purged after a day.
CREATE TABLE IF NOT EXISTS sends (
  at TEXT NOT NULL                                                  -- ISO 8601 UTC
);
CREATE INDEX IF NOT EXISTS sends_at ON sends (at);
