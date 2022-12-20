"""This module houses all of the string queries for the local library app.

The purpose of this file is to clean up the routes in the main app.py file
so that the processing inside the route is easier to see and maintain.
"""

def creators_query_headers():
    """Header query for the creators page.

    Returns:
        str: The string query for the headers on the creators page.
    """

    query = "SELECT creator_id as 'Creator ID', full_name as "
    query += "'Creator' FROM Creators LIMIT 1;"

    return query

def get_creators_query_results():
    """All results from the Creators table to load into the search area.

    Returns:
        str: The string query for all search results on the creators page.
    """

    query = "SELECT creator_id as 'Creator ID', full_name as "
    query += "'Creator' FROM Creators;"

    return query

def post_creators_query_results():
    """Custom query results string for the creators page dynamic search.

    Returns:
        str: The string query for the dynamic search on the creators page.
    """

    query = "SELECT creator_id as 'Creator ID', full_name as "
    query += "'Creator' FROM Creators WHERE creator_id LIKE %s"
    query += " AND full_name LIKE %s;"

    return query

def new_creator_insert_query():
    """The insert query to insert a new creator into the creators page.

    Returns:
        str: The string query to insert a new creator on the creators page.
    """

    query = "INSERT INTO Creators (full_name) VALUES (%s);"

    return query

def delete_creator_query():
    """The query to delete a creator from the creators page.

    Returns:
        str: The string query to delete a creator.
    """

    query = "DELETE FROM Creators WHERE creator_id = %s;"

    return query

def get_edit_creators_find_query():
    """The query to load a creator to edit.

    Returns:
        str: The string query to locate the creator to edit.
    """

    query = "SELECT creator_id as 'Creator ID', full_name as "
    query += "'Creator' FROM Creators WHERE creator_id = %s;"

    return query

def post_edit_creators_update_query():
    """The query to update creator information.

    Returns:
        str: The update query to edit a creator entry.
    """

    query = "UPDATE Creators SET full_name = %s WHERE "
    query += "creator_id = %s;"

    return query

def suppliers_header_query():
    """Header query for the suppliers page.

    Returns:
        str: The string query for the headers on the suppliers page.
    """

    query = "SELECT supplier_id as 'Supplier ID', name as"
    query += "'Name', address as 'Address', "
    query += "phone_number as 'Phone Number' "
    query += "FROM Suppliers LIMIT 1;"

    return query

def get_suppliers_results_query():
    """All results from the Suppliers table to load into the search area.

    Returns:
        str: The string query for all search results on the suppliers page.
    """

    query = "SELECT supplier_id as 'Supplier ID', name as "
    query += "'Name', address as 'Address', phone_number "
    query += "as 'Phone Number' FROM Suppliers;"

    return query

def post_suppliers_results_query():
    """Custom query results string for the suppliers page dynamic search.

    Returns:
        str: The string query for the dynamic search on the suppliers page.
    """

    query = "SELECT supplier_id as 'Supplier ID', name as "
    query += "'Name', address as 'Address', "
    query += "phone_number as 'Phone Number' FROM "
    query += "Suppliers WHERE supplier_id LIKE %s AND name"
    query += " LIKE %s AND phone_number LIKE %s"

    return query

def new_suppliers_insert_query():
    """The insert query to insert a new supplier into the suppliers page.

    Returns:
        str: The string query to insert a new supplier on the suppliers page.
    """

    query = "INSERT INTO Suppliers (name, address, "
    query += "phone_number) VALUES (%s, %s, %s);"

    return query

def delete_suppliers_query():
    """The query to delete a supplier from the suppliers page.

    Returns:
        str: The string query to delete a supplier.
    """

    query = "DELETE FROM Suppliers WHERE supplier_id = %s;"

    return query

def get_edit_suppliers_find_query():
    """The query to load a supplier to edit.

    Returns:
        str: The string query to locate the supplier to edit.
    """

    query = "SELECT supplier_id as 'Supplier ID', name as "
    query += "'Name', address as 'Address', phone_number "
    query += "as 'Phone Number' FROM Suppliers "
    query += "WHERE supplier_id = %s;"

    return query

def post_edit_suppliers_update_query():
    """The query to update supplier information.

    Returns:
        str: The update query to edit a supplier entry.
    """

    query = "UPDATE Suppliers SET name = %s, "
    query += "address = %s, phone_number = %s "
    query += "WHERE supplier_id = %s;"

    return query

