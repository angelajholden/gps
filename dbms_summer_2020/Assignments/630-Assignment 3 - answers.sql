-- capture the results into a text file to print later
--
spool Assignment3-results.txt

-- setup the width and height of the page to print
--
set linesize 80;
set pagesize 64;


-- Set echo on so that you can see the input as well in the spool file
set echo on;

--
-- Name: Ron Chiang
-- SEIS 630 Assignment 3 
--
--
-- reduce the widths of column being printed
--column cname format A10;
--column bname format A15;


-- Q1: For the bank database given in class, write a SQL command that prints the names of all customers whose accounts and loans in Edina are in different branches (in other words, the customers we want are the ones whose set of account branches and loan branches in Edina DO NOT intersect. For example, Jones who has an account in France and a loan also in France, is NOT one of the answers).
----customers who have accounts in Edina branches
select a1.cname
from account a1, branch b
where a1.bname=b.bname AND
      lower(b.bcity)='edina' AND
	  NOT EXISTS
	  (--The results of intersect
		--branches of the customer's loans in Edina	  
		select l.bname
		from loan l, branch BL
		where l.bname = BL.bname 
		   AND lower(BL.bcity)='edina' 
		   AND l.cname=a1.cname
		intersect 
		--branches of the customer's accounts in Edina
		select a2.bname
		from account a2, branch ba
		where a2.bname=ba.bname
			AND lower(ba.bcity)='edina'
			AND a1.cname=a2.cname			
	  )
--If you want to exclude customers who don't have loans in Edina branches  
	  AND EXISTS
	  ( --This condition is to ensure the customer has at least one loan in the Edina branches.
	  	select l2.bname
		from loan l2, branch b3
		where l2.bname = b3.bname 
			AND lower(b3.bcity)='edina' 
			AND l2.cname=a1.cname
	  );

-- Q2: For the bank database given in class, write a SQL statement that prints the name of all cities when there is at least one customer who has an account in every one of the city’s branches.
SELECT DISTINCT BCITY 
FROM BRANCH B
WHERE EXISTS 
	(
		SELECT CNAME 
		FROM ACCOUNT A
		WHERE NOT EXISTS
			(
				SELECT BNAME 
				FROM BRANCH B1
				WHERE B1.BCITY=B.BCITY
				AND BNAME NOT IN 
				(
					SELECT BNAME 
					FROM ACCOUNT A1
					WHERE A1.CNAME=A.CNAME
				)
			)
	);

-- Q3: Write one SQL statement to find the name of all customers who have a loan and an account in the same branch in Minnetonka
select cname
from Loan, Branch
where lower(bcity) = 'minnetonka'  AND
loan.bname = branch.bname AND
Cname  IN 
	(select cname
	from Account
	where account.bname = loan.bname);


-- Close the spool file
spool off;

