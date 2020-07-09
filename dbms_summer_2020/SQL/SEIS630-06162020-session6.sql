-- Insert a new account for Rahimi with account number of 1111, at York branch, and the balance of 5000
insert into account values (1111111,'Rahimi','York', 5000.00);

-- Insert multiple records 
insert into Account (bname, A#, cname, bal)
	select bname, L#, cname, amt
	from Loan;

rollback;

-- Create an account with the balance of 500 for all customers who have a loan with an amount $20000 or more in the bank.
insert into account (bname, cname, A#, bal)
select bname, cname, L#, 
CASE
	when amt < 30000 then 500
	else 750
END as bal
from loan
where amt>= 20000
;

rollback;

-- update command
-- set all Rahimi's loan amt to zero
update loan
	set amt = 0
	where upper(cname) = 'RAHIMI';

-- add interest to accounts
update account
	set bal = bal*1.01
	where bal >= 10000;

-- You can also set values more than one column
update customer
	set ccity = 'MPLS', street='Main';

-- the customer account gets 10% increase if a customer has a loan >= 20000
update account
set bal = bal*1.1
where cname IN (
		select cname
		from loan
		where amt >= 20000
	)
;

-- aggregate functions example
-- show the average account balance in each branch
select bname, avg(bal)
from account
group by bname;

select bname, bal --> doesn't work
from account
group by bname;

select bname
from account
order by bname;

-- having condition
-- where does not work, need to use having
select bname, avg(bal)
from account
group by bname
having avg(bal)>1000
order by bname DESC;

-- show the customer names and the ave bal, and the number of accounts of all account of that customer
select cname, avg(bal), count(*)
from account
group by cname;

-- pattern matching - using LIKE and % or _
-- change headings
select bname, avg(bal) as BALANCE, count(*) --> as BALANCE changes heading
from account
where lower(cname) LIKE '%o%'
group by bname
having avg(bal) > 100
order by bname DESC
;

select bname, avg(bal), count(*)
from account
where lower(cname) LIKE '%o%'
group by bname
having avg(bal) > 100
order by bname DESC
;

-- change format
column avg(bal) heading Average;
column avg(bal) format 99999.99;
column bname format A20;

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
