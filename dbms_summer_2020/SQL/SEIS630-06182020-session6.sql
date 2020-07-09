-- The CASE statement
-- SYNTAX
-- CASE
-- WHEN CONDITION_1 THEN ACTION_1
-- WHEN CONDITION_2 THEN ACTION_2
-- [ELSE ...]
-- END

-- If the customer has a loan with an amount more than $20000, the account balance will be $500.
-- If the customer has a loan with an amount more than $30000, the account balance will be $750.
insert into account (bname, cname, A#, bal)
select bname, cname, L#, 
CASE
     when amt < 30000 then 500
	 else 750
END as bal
from loan
where amt>=20000
;

-- update command
-- set all Rahimi's loan amt to zero
update loan
set amt=0
where upper(cname)='RAHIMI';

-- add interest to accounts
update account
set bal=bal*1.01
where bal>10000;

-- You can also set values more than one column. 
update customer
set ccity='MPLS',street='Main'
;

-- the customer account gets 10% increase if a customer has a loan >=20000
update account
set bal=bal*1.1
where cname IN (
      select cname 
	  from loan
	  where amt>=20000)
;

-- aggregate functions example
-- show the average account bal in each branch
select bname, avg(bal)
from account
group by bname;

select bname 
from account
order by bname;

-- having condition
select bname, avg(bal)
from account
group by bname
having avg(bal)>1000
order by bname DESC;

-- show the customer names, the avg bal, and number of accounts of all accounts of that customer
select cname, avg(bal), count(bal)
from account
group by cname;

-- pattern matching - using LIKE and % or _
select bname, avg(bal), count(*)
from account
where lower(cname) LIKE '%o%'
group by bname
having avg(bal) > 100
order by bname DESC
;

-- Find all Customers who have an account at ALL Branches in Edina
select a.cname
from account a
where a.bname IN (
		select bname
		from branch
		where lower(bcity)='edina'
	)
group by a.cname
having count(distinct a.bname)=(
		select count(bname)
		from branch
		where lower(bcity)='edina'
		)
;

-- 
create view customerBasicReadOnly (name, city)
as
select cname, ccity
from customer
with READ ONLY
;




