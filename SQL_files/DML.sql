-- Jake Hathaway and Kevin Kraatz
-- Project Group 50
-- User input in all queries is denoted by :user_input

--query for the table headers on the creators page
SELECT
    creator_id as 'Creator ID', 
    full_name as 'Creator'
FROM
    Creators
LIMIT 1;

--query to retrieve all records from the creators table
SELECT
    creator_id as 'Creator ID',
    full_name as 'Creator'
FROM
    Creators;

--query to get custom search results for creators page
SELECT
    creator_id as 'Creator ID',
    full_name as 'Creator'
FROM
    Creators
WHERE
    creator_id LIKE :user_input
AND
    full_name LIKE :user_input;

--query to insert a new creator object into the table
INSERT INTO Creators (full_name) VALUES (:user_input);

--query to delete a creator from the table
DELETE FROM Creators WHERE creator_id = :user_input;

--query to load the details of the creator to edit into the edit page
SELECT
    creator_id as 'Creator ID',
    full_name as 'Creator'
FROM
    Creators
WHERE
    creator_id = :user_input;

--query to update the creator that is being edit on the edit page
UPDATE
    Creators
SET
    full_name = :user_input
WHERE
    cretaor_id = :user_input;

--query to get table headers for the suppliers page
SELECT
    supplier_id as 'Supplier ID',
    name as 'Name',
    address as 'Address',
    phone_number as 'Phone Number'
FROM
    Suppliers
LIMIT 1;

--query to get all results for the table on the suppliers page.
SELECT
    supplier_id as 'Supplier ID',
    name as 'Name',
    address as 'Address',
    phone_number as 'Phone Number'
FROM
    Suppliers;

--query to get custom supplier results based on user lookup values
SELECT
    supplier_id as 'Supplier ID',
    name as 'Name',
    address as 'Address',
    phone_number as 'Phone Number'
FROM
    Suppliers
WHERE
    supplier_id LIKE :user_input
AND
    name LIKE :user_input
AND
    phone_number LIKE :user_input;

--query to add a new supplier to the table
INSERT INTO
    Suppliers (
        name,
        address,
        phone_number
    ) VALUES (
        :user_input,
        :user_input,
        :user_input
    );

--query to delete a supplier
DELETE FROM
    Suppliers
WHERE
    supplier_id = :user_input;

--query to find the supplier to edit
SELECT
    supplier_id as 'Supplier ID',
    name as 'Name',
    address as 'Address',
    phone_number as 'Phone Number'
FROM
    Suppliers
WHERE
    supplier_id = :user_input;

--query to update the supplier being edited
UPDATE
    Suppliers
SET
    name = :user_input,
    address = :user_input,
    phone_number = :user_input
WHERE
    supplier_id = :user_input;

--query to get the table headers for the employee page
SELECT
    employee_id as 'Employee ID',
    first_name as 'First Name',
    last_name as 'Last Name',
    phone_number as 'Phone Number',
    address as 'Address'
FROM
    Employees
LIMIT 1;

--query to get the whole list of employees for the employees page
SELECT
    employee_id as 'Employee ID',
    first_name as 'First Name',
    last_name as 'Last Name',
    phone_number as 'Phone Number',
    address as 'Address'
FROM
    Employees;

--query to get a custom list of employess based on dynamic user search
SELECT
    employee_id as 'Employee ID',
    first_name as 'First Name',
    last_name as 'Last Name',
    phone_number as 'Phone Number',
    address as 'Address'
FROM
    Employees
WHERE
    employee_id LIKE :user_input
AND
    first_name LIKE :user_input
AND
    last_name LIKE :user_input
AND (phone_number LIKE :user_input OR phone_number IS NULL);

--query to add a new employee
INSERT INTO
    Employees (first_name, last_name, phone_number, address)
    VALUES (:user_input, :user_input, :user_input, :user_input);

--query to delete an employee
DELETE FROM
    Employees
WHERE
    employee_id = :user_input;