def employee_header_query():
    """Header query for the employees page.

    Returns:
        str: The string query for the headers on the employees page.
    """

    query = "SELECT employee_id as 'Employee ID', first_name as"
    query += "'First Name', last_name as 'Last Name', "
    query += "phone_number as 'Phone Number', address as "
    query += "'Address' FROM Employees LIMIT 1;"

    return query

def get_employee_results_query():
    """The query that generates a list of all employees.

    Returns:
        str: The string query that generates all employees.
    """

    query = "SELECT employee_id as 'Employee ID', first_name as "
    query += "'First Name', last_name as 'Last Name', phone_number "
    query += "as 'Phone Number', address as 'Address' FROM Employees;"

    return query

def post_employee_results_query():
    """The custom query that generates a dynamic employee search.

    Returns:
        str: The string query to generate a dynamic employee search.
    """

    query = "SELECT employee_id as 'Employee ID', first_name as "
    query += "'First Name', last_name as 'Last Name', phone_number "
    query += "as 'Phone Number', address as 'Address' FROM "
    query += "Employees WHERE employee_id LIKE %s AND first_name"
    query += " LIKE %s AND last_name LIKE %s AND (phone_number "
    query += "LIKE %s OR phone_number IS NULL);"

    return query

def new_employee_insert_query():
    """The insert query to add a new employee.

    Returns:
        str: The insert string query to add a new employee.
    """

    query = "INSERT INTO Employees (first_name, last_name, "
    query += "phone_number, address) VALUES (%s, %s, %s, %s);"

    return query

def delete_employee_query():
    """The string query to delete an employee.

    Returns:
        str: The string query to delete an employee.
    """

    query = "DELETE FROM Employees WHERE employee_id = %s;"

    return query

def get_edit_employee_find_query():
    """The query to find a specific employee to edit.

    Returns:
        str: The string query to find the employee to edit.
    """

    query = "SELECT employee_id as 'Employee ID', first_name as "
    query += "'First Name', last_name as 'Last Name', COALESCE(phone_number, '') "
    query += "as 'Phone Number', address as 'Address' FROM "
    query += "Employees WHERE employee_id = %s;"

    return query

def post_edit_employee_update_query():
    """The update query to edit employee attributes.

    Returns:
        str: The string query to update and edit employee attributes.
    """

    query = "UPDATE Employees SET first_name = %s, last_name = "
    query += "%s, phone_number = %s, address = %s "
    query += "WHERE employee_id = %s;"

    return query

def patrons_query_headers():
    """Header query for the patrons page.

    Returns:
        str: The string query for the headers on the patrons page.
    """

    query = "SELECT patron_id as 'Patron ID', first_name as "
    query += "'First Name', last_name as 'Last Name', "
    query += "phone_number as 'Phone Number', fine_amount as "
    query += "'Fine Amount', address as 'Address' FROM Patrons LIMIT 1;"

    return query

def get_patrons_query_results():
    """The query that generates a list of all patrons.

    Returns:
        str: The string query that generates all patrons.
    """

    query = "SELECT patron_id as 'Patron ID', first_name as "
    query += "'First Name', last_name as 'Last Name', "
    query += "phone_number as 'Phone Number', FORMAT(fine_amount, 2) as "
    query += "'Fine Amount', address as 'Address' FROM Patrons;"

    return query

def post_patrons_query_results():
    """The custom query that generates a dynamic patron search.

    Returns:
        str: The string query to generate a dynamic patron search.
    """

    query = "SELECT patron_id as 'Patron ID', first_name as "
    query += "'First Name', last_name as 'Last Name', "
    query += "phone_number as 'Phone Number', FORMAT(fine_amount, 2) as "
    query += "'Fine Amount', address as 'Address' FROM Patrons "
    query += "WHERE patron_id LIKE %s AND first_name LIKE %s "
    query += "AND last_name LIKE %s AND phone_number Like %s;"

    return query

def new_patrons_insert_query():
    """The insert query to add a new patron.

    Returns:
        str: The insert string query to add a new patron.
    """

    query = "INSERT INTO Patrons (first_name, last_name, "
    query += "phone_number, fine_amount, address) VALUES (%s, %s, %s, %s, %s);"

    return query

