Write a query that will return a list of all customers and ther invoices.
Return only rows where invoices were created by a user who never contacted
thar particular customer.
For each row, return the invoices number, customer name and the number of contacts 
that started prior to the time the invoice was created.Order the result by invoice 
number ascending.
table definitions and a data simple are give below.

Input: 
Table: customer
+----+------+------------+
| column name       | column type  | key/NULL |
+----+------+------------+
| id                | int          | PK       |
| customer_name     | varchar(255) |          |
| city_id           | int          |          |
| customer_address  | varchar(255) |          |
| contact_person    | varchar(255) | N        |
| email             | varchar(128) |          |
| phone             | varchar(128) |          |
+----+------+------------+
Table: invoice
+----+------+------------+
| column name       | column type  | key/NULL |
+----+------+------------+
| id                | int          | PK       |
| invoice_number    | varchar(255) |          |
| customer_id       | int          |          |
| user_account_id   | varchar(255) |          |
| total_price       | decimal(8,2) |          |
| time_issued       | varchar(255) | N        |
| time_due          | varchar(255) | N        |
| time_paid         | varchar(255) | N        |
| time_canceled     | varchar(255) | N        |
| time_refunded     | varchar(255) | N        |

+----+------+------------+
Table: usser_account
+----+------+------------+
| column name       | column type  | key/NULL |
+----+------+------------+
| id                | int          | PK       |
| first_name        | varchar(64)  |          |
| last_name         | varchar(64)  |          |
| user_name         | varchar(128) |          |
| password          | varchar(255) |          |
| email             | varchar(128) |          |
| phone             | varchar(128) | N        |
+----+------+------------+
Table: contact
+----+------+------------+
| column name        | column type  | key/NULL |
+----+------+------------+
| id                 | int          | PK       |
| usser_account_id   | int          | FK       |
| customer_id        | int          | FK       |
| contact_type_id    | int          |          |
| contact_outcome_id | int          | N        |
| addtional_comment  | varchar(255) | N        |
| contact_start_time | varchar(255) |          |
| contact_end_time   | varchar(255) | N        |

contact.user_account_id references user_account.id
contact.customer_id references customer.id
+----+------+------------+

The first line of the result should be:
+----+------+------------+
| invoice_number                   | customer_name | invoice_count |
+----+------+------------+
| 2a24cc2ad4440d698878a0a1a71f70fa | K-Wien        | 1             |