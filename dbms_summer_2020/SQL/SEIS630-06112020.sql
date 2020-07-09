-- Inner join example
select customer.cname, ccity, bname
from loan, customer
where loan.cname=customer.cname
AND lower(loan.bname)='france';

-- Print all Customer names who live in MPLS and have account(s) in branches 
-- that have more than 90,000 in assets and are located in the city Minnetonka. 
select distinct customer.cname
from account, customer, branch
where account.cname = customer.cname AND
      account.bname = branch.bname AND
	  upper(ccity)= 'MPLS' AND
	  assets > 90000 AND
	  lower(bcity)= 'minnetonka';
	  
-- Example: left outer join
select distinct account.cname, loan.cname
from account left outer join loan
on account.cname = loan.cname;

-- Example: right outer join
select distinct account.cname, loan.cname
from account right outer join loan
on account.cname = loan.cname;

-- Example: full outer join
select distinct account.cname, loan.cname
from account full outer join loan
on account.cname = loan.cname;

-- inner join syntax
select distinct account.cname, loan.cname
from account, loan
where account.cname=loan.cname;

select distinct account.cname, loan.cname
from account join loan
on account.cname=loan.cname;

-- If a customer has account in the bank, print the name of the customer and the branch name for their account. 
-- If a customers does not have an account in the bank, then just print the name of the customer.
select customer.cname, account.bname
from customer left outer join account
on customer.cname = account.cname;


-- Repeat the previous question only for those customers who live in MPLS.
select customer.cname, account.bname
from customer left outer join account
on customer.cname = account.cname
where upper(ccity)='MPLS'
order by customer.cname;


-- Create view example
create view loan_account
AS
select loan.cname, loan.l#, account.a#
from loan,account
where loan.cname=account.cname;

-- column information, index, and constraints
select table_name, index_name, column_name
from all_ind_columns
where lower(table_name)='account';

-- column information from tables
select table_name, column_name, data_type
from all_tab_columns
where lower(owner)='seisdbms';
