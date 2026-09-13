create database bk;

create table users (
    id serial unique primary key,
    name varchar(50) not null,
    age int default 18,
    email varchar(100) unique,
    metadata json
);

insert into users(name, email)
values
      ('zzz', 'zzz@mail.com');

update users set metadata = '{ "name": "xyz" }' where id = 2;

alter table users add column department varchar(50);
alter table users add constraint dept_unique unique (department);
alter table users add constraint min_age check (age >= 18);

select * from users;
select name, users.department from public.users;
select name from users where age > 20;
select name, department from users order by name desc limit 2;
select avg(age) from users;
select count(*) as total from users where age >= 19;

delete from users where id = 2; -- DELETE ROW
drop database bk; -- DELETE DATABASE
drop table users; -- DELETE TABLE


2nd class

create table posts (
    id serial unique primary key,
    title varchar(50) not null
--  user_id int references users(id)
);

alter table posts add column user_id int, add constraint user_posts foreign key (user_id) references users(id);

-- SELECT u.name, p.title from users u LEFT JOIN posts p ON u.id = p.user_id WHERE p.user_id NOTNULL;

select users.name, count(posts.user_id) as post_count from users left join posts on users.id = posts.user_id where posts.user_id notnull
group by users.name;