--query to get the details about the employee to edit
SELECT
    employee_id as 'Employee ID',
    first_name as 'First Name',
    last_name as 'Last Name',
    COALESCE(phone_number, '') as 'Phone Number',
    address as 'Address'
FROM
    Employees
WHERE
    employee_id = :user_input;

--query to update the employee being edited
UPDATE
    Employees
SET
    first_name = :user_input,
    last_name = :user_input,
    phone_number = :user_input,
    address = :user_input
WHERE
    employee_id = :user_input;

--query to get the table headers for the patrons page
SELECT
    patron_id as 'Patron ID',
    first_name as 'First Name',
    last_name as 'Last Name',
    phone_number as 'Phone Number',
    fine_amount as 'Fine Amount',
    address as 'Address'
FROM
    Patrons
LIMIT 1;

--query to get all the patrons for the patrons page on load.
SELECT
    patron_id as 'Patron ID',
    first_name as 'First Name',
    last_name as 'Last Name',
    phone_number as 'Phone Number',
    FORMAT(fine_amount, 2) as 'Fine Amount',
    address as 'Address'
FROM
    Patrons;

--get user dynamically generated search results
SELECT
    patron_id as 'Patron ID',
    first_name as 'First Name',
    last_name as 'Last Name',
    phone_number as 'Phone Number',
    FORMAT(fine_amount, 2) as 'Fine Amount',
    address as 'Address'
FROM
    Patrons
WHERE
    patron_id LIKE :user_input
AND
    first_name LIKE :user_input
AND
    last_name LIKE :user_input
AND
    phone_number LIKE :user_input;

--query to insert a new patron
INSERT INTO
    Patrons (first_name, last_name, phone_number, fine_amount, address)
    VALUES (:user_input, :user_input, :user_input, :user_input, :user_input);

--query to delete a patron
DELETE FROM
    Patrons
WHERE
    patron_id = :user_input;

--query to get the details of the patron to edit
SELECT
    patron_id as 'Patron ID',
    first_name as 'First Name',
    last_name as 'Last Name',
    phone_number as 'Phone Number',
    COALESCE(fine_amount, '') as 'Fine Amount',
    address as 'Address'
FROM
    Patrons
WHERE
    patron_id = :user_input;

--query to update the patron being edited
UPDATE
    Patrons
SET
    first_name = :user_input,
    last_name = :user_input,
    phone_number = :user_input,
    fine_amount = :user_input,
    address = :user_input
WHERE
    patron_id = :user_input;

--query to get the table headers for the media items page
SELECT
    item_id as 'Item ID',
    media_type as 'Media Type',
    supplier_id as 'Supplier',
    title as 'Title',
    creator_id as 'Creator',
    release_date as 'Release Date',
    replacement_cost as 'Replacement Cost',
    quantity_owned as 'Quantity Owned'
FROM
    Media_Items
LIMIT 1;

--query to get all the media item details for the media items page
SELECT
    Media_Items.item_id as 'Item ID',
    Media_Items.media_type as 'Media Type',
    Media_Items.supplier_id as 'Supplier ID',
    Suppliers.name as 'Supplier',
    Media_Items.title as 'Title',
    Media_Items.creator_id as 'Creator ID',
    Creators.full_name as 'Creator',
    Media_Items.release_date as 'Release Date',
    FORMAT(Media_Items.replacement_cost, 2) as 'Replacement Cost',
    Media_Items.quantity_owned as 'Quantity Owned'
FROM
    Media_Items
INNER JOIN
    Creators on Media_Items.creator_id = Creators.creator_id
LEFT JOIN
    Suppliers ON Suppliers.supplier_id = Media_Items.supplier_id
ORDER BY
    Media_Items.item_id ASC;

