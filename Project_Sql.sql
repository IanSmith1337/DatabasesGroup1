CREATE TABLE IF NOT EXISTS EMPLOYEE
(
    Empid int IDENTITY(1,1) PRIMARY KEY,
    Fname VARCHAR(10) NOT NULL,
    Lname VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS CUSTOMER
(
    Custid int IDENTITY(1,1) PRIMARY KEY,
    CustName VARCHAR(10) NOT NULL,
    Address VARCHAR(20),
	City Varchar(20),
	State Varchar(20),
	ZipCode char(5),
	Phone varchar(10)
);

 create table IF NOT EXISTS items
 (
 itemid int IDENTITY(1,1) PRIMARY KEY,
 itemprice float,
 itemname varchar(20)
 );

 create table IF NOT EXISTS delivery
 (
 deliveryid int IDENTITY(1,1) PRIMARY KEY,
 deliveryfee float,
 Deliverytype varchar(20),
 Empid int,
 FOREIGN KEY (Empid) REFERENCES EMPLOYEE(Empid)
 );

Create table IF NOT EXISTS ORDER1
(
orderid int IDENTITY(1,1) PRIMARY KEY,
amount float,
deliveryfee float,
tax float as (0.07 * amount),
Total_amount float as ( (0.07 * amount) + amount + deliveryfee),
deliveryid int,
Custid int,
FOREIGN KEY (deliveryid) REFERENCES Delivery(deliveryid),
FOREIGN KEY (Custid) REFERENCES Customer(Custid)
);

Create table IF NOT EXISTS ORDERDETAILS
(
 orderdetailid int IDENTITY(1,1) PRIMARY KEY,
 ordertype varchar(20) NOT NULL,
 amount float,
 quantity int,
 orderdate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 Custid int,
 Empid int,
  orderid int,
  itemid int,
  FOREIGN KEY (Custid) REFERENCES Customer(Custid),
  FOREIGN KEY (Empid) REFERENCES Employee(Empid),
  FOREIGN KEY (orderid) REFERENCES Order1(orderid),
  FOREIGN KEY (itemid) REFERENCES items(itemid)
 );

Create table IF NOT EXISTS hotspot
(
Zipcode char(5),
hotspotfee float,
address varchar(20),
deliveryid int,
primary key (Zipcode),
FOREIGN KEY (deliveryid) REFERENCES delivery(deliveryid)
);
