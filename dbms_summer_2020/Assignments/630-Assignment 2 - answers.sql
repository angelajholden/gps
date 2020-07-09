-- capture the results into a text file to print later
--
spool Assignment2-results.txt

-- setup the width and height of the page to print
--
set linesize 40;
set pagesize 64;


-- Set echo on so that you can see the input as well in the spool file
set echo on;

--
-- Name: Ron Chiang
-- SEIS 630 Assignment 2 
--
--
-- reduce the widths of column being printed
--column cname format A10;
--column bname format A15;


-- Q1: Assume that we build a database based on the solution to assignment1, question 2. Write a SQL statement that prints the balance of accounts and their customer names if the account balance is more than $10,000.
select bal, name 
from Account, Person
where Account.SSN=Person.SSN AND
      Account.bal>10000;

--
-- Q2: For the bank database given in class, write a SQL statement to print the customer names and the branch names for all branches in where the customer has an account, a loan or both. Don’t print the branch name but still print the customer name if the customer does not have a loan or account in the bank.
Select distinct c.cname, b.bname
from customer c
left outer join (
(select cname, bname from account) 
union
(select cname, bname from loan)) b
on c.cname=b.cname
;

select cname, bname from account 
UNION
select cname, bname from loan 
UNION 
select cname, ' ' as bname from customer 
where cname not in 
(select cname from loan union select cname from account);


-- Q3: For the bank database given in class, write a SQL statement that prints the name of all cities when there is at least one customer who has an account in one of the city’s branches and that branch has more than $500,000 in assets.
select distinct BCITY from account, branch
where account.bname=branch.bname
AND   branch.assets>=500000;

-- Close the spool file
spool off;