def delete_patrons_query():
    """The string query to delete a patron.

    Returns:
        str: The string query to delete a patron.
    """

    query = "DELETE FROM Patrons WHERE patron_id = %s;"

    return query

def get_edit_patrons_find_query():
    """The query to find a specific patron to edit.

    Returns:
        str: The string query to find the patron to edit.
    """

    query = "SELECT patron_id as 'Patron ID', first_name as "
    query += "'First Name', last_name as 'Last Name', "
    query += "phone_number as 'Phone Number', COALESCE(fine_amount, '') as "
    query += "'Fine Amount', address as 'Address' FROM Patrons "
    query += "WHERE patron_id = %s;"

    return query

def post_edit_patrons_update_query():
    """The update query to edit patron attributes.

    Returns:
        str: The string query to update and edit patron attributes.
    """

    query = "UPDATE Patrons SET first_name = %s, "
    query += "last_name = %s, phone_number = %s, "
    query += "fine_amount = %s, address = %s "
    query += "WHERE patron_id = %s;"

    return query

def media_items_header_query():
    """The string query to generate the headers for the media items page.

    Returns:
        str: The string query for media items headers.
    """

    query = "SELECT item_id AS 'Item ID', media_type AS 'Media Type', "
    query += "supplier_id as 'Supplier', title as 'Title', creator_id"
    query += " AS 'Creator', release_date AS 'Release Date', "
    query += "replacement_cost AS 'Replacement Cost', quantity_owned AS "
    query += "'Quantity Owned' FROM Media_Items LIMIT 1;"

    return query

def get_media_items_results_query():
    """The query that returns all results from media items.

    Returns:
        str: The string query to return all media items.
    """

    query = "SELECT Media_Items.item_id AS 'Item ID', Media_Items.media_type "
    query += "AS 'Media Type', Media_Items.supplier_id as 'Supplier ID', "
    query += "Suppliers.name as 'Supplier', "
    query += "Media_Items.title as 'Title', Media_Items.creator_id AS "
    query += "'Creator ID', Creators.full_name as 'Creator', "
    query += "Media_Items.release_date AS 'Release Date', "
    query += "FORMAT(Media_Items.replacement_cost, 2) AS 'Replacement Cost', "
    query += "Media_Items.quantity_owned AS "
    query += "'Quantity Owned' FROM Media_Items INNER JOIN Creators ON "
    query += "Media_Items.creator_id = Creators.creator_id LEFT JOIN Suppliers"
    query += " ON Suppliers.supplier_id = Media_Items.supplier_id ORDER BY"
    query += " Media_Items.item_id ASC;"

    return query

def post_media_items_search_query():
    """The custom query to dynamically search for media items.

    Returns:
        str: The string query to dynamically search for media items.
    """
    query = "SELECT Media_Items.item_id AS 'Item ID', Media_Items.media_type "
    query += "AS 'Media Type', Media_Items.supplier_id as 'Supplier ID', "
    query += "Suppliers.name as 'Supplier',"
    query += "Media_Items.title as 'Title', Media_Items.creator_id AS "
    query += "'Creator ID', Creators.full_name as 'Creator', "
    query += "Media_Items.release_date AS 'Release Date', "
    query += "FORMAT(Media_Items.replacement_cost, 2) AS 'Replacement Cost', "
    query += "Media_Items.quantity_owned AS "
    query += "'Quantity Owned' FROM Media_Items INNER JOIN Creators ON "
    query += "Media_Items.creator_id = Creators.creator_id LEFT JOIN Suppliers"
    query += " ON Suppliers.supplier_id = Media_Items.supplier_id"
    query += " WHERE Media_Items.item_id LIKE %s AND"
    query += " Media_Items.media_type LIKE %s AND (Suppliers.name "
    query += "LIKE %s OR Suppliers.name IS NULL OR Suppliers.supplier_id LIKE %s) "
    query += "AND Media_Items.title LIKE %s AND (Creators.full_name LIKE %s OR"
    query += " Creators.creator_id LIKE %s);"

    return query

def new_media_item_insert_query():
    """The insert query to add a new media item.

    Returns:
        str: The insert query to add a new media item.
    """

    query = "INSERT INTO Media_Items (media_type, supplier_id, title, "
    query += "creator_id, release_date, replacement_cost, quantity_owned)"
    query += " VALUES ( %s, %s, %s, %s, %s, %s, %s );"

    return query

