create database IF NOT EXISTS flog_db;

use flog_db;

create table users(user_id int auto_increment, first_name varchar(30), last_name varchar(30), username varchar(30) unique, email varchar(40) unique, password varchar(200), primary key(user_id));

create table blog(blog_id int auto_increment, title varchar(100), author varchar(40), body varchar(16000), primary key(blog_id));