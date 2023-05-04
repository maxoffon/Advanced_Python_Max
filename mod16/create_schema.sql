DROP TABLE IF EXISTS actors;
CREATE TABLE actors (
act_id integer primary key autoincrement , 
act_first_name varchar(50), 
act_last_name varchar(50), 
act_gender varchar(1));

DROP TABLE IF EXISTS 'movie';
CREATE TABLE movie (
mov_id integer primary key autoincrement,
mov_title varchar(50));

DROP TABLE IF EXISTS 'director';
CREATE TABLE director (
dir_id integer primary key autoincrement,
dir_first_name varchar(50),
dir_last_name varchar(50));

DROP TABLE IF EXISTS 'movie_cast';
CREATE TABLE movie_cast (
act_id integer references actors (act_id) on delete cascade,
mov_id integer references movie (mov_id) on delete cascade,
role varchar(50));

DROP TABLE IF EXISTS 'oscar_awarded';
CREATE TABLE oscar_awarded (
award_id integer primary key autoincrement,
mov_id integer references movie (mov_id) on delete cascade);

DROP TABLE IF EXISTS 'movie_directors';
CREATE TABLE movie_directors (
dir_id integer references director (dir_id) on delete cascade,
mov_id integer references movie (mov_id) on delete cascade)
