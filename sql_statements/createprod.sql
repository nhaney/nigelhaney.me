CREATE DATABASE prod_portfoliosite;

USE prod_portfoliosite;

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

CREATE TABLE IF NOT EXISTS fish_leaderboard (
	score_id INT AUTO_INCREMENT,
	score INT NOT NULL,
	name VARCHAR(25),
	PRIMARY KEY (score_id)
);

CREATE TABLE IF NOT EXISTS mail_list (
	sub_id INT AUTO_INCREMENT,
	email VARCHAR(255),
	is_activated BOOLEAN NOT NULL default 0,
	email_hash VARCHAR(255),
	PRIMARY KEY (sub_id),
	UNIQUE(email)
)
