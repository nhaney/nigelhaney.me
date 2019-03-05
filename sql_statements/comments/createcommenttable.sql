CREATE TABLE IF NOT EXISTS comments (
	comment_id INT AUTO_INCREMENT,
	post_id INT NOT NULL,
	author VARCHAR(255) NOT NULL,
	published_time DATETIME DEFAULT CURRENT_TIMESTAMP,
	last_edited DATETIME,
	like_count INT,
	status INT,
	type INT,
	content VARCHAR(10000),
	PRIMARY KEY (comment_id),
	FOREIGN KEY (post_id) 
		REFERENCES blog_posts(post_id)	
		ON DELETE CASCADE
);