def delete_media_item_query():
    """The delete query to remove a media item.

    Returns:
        str: The delete query to remove a media item.
    """

    query = "DELETE FROM Media_Items WHERE item_id = %s;"

    return query

def edit_media_item_find_query():
    """The query to find a specific media item to edit.

    Returns:
        str: The query to find a specific media item to edit.
    """

    query = "SELECT item_id AS 'Item ID', media_type AS 'Media Type', "
    query += "supplier_id AS 'Supplier ID', title AS 'Title', creator_id"
    query += " AS 'Creator ID', release_date AS 'Release Date', "
    query += "COALESCE(replacement_cost, '') AS 'Replacement Cost', quantity_owned AS "
    query += "'Quantity Owned' FROM Media_Items WHERE item_id = %s;"

    return query

def post_edit_media_item_query():
    """The update query to edit the attributes of a media item.

    Returns:
        str: The update query to edit the attributes of a media item.
    """

    query = "UPDATE Media_Items SET media_type = %s, supplier_id = %s"
    query += ", title = %s, creator_id = %s, release_date = %s, "
    query += "replacement_cost = %s, quantity_owned = %s WHERE item_id"
    query += " = %s;"

    return query

def media_transactions_header_query():
    """The query to generate table headers for the media transactions page.

    Returns:
        str: The query to generate table headers for the media transactions
             page.
    """

    query = "SELECT Media_Transactions.transaction_id AS 'Transaction ID', "
    query += "Media_Transactions.patron_id "
    query += "AS 'Patron ID', CONCAT(Patrons.last_name, ', ', "
    query += "Patrons.first_name, ' (', Patrons.patron_id, ')') as "
    query += "'Patron', Media_Transactions.transaction_type as "
    query += "'Transaction Type', CONCAT(Employees.last_name, ', ', "
    query += "Employees.first_name, ' (', Employees.employee_id, ')') as "
    query += "'Employee', "
    query += "Media_Transactions.employee_id as 'Employee ID', "
    query += "Media_Transactions.item_id as 'Item', "
    query += "Media_Transactions.transaction_date AS 'Transaction Date' FROM "
    query += "Media_Transactions INNER JOIN Patrons on "
    query += "Media_Transactions.patron_id = Patrons.patron_id INNER JOIN "
    query += "Employees ON Employees.employee_id = "
    query += "Media_Transactions.employee_id LIMIT 1;"

    return query

def get_media_transactions_all_checkouts_query():
    """The query to get all current media transactions that are checked out.

    Returns:
        str: The query to get all checked out media items.
    """

    query = "SELECT Media_Transactions.transaction_id AS 'Transacti"
    query += "on ID', Media_Transactions.patron_id AS 'Patron ID', "
    query += "CONCAT(Patrons.last_name, ', ', Patrons.first_name, ' (', "
    query += "Patrons.patron_id, ')') as 'Patron', "
    query += "Media_Transactions.transaction_type AS 'Transaction "
    query += "Type', Media_Transactions.employee_id as 'Employee ID',"
    query += " CONCAT(Employees.last_name, ', ', Employees.first_name, ' (', "
    query += "Employees.employee_id, ')') AS 'Employee',"
    query += " Media_Transactions.item_id as 'Item ID', "
    query += "Items.item as 'Item', Counts.trans"
    query += "action_date AS 'Transaction Date' FROM Media_Transact"
    query += "ions INNER JOIN (SELECT DISTINCT Media_Transactions."
    query += "patron_id, Media_Transactions.item_id, COALESCE(media"
    query += "_out.out_count, 0) AS Checkouts, COALESCE(media_in.in_"
    query += "count, 0) AS Checkins, media_out.transaction_date as"
    query += " transaction_date FROM Media_Transactions LEFT JOIN "
    query += "(SELECT patron_id, item_id, transaction_type, count(*) "
    query += "AS in_count, max(transaction_date) as transaction_date"
    query += " FROM Media_Transactions WHERE transaction_type = "
    query += "'checkin' GROUP BY patron_id, item_id, transaction_"
    query += "type) media_in ON Media_Transactions.patron_id = "
    query += "media_in.patron_id AND Media_Transactions.item_id = "
    query += "media_in.item_id LEFT JOIN( SELECT patron_id, item_id, "
    query += "transaction_type, count(*) AS out_count, max(transact"
    query += "ion_date) as transaction_date FROM Media_Transactions"
    query += " WHERE transaction_type = 'checkout' GROUP BY patron_"
    query += "id, item_id, transaction_type) media_out ON Media_Tran"
    query += "sactions.patron_id = media_out.patron_id AND Media_Tran"
    query += "sactions.item_id = media_out.item_id HAVING Checkouts >"
    query += " Checkins) Counts ON Counts.patron_id = Media_Transacti"
    query += "ons.patron_id AND Counts.item_id = Media_Transactions."
    query += "item_id AND Counts.transaction_date = Media_Transactio"
    query += "ns.transaction_date INNER JOIN Patrons on Patrons.patron_id = "
    query += "Media_Transactions.patron_id INNER JOIN Employees on "
    query += "Employees.employee_id = Media_Transactions.employee_id"
    query += " INNER JOIN( SELECT CONCAT('\\'', Media_Items.title, '\\' By: "
    query += "', Creators.full_name, ' (', Media_Items.item_id, ')') AS 'item',"
    query += " Media_Items.item_id AS 'item_id' FROM Media_Items INNER JOIN "
    query += "Creators ON Media_Items.creator_id = Creators.creator_id) Items"
    query += " ON Items.item_id = Media_Transactions.item_id;"

    return query