--custom query results for media items based on user search
SELECT
    Media_Items.item_id AS 'Item ID',
    Media_Items.media_type AS 'Media Type',
    Media_Items.supplier_id AS 'Supplier ID',
    Suppliers.name as 'Supplier',
    Media_Items.title AS 'Title',
    Media_Items.creator_id AS 'Creator ID',
    Creators.full_name AS 'Creator',
    Media_Items.release_date AS 'Release Date',
    FORMAT(Media_Items.replacement_cost, 2) AS 'Replacement Cost',
    Media_Items.quantity_owned AS 'Quantity Owned'
FROM
    Media_Items
INNER JOIN
    Creators
ON
    Media_Items.creator_id = Creators.creator_id
LEFT JOIN
    Suppliers
ON
    Suppliers.supplier_id = Media_Items.supplier_id
WHERE
    Media_Items.item_id LIKE :user_input
AND
    Media_Items.media_type LIKE :user_input
AND (
    Suppliers.name LIKE :user_input
    OR
    Suppliers.name IS NULL
    OR
    Suppliers.supplier_id LIKE :user_input)
AND
    Media_Items.title LIKE :user_input
AND
    (Creators.full_name LIKE :user_input
    OR
    Creators.creator_id LIKE :user_input);

--query to insert a new media item
INSERT INTO
    Media_Items (
        media_type, 
        supplier_id, 
        title, 
        creator_id, 
        release_date,
        replacement_cost, 
        quantity_owned
    ) VALUES (
        :user_input,
        :user_input,
        :user_input,
        :user_input,
        :user_input,
        :user_input,
        :user_input
    );

--query to delete a media item
DELETE FROM
    Media_Items
WHERE
    item_id = :user_input;

--query to find the media item details for the item to edit
SELECT
    item_id as 'Item ID',
    media_type as 'Media Type',
    supplier_id as 'Supplier ID',
    title as 'Title',
    creator_id as 'Creator ID',
    release_date as 'Release Date',
    COALESCE(replacement_cost, '') as 'Replacement Cost',
    quantity_owned as 'Quantity Owned'
FROM
    Media_Items
WHERE
    item_id = :user_input;

--query to update the media item being edited
UPDATE
    Media_Items
SET
    media_type = :user_input,
    supplier_id = :user_input,
    title = :user_input,
    creator_id = :user_input,
    release_date = :user_input,
    quantity_owned = :user_input
WHERE
    item_id = :user_input;

--query to get the table headers for media transactions
SELECT
    Media_Transactions.transaction_id as 'Transaction ID',
    Media_Transactions.patron_id as 'Patron ID',
    CONCAT(Patrons.last_name, ', ', Patrons.first_name, ' (', Patrons.patron_id, ')') AS 'Patron',
    Media_Transactions.transaction_type as 'Transaction Type',
    CONCAT(Employees.last_name, ', ', Employees.first_name, ' (', Employees.employee_id, ')') AS 'Employee',
    Media_Transactions.employee_id as 'Employee ID',
    Media_Transactions.item_id as 'Item',
    Media_Transactions.transaction_date as 'Transaction Date'
FROM
    Media_Transactions
INNER JOIN
    Patrons
ON
    Media_Transactions.patron_id = Patrons.patron_id
INNER JOIN
    Employees
ON
    Employees.employee_id = Media_Transactions.employee_id
LIMIT 1;

--query to get the list of media items that are currently checked out
SELECT
    Media_Transactions.transaction_id as 'Transaction ID',
    Media_Transactions.patron_id as 'Patron ID',
    CONCAT(Patrons.last_name, ', ', Patrons.first_name, ' (', Patrons.patron_id, ')') as 'Patron',
    Media_Transactions.transaction_type as 'Transaction Type',
    Media_Transactions.employee_id as 'Employee ID',
    CONCAT(Employees.last_name, ', ', Employees.first_name, ' (', Employees.employee_id, ')') as 'Employee',
    Media_Transactions.item_id as 'Item ID',
    Items.item AS 'Item',
    Counts.transaction_date as 'Transaction Date'
FROM
    Media_Transactions
