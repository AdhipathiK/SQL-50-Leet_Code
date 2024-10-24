--Schema
Create table If Not Exists Customer (id int, name varchar(25), referee_id int)
Truncate table Customer
insert into Customer (id, name, referee_id) values ('1', 'Will', NULL)
insert into Customer (id, name, referee_id) values ('2', 'Jane', NULL)
insert into Customer (id, name, referee_id) values ('3', 'Alex', '2')
insert into Customer (id, name, referee_id) values ('4', 'Bill', NULL)
insert into Customer (id, name, referee_id) values ('5', 'Zack', '1')
insert into Customer (id, name, referee_id) values ('6', 'Mark', '2')

--Solution 1
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL

--Solution 2
SELECT name
FROM Customer
WHERE IFNULL(referee_id,-1) <>2

--Solution 3
SELECT name
FROM Customer
WHERE COALESCE(referee_id,-1) <>2
