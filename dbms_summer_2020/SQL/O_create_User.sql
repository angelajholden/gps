-- This command runs SQLPLUS using the currently logged in NT user
-- This file assumes that you have already connected to Oracle using SYSTEM/Password on
-- your laptop or SU/SuperUser_S1 if you are using machines in OSS333
-- 
-- Create the user
-- Edit XYZ to indicate your initials and choose a PASSWORD for this user. Needs to be 
-- at least 8 places. Do not include $ and/or @ symbols

-- The following line is needed if the DBMS is not Oracle XE 11g. (12 or later)
alter session set "_ORACLE_SCRIPT"=true;

create user seisdbms profile default
identified by seisdbmspassword
default tablespace users
temporary tablespace temp
quota unlimited on users
account unlock;

commit;

-- Grant this user DBA to the database
--

GRANT connect, resource to seisdbms;
GRANT create view to seisdbms;

-- Log in
--
sqlplus system/oracle@//localhost:1521/xe

-- Clear
--
clear screen;

-- check oracle version
--
SELECT * FROM v$version;

-- Exam 1, question 11
--
/*==================================================*/
/* Table: EMP                                     	*/
/*==================================================*/
create table EMP 
(
   SSN                  CHAR(11)            not null,
   EID                	NUMBER(5)           not null,
   NAME                	VARCHAR(15),
   SEX                  CHAR(1),
   constraint PK_EID primary key (EID),
   constraint UNIQUE_SSN unique (SSN)
);

-- Exam 1, question 12
--
EMPLOYEE(SSN, Sup_SSN, Dept_Number, Fname, Lname, Minit, Sex, Address, Birthdate)
SSN is the primary key

DEPENDANT(SSN, Dep_SSN, Name, Sex, Birthdate, Relationship)
SSN is the primary key

DEPARTMENT(Dep_Number, Mgr_SSN, Name, Location)
Dep_Number is the primary key

PROJECT(Prj_Number, Dep_Number, Name, Location)
Prj_Number is the primary key

PROJECTEMP(Emp_SSN, Prj_Number)
Emp_SSN and Prj_Number are the primary key

-- Exam 1, question 13
--
DEPARTMENT(D#, Mgr_SSN)
	D# is the primary key
EMPLOYEE(SSN, Name, Super_SSN, D#)
	SSN is the primary key
HOURLY(SSN, Rate)
	SSN is the primary key
SALARIED(SSN, Salary)
	SSN is the primary key

-- Exam 1, question 14
-- For the company, we maintain the company name as Primary key (Pkey) and its address.
-- Employees and their dependents are Persons.
-- For Person, we maintain SSN as the Pkey, Name as a three-component attribute with Fname, MI, and Lname, DOB, and address.
-- Employees have properties of EID as Candidate Key (CKey), hireDate, and sex.
-- For dependents, we maintain Age as a Derived attribute from DOB.
-- For Departments, we maintain DID (Pkey), Dname (Ckey), and Budget.
--
COMPANY(Name, Address)
Name is the Pkey

EMPLOYEE(SSN, Fname, Lname, Minit, DOB, Address, EID, HireDate, Sex)
SSN is the Pkey

DEPENDANT(DOB, Age)

DEPARTMENTS(DID, Dname, Budget, Mgr_Start_Date)
DID is Pkey

EXEMPT(SSN, Hours, Rate)
NONEXEMPT(SSN, Salary)



Marital_Status
Marital_Emp
Dep_SSN
Sup_SSN
Mgr_SSN
