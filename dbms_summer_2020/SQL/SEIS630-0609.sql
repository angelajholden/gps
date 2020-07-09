-- Print the name of all Customer with an account(s) at France branch
select cname
from account
where lower(bname)='france';

-- Print the name of all Customer with a loan(s) at France branch
select cname
from loan
where lower(bname)='france'
order by cname desc;

-- Print all Customer names with a loan, an account or both at France
-- set a: customers have accounts
-- set b: customers have loans
-- a union b
select cname, bname
from account
where lower(bname)='france'
union
select cname, bname
from loan
where lower(bname)='france';

-- Print all Customer names with a loan AND an account at France
select cname, bname
from account
where lower(bname)='france'
intersect
select cname, bname
from loan
where lower(bname)='france';

-- Print all Customer names with an account at France but not a loan at France
select cname, bname
from account
where lower(bname)='france'
minus
select cname, bname
from loan
where lower(bname)='france';

-- Print the name of customers who have an account or a loan, or both in France branch 
-- except for those customers who have an account with bal of less than $800.
-- set a: customers have accounts at France branch
-- set b: customers have loans at France branch
-- set c: customers who have an account with bal<800 in ANY branch
select cname
from account
where lower(bname)='france'
union
select cname
from loan
where lower(bname)='france'
minus
select cname
from account
where bal<800;

-- Print the name of customers who have an account or a loan, or both in France branch 
-- except for those customers who have an account with bal of less than $800 in France Branch.
-- set a: customers have accounts at France branch
-- set b: customers have loans at France branch
-- set c: customers who have an account with bal<800 in France branch
select cname
from account
where lower(bname)='france'
union
select cname
from loan
where lower(bname)='france'
minus
select cname
from account
where bal<800 and lower(bname)='france';

-- If you do this, the union operation may bring back customers who doesn't have accounts>=800 at the France branch. 
select cname
from account
where bal>=800 and lower(bname)='france'
union
select cname
from loan
where lower(bname)='france';


