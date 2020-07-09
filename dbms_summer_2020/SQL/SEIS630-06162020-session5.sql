-- Find all Customers who have a loan at France Branch but NOT an account there.
--- Use NOT IN to answer
select cname
from Loan
where lower(bname) = 'france'  AND
	cname NOT IN 
	(
		select cname
		from Account
		where lower(bname) = 'france'
	)
;

--- USE minus to answer
select cname
from Loan
where lower(bname) = 'france'
minus
select cname
from Account
where lower(bname) = 'france'
;

-- Find the name of all Customers who have an account at a Branch at which Jones has an account
-- Use IN construct to answer
select cname, bname
from account 
where lower(cname) != 'jones' AND
bname IN
(
	select bname
	from account
    where lower(cname)='jones'
)
;

-- Us table aliases
select T.cname
from Account s, Account T
where lower(s.cname) = 'jones' AND 
      s.bname = T.bname AND 
      lower(T.cname) != 'jones';

-- Print the balance and the  branch name of all accounts of a customer 
-- if the customer has an account with a balance of equal to or more than 1000.
-- First, use Account S to find out who has accounts with a bal >= 1000
-- Then, use Account T to find out those customer's accounts and bal. 
select S.A#, T.A#, T.bname, T.bal
from Account S, Account T
where S.bal >= 1000 AND
      S.cname = T.cname
order by S.A#
;

-- Show all accounts with a bal over 1000
select bname, bal
from account
where bal >= 1000;


-- Find all Branches that have assets greater than assets at all Branches in Edina
select bname
from Branch
where  assets > all
(
	select assets
	from Branch
	where lower(bcity) = 'edina'
);

-- Find all Customers who have an account at ALL Branches in Edina
-- 1. List of branches in Edina
select distinct a1.cname
from account a1
where 
	NOT EXISTS(
		select bname
		from branch
		where lower(bcity)='edina' AND
		bname NOT IN (
			select bname
			from account a2
			where a2.cname=a1.cname
		)
	)
;



