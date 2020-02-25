DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS articles_to_tags;

CREATE TABLE articles (
  article_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title CHAR(255) NOT NULL,
  preview TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at DATETIME NOT NULL
);

CREATE TABLE tags (
  tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
  tag_name CHAR(30) NOT NULL
);

CREATE TABLE articles_to_tags(
  article_id INTEGER,
  tag_id INTEGER,
  FOREIGN KEY (article_id) REFERENCES articles (article_id),
  FOREIGN KEY (tag_id) REFERENCES tags (tag_id)
);

INSERT INTO tags (tag_name) VALUES ('Javascript'), ('VueJS'), ('Python'), ('Flask');

INSERT INTO articles (title, preview, content, created_at) VALUES
('測試1', '測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽', '測試內容', '2020/02/20 20:18:53'),
('測試2', '測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽', '測試內容', '2020/02/22 20:18:53'),
('測試3', '測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽', '測試內容', '2020/02/24 20:18:53'),
('測試4', '測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽測試預覽', '測試內容', '2020/02/26 20:18:53');

INSERT INTO articles_to_tags VALUES 
(1,1), (1,2), 
(2,3), (2,4),
(3,2), (3,3),
(4,1), (4,4);

