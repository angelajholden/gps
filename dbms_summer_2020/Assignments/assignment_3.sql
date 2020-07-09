-- For the bank database given in class, write a SQL command that prints the names of all customers whose accounts and loans in Edina are in different branches (in other words, the customers we want are the ones whose set of account branches and loan branches in Edina DO NOT intersect. For example, Jones who has an account in France and a loan also in France, is NOT one of the answers).
--
select cname, branch.bname, branch.bcity
from account, branch
where lower(bcity)='edina' AND
	cname NOT IN 
  (
	select cname
	from loan, branch
	where lower(bcity)='edina'
  )
union
select cname, branch.bname, branch.bcity
from loan, branch
where lower(bcity)='edina' AND
	cname NOT IN 
  (
	select cname
	from account, branch
	where lower(bcity)='edina'
  )
;

-- For the bank database given in class, write a SQL statement that prints the name of all cities when there is at least one customer who has an account in every one of the city’s branches.
--
-- I got the same result as the answer you provided (Edina and Minnetonka), but I'm not sure it's the correct solution.
select branch.bcity, branch.bname
from branch, account
where account.bname = branch.bname AND
	cname IN (
			select cname
			from branch, loan
			where loan.bname = branch.bname
			AND loan.bname = account.bname
		)
;

-- Write one SQL statement to find the name of all customers who have a loan and an account in the same branch in Minnetonka
--
select cname
from loan, branch
where lower(bcity) = 'minnetonka'
AND loan.bname = branch.bname
intersect
select cname
from account, branch
where lower(bcity) = 'minnetonka'
AND account.bname = branch.bname
;