def post_media_transactions_checkouts_custom_query():
    """The dynamic search query to find checked out media items.

    Returns:
        str: The dynamic search query to find checked out media items.
    """

    query = "SELECT Media_Transactions.transaction_id AS 'Transacti"
    query += "on ID', Media_Transactions.patron_id AS 'Patron ID', "
    query += "CONCAT(Patrons.last_name, ', ', Patrons.first_name, ' (', "
    query += "Patrons.patron_id, ')') as 'Patron', "
    query += "Media_Transactions.transaction_type AS 'Transaction "
    query += "Type', Media_Transactions.employee_id as 'Employee ID',"
    query += " CONCAT(Employees.last_name, ', ', Employees.first_name, ' (', "
    query += "Employees.employee_id, ')') AS 'Employee',"
    query += " Media_Transactions.item_id as 'Item ID', "
    query += "Items.item as 'Item', Counts.trans"
    query += "action_date AS 'Transaction Date' FROM Media_Transact"
    query += "ions INNER JOIN (SELECT DISTINCT Media_Transactions."
    query += "patron_id, Media_Transactions.item_id, COALESCE(media"
    query += "_out.out_count, 0) AS Checkouts, COALESCE(media_in.in_"
    query += "count, 0) AS Checkins, media_out.transaction_date as"
    query += " transaction_date FROM Media_Transactions LEFT JOIN "
    query += "(SELECT patron_id, item_id, transaction_type, count(*) "
    query += "AS in_count, max(transaction_date) as transaction_date"
    query += " FROM Media_Transactions WHERE transaction_type = "
    query += "'checkin' GROUP BY patron_id, item_id, transaction_"
    query += "type) media_in ON Media_Transactions.patron_id = "
    query += "media_in.patron_id AND Media_Transactions.item_id = "
    query += "media_in.item_id LEFT JOIN( SELECT patron_id, item_id, "
    query += "transaction_type, count(*) AS out_count, max(transact"
    query += "ion_date) as transaction_date FROM Media_Transactions"
    query += " WHERE transaction_type = 'checkout' GROUP BY patron_"
    query += "id, item_id, transaction_type) media_out ON Media_Tran"
    query += "sactions.patron_id = media_out.patron_id AND Media_Tran"
    query += "sactions.item_id = media_out.item_id HAVING Checkouts >"
    query += " Checkins) Counts ON Counts.patron_id = Media_Transacti"
    query += "ons.patron_id AND Counts.item_id = Media_Transactions."
    query += "item_id AND Counts.transaction_date = Media_Transactio"
    query += "ns.transaction_date INNER JOIN Patrons on Patrons.patron_id = "
    query += "Media_Transactions.patron_id INNER JOIN Employees on "
    query += "Employees.employee_id = Media_Transactions.employee_id"
    query += " INNER JOIN( SELECT CONCAT('\\'', Media_Items.title, '\\' By: "
    query += "', Creators.full_name, ' (', Media_Items.item_id, ')') AS 'item',"
    query += " Media_Items.item_id AS 'item_id' FROM Media_Items INNER JOIN "
    query += "Creators ON Media_Items.creator_id = Creators.creator_id) Items"
    query += " ON Items.item_id = Media_Transactions.item_id"
    query += " WHERE (Media_Transactions.patron_"
    query += "id LIKE %s OR Patrons.first_name LIKE %s OR Patrons.last_name "
    query += "LIKE %s OR CONCAT(Patrons.last_name, ', ', Patrons.first_name) "
    query += "LIKE %s) AND (Media_Transactions.employee_id LIKE %s OR "
    query += "Employees.first_name LIKE %s OR Employees.last_name LIKE %s OR "
    query += "CONCAT(Employees.last_name, ', ', Employees.first_name) LIKE %s) "
    query += "AND Media_Transactions.transaction_type LIKE %s AND "
    query += "(Media_Transactions.item_id LIKE %s OR Items.item LIKE %s) AND "
    query += "Counts.transaction_date BETWEEN %s AND %s;"

    return query