INNER JOIN
    (
        SELECT DISTINCT
            Media_Transactions.patron_id, 
            Media_Transactions.item_id, 
            COALESCE(media_out.out_count, 0) AS Checkouts, 
            COALESCE(media_in.in_count,0) AS Checkins,
            media_out.transaction_date as transaction_date
        FROM 
            Media_Transactions 
        LEFT JOIN(
            SELECT 
                patron_id, 
                item_id, 
                transaction_type, 
                count(*) AS in_count,
                max(transaction_date) as transaction_date
            FROM 
                Media_Transactions 
            WHERE
                transaction_type = "checkin" 
            GROUP BY 
                patron_id, item_id, transaction_type
            ) media_in 
        ON 
            Media_Transactions.patron_id = media_in.patron_id
        AND 
            Media_Transactions.item_id = media_in.item_id
        LEFT JOIN(
            SELECT
                patron_id,
                item_id,
                transaction_type,
                count(*) AS out_count,
                max(transaction_date) as transaction_date
            FROM 
                Media_Transactions
            WHERE 
                transaction_type = "checkout" 
            GROUP BY
                patron_id, 
                item_id, 
                transaction_type
            ) media_out
        ON
            Media_Transactions.patron_id = media_out.patron_id
        AND
            Media_Transactions.item_id = media_out.item_id
        HAVING
            Checkouts > Checkins
    ) Counts
ON
    Counts.patron_id = Media_Transactions.patron_id
AND
    Counts.item_id = Media_Transactions.item_id
AND
    Counts.transaction_date = Media_Transactions.transaction_date
INNER JOIN
    Patrons
ON
    Patrons.patron_id = Media_Transactions.patron_id
INNER JOIN
    Employees
ON
    Employees.employee_id = Media_Transactions.employee_id
INNER JOIN(
    SELECT
        CONCAT('\'', Media_Items.title, '\' By: ', Creators.full_name, ' (', Media_Items.item_id, ')') AS 'item',
        Media_Items.item_id as 'item_id'
    FROM
        Media_Items
    INNER JOIN
        Creators on Media_Items.creator_id = Creators.creator_id
    ) Items 
ON
    Items.item_id = Media_Transactions.item_id;

--The query to get all checked out items dynamically searched by the user
SELECT
    Media_Transactions.transaction_id as 'Transaction ID',
    Media_Transactions.patron_id as 'Patron ID',
    CONCAT(Patrons.last_name, ', ', Patrons.first_name, ' (', Patrons.patron_id, ')') AS 'Patron',
    Media_Transactions.transaction_type as 'Transaction Type',
    CONCAT(Employees.last_name, ', ', Employees.first_name, ' (', Employees.employee_id, ')') AS 'Employee',
    Media_Transactions.employee_id as 'Employee ID',
    Media_Transactions.item_id as 'Item',
    Media_Transactions.transaction_date as 'Transaction Date'
FROM
    Media_Transactions
INNER JOIN
    Patrons
ON
    Media_Transactions.patron_id = Patrons.patron_id
INNER JOIN
    Employees
ON
    Employees.employee_id = Media_Transactions.employee_id
LIMIT 1;

--query to get the list of media items that are currently checked out
SELECT
    Media_Transactions.transaction_id as 'Transaction ID',
    Media_Transactions.patron_id as 'Patron ID',
    CONCAT(Patrons.last_name, ', ', Patrons.first_name, ' (', Patrons.patron_id, ')') as 'Patron',
    Media_Transactions.transaction_type as 'Transaction Type',
    Media_Transactions.employee_id as 'Employee ID',
    CONCAT(Employees.last_name, ', ', Employees.first_name, ' (', Employees.employee_id, ')') as 'Employee',
    Media_Transactions.item_id as 'Item ID',
    Items.item AS 'Item',
    Counts.transaction_date as 'Transaction Date'
FROM
    Media_Transactions
