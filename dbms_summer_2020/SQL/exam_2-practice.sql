-- Based on the tables below, which of the following commands in SQL would return 
-- only the name of the sales representative 
-- and the name of the customer 
-- for each customer that has a balance greater than 400?
--
-- select RepName, CustName
-- from SALESREP, CUSTOMER
-- where CUSTOMER.Balance > 400;


-- SELECT * 
-- FROM SALESREP, CUSTOMER 
-- WHERE SALESREP.SalesRepNo = CUSTOMER.SalesRepNo 
-- AND Balance > 400;

-- SELECT DISTINCT RepName, CustName 
-- FROM SALESREP, CUSTOMER 
-- WHERE Balance > 400;

-- SELECT * 
-- FROM SALESREP, CUSTOMER 
-- WHERE Balance > 400;

SELECT RepName, CustName 
FROM SALESREP, CUSTOMER 
WHERE SALESREP.SalesRepNo = CUSTOMER.SalesRepNo 
AND Balance > 400;

-- Write a SQL statement that prints the name of all cities when there is at least one customer who has an account in every one of the city’s branches.
--
select distinct bcity 
from branch b
where EXISTS 
(
	select cname 
	from account a
	where NOT EXISTS
	(
		select bname 
		from branch b1
		where b1.bcity=b.bcity
		and bname NOT IN 
		(
			select bname 
			from account a1
			where a1.cname=a.cname
		)
	)
)
;

-- Write a SQL statement that prints a customer name, 
-- if this customer lives in a city that has 'M' or 'm' as the first letter in its name. 
-- Also, for each qualified customer, prints the average balance 
-- and the number of accounts of the customer if the average balance of this customer is over $2,000.
--
-- pattern matching - using LIKE and % or _
--
select customer.cname, avg(bal), count(*)
from customer, account
where lower(customer.ccity) LIKE 'm%'
AND customer.cname = account.cname
group by customer.cname
having avg(bal) > 2000
;

-- without bal > 2000
select customer.cname, avg(bal), count(*)
from customer, account
where lower(customer.ccity) LIKE 'm%'
AND customer.cname = account.cname
group by customer.cname;

-- Write one SQL statement to find the name of all customers who have a loan and an account in the same branch in Minnetonka
--
select cname
from loan, branch
where lower(bcity) = 'minnetonka'
AND loan.bname = branch.bname
AND cname IN 
	(
	select cname
	from account
	where account.bname = loan.bname
	)
;

-- Write one SQL statement to 
-- find the customer names and branch names 
-- of all customers who do have an account(s) 
-- but not a loan in the bank, 
-- then...
-- and those customers who do have a loan(s) but not an account in the bank.
--
select cname, bname
from account
where 
(
	select count(*)
	from loan
	where account.cname = loan.cname
) = 0
union
select cname, bname
from loan
where 
(
	select count(*)
	from account
	where account.cname = loan.cname
) = 0
;