def get_all_media_transactions_custom_query():
    """Dynamic search query that returns media transactions for all history.

    Returns:
        str: The query string to return dynamic results for all transactions.
    """

    query = "SELECT Media_Transactions.transaction_id AS 'Transaction ID', "
    query += "Media_Transactions.patron_id AS 'Patron ID', CONCAT("
    query += "Patrons.last_name, ', ', Patrons.first_name, ' (', "
    query += "Patrons.patron_id, ')') AS 'Patron', "
    query += "Media_Transactions.transaction_type AS 'Transaction Type', "
    query += "Media_Transactions.employee_id AS "
    query += "'Employee ID', CONCAT(Employees.last_name, ', ', "
    query += "Employees.first_name, ' (', Employees.employee_id, ')') AS "
    query += "'Employee',  Media_Transactions.item_id AS 'Item ID', "
    query += "Items.item as 'Item', "
    query += "Media_Transactions.transaction_date AS "
    query += "'Transaction Date' FROM Media_Transactions INNER JOIN Patrons ON "
    query += "Patrons.patron_id = Media_Transactions.patron_id INNER JOIN "
    query += "Employees on Employees.employee_id = "
    query += "Media_Transactions.employee_id"
    query += " INNER JOIN( SELECT CONCAT('\\'', Media_Items.title, '\\' By: "
    query += "', Creators.full_name, ' (', Media_Items.item_id, ')') AS 'item',"
    query += " Media_Items.item_id AS 'item_id' FROM Media_Items INNER JOIN "
    query += "Creators ON Media_Items.creator_id = Creators.creator_id) Items"
    query += " ON Media_Transactions.item_id = Items.item_id"
    query += " WHERE (Patrons.patron_id LIKE %s "
    query += "OR Patrons.first_name LIKE %s OR Patrons.last_name LIKE %s OR "
    query += "CONCAT(Patrons.last_name, ', ', Patrons.first_name) LIKE %s) "
    query += "AND (Employees.employee_id LIKE %s OR Employees.first_name LIKE "
    query += "%s OR Employees.last_name LIKE %s OR CONCAT(Employees.last_name, "
    query += "', ', Employees.first_name) LIKE %s) "
    query += "AND Media_Transactions.transaction_type LIKE "
    query += "%s and (Media_Transactions.item_id LIKE %s OR Items.item LIKE %s )and "
    query += "Media_Transactions.transaction_date "
    query += "BETWEEN %s AND %s;"

    return query

def new_media_transaction_insert_query():
    """The query to insert a new media transaction.

    Returns:
        str: The query to insert a new media transaction.
    """

    query = "INSERT INTO Media_Transactions (patron_id, transaction_type,"
    query += " employee_id, item_id, transaction_date) VALUES "
    query += "(%s, %s, %s, %s, %s);"

    return query

def edit_media_transaction_find_query():
    """The query to find the media transaction to edit.

    Returns:
        str: The query to find the media transaction to edit.
    """

    query = "SELECT transaction_id as 'Transaction ID', patron_id AS "
    query += "'Patron ID', transaction_type AS 'Transaction Type', "
    query += "employee_id as 'Employee ID', item_id AS 'Item ID', transacti"
    query += "on_date AS 'Transaction Date' FROM Media_Transactions WHERE "
    query += "transaction_id = %s;"

    return query