INNER JOIN
    (
        SELECT DISTINCT
            Media_Transactions.patron_id, 
            Media_Transactions.item_id, 
            COALESCE(media_out.out_count, 0) AS Checkouts, 
            COALESCE(media_in.in_count,0) AS Checkins,
            media_out.transaction_date as transaction_date
        FROM 
            Media_Transactions 
        LEFT JOIN(
            SELECT 
                patron_id, 
                item_id, 
                transaction_type, 
                count(*) AS in_count,
                max(transaction_date) as transaction_date
            FROM 
                Media_Transactions 
            WHERE
                transaction_type = "checkin" 
            GROUP BY 
                patron_id, item_id, transaction_type
            ) media_in 
        ON 
            Media_Transactions.patron_id = media_in.patron_id
        AND 
            Media_Transactions.item_id = media_in.item_id
        LEFT JOIN(
            SELECT
                patron_id,
                item_id,
                transaction_type,
                count(*) AS out_count,
                max(transaction_date) as transaction_date
            FROM 
                Media_Transactions
            WHERE 
                transaction_type = "checkout" 
            GROUP BY
                patron_id, 
                item_id, 
                transaction_type
            ) media_out
        ON
            Media_Transactions.patron_id = media_out.patron_id
        AND
            Media_Transactions.item_id = media_out.item_id
        HAVING
            Checkouts > Checkins
    ) Counts
ON
    Counts.patron_id = Media_Transactions.patron_id
AND
    Counts.item_id = Media_Transactions.item_id
AND
    Counts.transaction_date = Media_Transactions.transaction_date
INNER JOIN
    Patrons
ON
    Patrons.patron_id = Media_Transactions.patron_id
INNER JOIN
    Employees
ON
    Employees.employee_id = Media_Transactions.employee_id
INNER JOIN(
    SELECT
        CONCAT('\'', Media_Items.title, '\' By: ', Creators.full_name, ' (', Media_Items.item_id, ')') AS 'item',
        Media_Items.item_id as 'item_id'
    FROM
        Media_Items
    INNER JOIN
        Creators on Media_Items.creator_id = Creators.creator_id
    ) Items 
ON
    Items.item_id = Media_Transactions.item_id
WHERE
    (Media_Transactions.patron_id LIKE :user_input 
    OR Patrons.first_name LIKE :user_input 
    OR Patrons.last_name LIKE :user_input 
    OR CONCAT(Patrons.last_name, ', ', Patrons.first_name) LIKE :user_input)
AND
    (Media_Transactions.employee_id LIKE :user_input
    OR Employees.first_name LIKE :user_input
    OR Employees.last_name LIKE :user_input
    OR CONCAT(Employees.last_name, ', ', Employees.first_name) LIKE :user_input)
AND
    Media_Transactions.transaction_type LIKE :user_input
AND
    (Media_Transactions.item_id LIKE :user_input
    OR Items.item LIKE :user_input)
AND
    Counts.transaction_date BETWEEN :user_input AND :user_input;

--query that returns all history regardless of checkin or checkout
SELECT
    Media_Transactions.transaction_id as 'Transaction ID',
    Media_Transactions.patron_id as 'Patron ID',
    CONCAT(Patrons.last_name, ', ', Patrons.first_name, ' (', Patrons.patron_id, ')') AS 'Patron',
    Media_Transactions.transaction_type as 'Transaction Type',
    Media_Transactions.employee_id as 'Employee ID',
    CONCAT(Employees.last_name, ', ', Employees.first_name, ' (', Employees.employee_id, ')') AS 'Employee',
    Media_Transactions.item_id as 'Item ID',
    Items.item AS 'Item',
    Media_Transactions.transaction_date as 'Transaction Date'
FROM
    Media_Transactions
INNER JOIN
    Patrons ON Patrons.patron_id = Media_Transactions.patron_id
INNER JOIN
    Employees ON Employees.employee_id = Media_Transactions.employee_id
INNER JOIN(
    SELECT
        CONCAT('\'', Media_Items.title, '\' By: ', Creators.full_name, ' (', Media_Items.item_id, ')') AS 'item',
        Media_Items.item_id as 'item_id'
    FROM
        Media_Items
    INNER JOIN 
        Creators
    ON
        Media_Items.creator_id = Creators.creator_id
) Items
ON
    Media_Transactions.item_id = Items.item_id
