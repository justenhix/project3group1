drop table raleigh

create table raleigh (
ID serial primary key,
year varchar not null,
month varchar not null,
value varchar not null,
rate varchar not null

);

select * from raleigh

drop table greensboro
create table greensboro (
ID serial primary key,
year varchar not null,
month varchar not null,
value varchar not null,
rate varchar not null

);

select * from greensboro

drop table winston
create table winston (
ID serial primary key,
year varchar not null,
month varchar not null,
value varchar not null,
rate varchar not null
);

select * from winston

drop table charlotte
create table charlotte (
ID serial primary key,
year varchar not null,
month varchar not null,
value varchar not null,
rate varchar not null

);

select * from charlotte

drop table year_month
create table year_month(
ID serial primary key,
year varchar not null,
month varchar not null,
value varchar not null,
rate varchar not null,
city varchar (30) not null


);
select * from year_month
