-- question 1
-- print balance of accounts and their customer names
-- if the account balance is more than $10,000
--
select account.bal, person.name
from account, person
where account.ssn = person.ssn AND
	bal.account > 10000;

-- print the customer names and the branch names for all branches (cname, bname)
-- in where the customer has an account, a loan or both (union)
-- Don't print the branch name, but still print the customer name if the customer does not have a loan or account in the bank.
--
select customer.cname, account.bname
from customer left outer join account
on customer.cname = account.cname
union
select customer.cname, loan.bname
from customer left outer join loan
on customer.cname = loan.cname;

-- print the name of all cities
-- when there's at least one customer with an acct in one of the city's branches
-- and when that branch has more than $500,000 in assets
--
select distinct bcity
from account, branch
where account.bname = branch.bname AND
	branch.assets > 500000;

select bname, bcity, assets
from branch
where assets > 500000;

select bname, bcity, assets
from branch;

select bname, bcity, assets
from branch
intersect
select cname, bname
from account;