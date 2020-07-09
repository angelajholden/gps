-- Find all Customers who have a loan and an account at France Branch
-- use intersect
select cname
from account
where lower(bname)='france'
intersect
select cname
from loan
where lower(bname)='france';

-- use IN construct
select cname
from account
where lower(bname)='france' AND
      cname IN 
	  (
		select cname
		from loan
		where lower(bname)='france'
	  )
;

-- table alias
select a.cname as NAME
from account a;


--Performance discussion: JOIN vs IN
Assume 2000 accounts, 500 loan, and 50 branches.  Assume uniform distribution, we get 10 loans per branch. 
JOIN: 2000 account*500 loan = 1,000,000
IN: (inner select 500) + 10 selected loan * 2000 account = 20000+500
Thus, IN is faster in this case.


--- Find the name of all customers who have a loan and an account in branches in Minnetonka using the IN construct
--- We need loan, account, branch tables
--- Set A: Find the name of all customers who have a loan in branches in Minnetonka
--- Set B: Find the name of all customers who have a account in branches in Minnetonka
select cname
from loan, branch
where lower(bcity)='minnetonka' AND
      loan.bname=branch.bname AND
	  cname IN (
		select cname
		from account, branch
		where lower(bcity)='minnetonka' AND
		account.bname=branch.bname
	  )
;

-- Find the name of all customers who have a loan and an account in the SAME branch in Minnetonka using the IN construct
select cname
from loan, branch
where lower(bcity)='minnetonka' AND
      loan.bname=branch.bname AND
	  cname IN (
		select cname
		from account, branch
		where lower(bcity)='minnetonka' AND
		account.bname=branch.bname AND
	    loan.bname=account.bname
	  )
;

-- Simplified statement
select cname
from loan, branch
where lower(bcity)='minnetonka' AND
      loan.bname=branch.bname AND
	  cname IN (
		select cname
		from account
		where loan.bname=account.bname
	  )
;
