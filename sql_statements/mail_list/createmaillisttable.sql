CREATE TABLE IF NOT EXISTS mail_list (
	sub_id INT AUTO_INCREMENT,
	email VARCHAR(255),
	is_activated BOOLEAN NOT NULL default 0,
	email_hash VARCHAR(255),
	PRIMARY KEY (sub_id),
	UNIQUE(email)
)