def post_edit_media_transaction_update_query():
    """The update query to save edited attributes for a media transaction.

    Returns:
        str: The update query for an edited media transaction.
    """

    query = "UPDATE Media_Transactions SET patron_id = %s, transaction_"
    query += "type = %s, employee_id = %s, item_id = %s WHERE "
    query += "transaction_id = %s;"

    return query

def delete_media_transaction_query():
    """The query to delete a media transaction.

    Returns:
        str: The query to delete a media transaction.
    """

    query = "DELETE FROM Media_Transactions WHERE transaction_id = %s;"

    return query

def get_supplier_ids_query():
    """The query to retrieve all supplier ID's for new/editing foreign keys.

    Returns:
        str: The query to retrieve all supplier ID's.
    """

    query = "SELECT name as 'Supplier', supplier_id AS 'Supplier ID' FROM "
    query += "Suppliers ORDER BY name ASC;"

    return query

def get_creator_ids_query():
    """The query to retrieve all creator ID's for new/editing foreign keys.

    Returns:
        str: The query to retrieve all creator ID's.
    """

    query = "SELECT full_name as 'Creator', creator_id AS 'Creator ID' FROM "
    query += "Creators ORDER BY full_name ASC;"

    return query

def get_patron_ids_query():
    """The query to retrieve all patron ID's for new/editing foreign keys.

    Returns:
        str: The query to retrieve all patron ID's.
    """

    query = "SELECT CONCAT(last_name, ', ', first_name, ' (', patron_id, ')') as "
    query += "'Patron', patron_id as 'Patron ID' FROM Patrons ORDER BY"
    query += " CONCAT(last_name, ', ', first_name, ' (', patron_id, ')') ASC;"

    return query

def get_employee_ids_query():
    """The query to retrieve all employee ID's for new/editing foreign keys.

    Returns:
        str: The query to retrieve all employee ID's.
    """

    query = "SELECT CONCAT(last_name, ', ', first_name, ' (', employee_id, ')')"
    query += " AS 'Employee', employee_id as 'Employee ID' FROM Employees"
    query += " ORDER BY CONCAT(last_name, ', ', first_name, '(', "
    query += "employee_id, ')') ASC;"

    return query

def get_items_query():
    """The query to retrieve all media items for new/editing foreign keys.

    Returns:
        str: The query to retrieve all media items.
    """

    query = "SELECT CONCAT('\\'', Media_Items.title, '\\' By: ', Creators.full_name,"
    query += " ' (', Media_Items.item_id, ')') AS 'Item', Media_Items.item_id "
    query += "AS 'Item ID' FROM Media_Items INNER JOIN Creators ON "
    query += "Creators.creator_id = Media_Items.creator_id ORDER BY "
    query += "CONCAT('\\'', Media_Items.title, '\\' By: ', Creators.full_name, ' "
    query += "(', Media_Items.item_id, ')') ASC;"

    return query


def prevent_employee_delete():
    """The query to retrieve list of employees who have made transactions.

    Returns:
        str: The query to allow or deny deletion of employee with transactions.
    """

    query = "SELECT DISTINCT employee_id AS 'Employee ID' FROM "
    query += "Media_Transactions ORDER BY employee_id ASC;"

    return query

def prevent_patron_delete():
    """The query to retrieve list of patrons who have made transactions.

    Returns:
        str: The query to allow or deny deletion of patron with transactions.
    """

    query = "SELECT DISTINCT patron_id AS 'Patron ID' FROM "
    query += "Media_Transactions ORDER BY patron_id ASC;"

    return query

def prevent_item_delete():
    """The query to retieve list of media items that have been checked out

    Returns:
        str: The query to allow or deny deletion of media items that have been
        checked out.
    """

    query = "SELECT DISTINCT item_id AS 'Item ID' FROM Media_Transactions "
    query += "ORDER BY item_id ASC;"

    return query

def prevent_creator_delete():
    """The query to retrieve list of creators that have media items

    Returns:
        str: The query to prevent creators with media items from being deleted.
    """

    query = "SELECT DISTINCT creator_id AS 'Creator ID' FROM Media_Items;"
    return query
