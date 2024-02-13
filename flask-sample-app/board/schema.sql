DROP TABLE IF EXISTS post;  -- For the sake of the tutorial
-- Obviously don't always drop the table in the real world

CREATE TABLE IF NOT EXISTS post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  author TEXT NOT NULL,
  message TEXT NOT NULL
);