WHERE
    (Patrons.patron_id LIKE :user_input
    OR Patrons.first_name LIKE :user_input
    OR Patrons.last_name LIKE :user_input
    OR CONCAT(Patrons.last_name, ', ', Patrons.first_name) LIKE :user_input)
AND
    (Employees.employee_id LIKE :user_input
    OR Employees.first_name LIKE :user_input
    OR Employees.last_name LIKE :user_input
    OR CONCAT(Employees.last_name, ', ', Employees.first_name) LIKE :user_input)
AND
    Media_Transactions.transaction_type LIKE :user_input
AND
    (Media_Transactions.item_id LIKE :user_input OR Items.item LIKE :user_input)
AND
    Media_Transactions.transaction_date BETWEEN :user_input AND :user_input;

--query to add a new media transaction
INSERT INTO
    Media_Transactions (
        patron_id, 
        transaction_type, 
        employee_id, 
        item_id, 
        transaction_date
    ) VALUES (
        :user_input,
        :user_input,
        :user_input,
        :user_input,
        :user_input
    );

--query to find the media transaction to edit
SELECT
    transaction_id as 'Transaction ID',
    patron_id as 'Patron ID',
    transaction_type as 'Transaction Type',
    employee_id as 'Employee ID',
    item_id as 'Item ID',
    transaction_date as 'Transaction Date'
FROM
    Media_Transactions
WHERE
    transaction_id = :user_input;

--query to update the media transaction being edit
UPDATE
    Media_Transactions
SET
    patron_id = :user_input,
    transaction_type = :user_input,
    employee_id = :user_input,
    item_id = :user_input
WHERE
    transaction_id = :user_input;

--query to delete a media transaction
DELETE FROM
    Media_Transactions
WHERE
    transaction_id = :user_input;

--query to get a list of all supplier ids
SELECT
    name as 'Supplier',
    supplier_id as 'Supplier ID'
FROM
    Suppliers
ORDER BY
    name ASC;

--query to get a list of all creator ids
SELECT
    full_name as 'Creator',
    creator_id as 'Creator ID'
FROM
    Creators
ORDER BY full_name ASC;

--query to get a list of all patron ids
SELECT
    CONCAT(last_name, ", ", first_name, " (", patron_id, ")") as 'Patron',
    patron_id as 'Patron ID'
FROM
    Patrons
ORDER BY
    CONCAT(last_name, ", ", first_name, " (", patron_id, ")") ASC;

--query to get a list of all employee ids
SELECT
    CONCAT(last_name, ', ', first_name '(', employee_id, ')') as 'Employee',
    employee_id as 'Employee ID'
FROM
    Employees
ORDER BY
    CONCAT(last_name, ', ', first_name ' (', employee_id, ')') ASC;

--query to get a list of all media items
SELECT
    CONCAT('\'', Media_Items.title, '\' By: ', Creators.full_name, ' (', Media_Items.item_id, ')') AS 'Item',
    Media_Items.item_id as 'Item ID'
FROM
    Media_Items
INNER JOIN
    Creators on Media_Items.creator_id = Creators.creator_id
ORDER BY
    CONCAT('\'', Media_Items.title, '\' By: ', Creators.full_name, 
    ' (', Media_Items.item_id, ')') ASC;


--query to get employees not to be deleted
SELECT DISTINCT
    employee_id as 'Employee ID'
FROM
    Media_Transactions
ORDER BY employee_id ASC;

--query to get patrons not to be deleted
SELECT DISTINCT
    patron_id as 'Patron ID'
FROM
    Media_Transactions
ORDER BY patron_id ASC;

--query to get items not to be deleted
SELECT DISTINCT
    item_id as 'Item ID'
FROM
    Media_Transactions
ORDER BY
    item_id ASC;

--query to prevent creator deletion
SELECT DISTINCT
    creator_id AS 'Creator ID'
FROM
    Media_Items;