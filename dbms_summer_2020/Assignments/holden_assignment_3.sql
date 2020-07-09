-- print names of all customers whose accounts and loans in Edina are in different branches
-- customers we want whose account branches and loans branches do not intersect
--
select cname, bcity, branch.bname
from loan, branch
where lower(bcity) = 'edina' AND
	loan.bname=branch.bname AND
	cname NOT IN 
	(
		select cname
		from account, branch
		where lower(bcity) = 'edina' AND
			account.bname=branch.bname
	)
;

-- prints the name of all cities
-- when there is at least one customer who has an account in every one of the city's branches

-- I RAN OUT OF TIME TO COMPLETE THE ASSIGNMENT