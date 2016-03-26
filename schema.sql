drop table if exists devices;
create table devices (
  id integer primary key autoincrement,
  name text not null,
  meta text null
);

drop table if exists services;
create table services (
  id integer primary key autoincrement,
  description text not null,
  command text not null
);