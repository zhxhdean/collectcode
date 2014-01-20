create database blogsdb;

create table blogs(
id int(4) primary key auto_increment,
title nvarchar(100) not null,
url varchar(50) not null,
note text not null,
tags nvarchar(50) ,
last_time datetime,
views int(4) default 0,
comments int(4)default 0,
top tinyint(1)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table comments(
id int(4)primary key auto_increment,
email varchar(50) not null,
comment nvarchar(500) not null,
last_time datetime,
blog_id int(4) not null
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table tags(
id int(4)primary key auto_increment,
tag varchar(20) not null,
last_time datetime,
blog_num int(4) default 0,
url varchar(50) not null
)ENGINE=InnoDB DEFAULT CHARSET =utf8;

create table blogs_tags(
id int(4)primary key auto_increment,
blogs_id int(4) not null,
tags_id int(4) not null
)ENGINE=InnoDB DEFAULT CHARSET =utf8;

create table user(
id int(4)primary key auto_increment,
name varchar(20)unique not null,
passwd varchar(32) not null
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
