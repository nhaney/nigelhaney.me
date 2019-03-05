CREATE TABLE IF NOT EXISTS blog_posts (
	post_id INT AUTO_INCREMENT,
	unique_url VARCHAR(255) NOT NULL,
	post_title VARCHAR(255) NOT NULL,
	excerpt VARCHAR(255),
	content TEXT,
	status INT,
	type INT,
	comment_count BIGINT DEFAULT 0,
	like_count BIGINT DEFAULT 0,
	published_time DATETIME DEFAULT CURRENT_TIMESTAMP,
	last_edited DATETIME,
	PRIMARY KEY (post_id),
	UNIQUE (post_title, unique_url)
);