"""
This module is used to start the Local Library Database Maintenance Flask
application.
"""

import os
from datetime import datetime, timedelta
from flask import Flask, redirect, render_template, request, flash
from flask_mysqldb import MySQL
import string_queries as sq
import db_connector

app = Flask(__name__)

keys = db_connector.get_db_creds()

app.config['MYSQL_HOST'] = keys["Host"]
app.config['MYSQL_USER'] = keys["User"]
app.config['MYSQL_PASSWORD'] = keys["Password"]
app.config['MYSQL_DB'] = keys["Database"]
app.config['MYSQL_CURSORCLASS'] = keys["Cursor Class"]
app.config['SESSION_TYPE'] = keys["Session Type"]
app.config['SECRET_KEY'] = keys["Secret Key"]
app.config['TEMPLATES_AUTO_RELOAD'] = keys["Templates Auto Reload"]

mysql = MySQL(app)


@app.route("/")
def home():
    """Renders the HTML for the main page of the website.

    Returns:
        Str: The rendered HTML for the main page.
    """
    return render_template('index.j2')


@app.route("/creators", methods=["GET", "POST"])
def creators():
    """
    Renders the HTML for the creators page of the website. If the method is GET
    then the page will be rendered with all creators shown. If the method is
    POST then search results from the page will be used to return a custom
    result.

    Returns:
        Str: The rendered HTML for the creators page.
    """
    cur = mysql.connection.cursor()

    # Get method is used on page load.
    if request.method == "GET":

        # Get headers for the data tables on the Creators page
        header = sq.creators_query_headers()
        cur.execute(header)
        headers = cur.fetchall()

        # Get contents to display in the search table
        search = sq.get_creators_query_results()
        cur.execute(search)
        search_results = cur.fetchall()

        # Get list of Creators to prevent deletion for.
        prevent = sq.prevent_creator_delete()
        cur.execute(prevent)
        prevent_delete = cur.fetchall()

        # Turn dictionary into list of Creator ID's
        prevent_delete = [value for elem in prevent_delete for value in
                          elem.values()]

        return render_template('creators.j2', headers=headers,
                               search_results=search_results,
                               prevent_delete=prevent_delete)

    # Post method is used when a search is performed.
    if request.method == "POST":

        # Get the headers for the data tables in the Creators page
        header = sq.creators_query_headers()
        cur.execute(header)
        headers = cur.fetchall()

        # Get the values that the user entered in the form lookup fields
        creator_id = request.form.get('creator_id_lookup')
        full_name = request.form.get('creator_full_name_lookup')

        # If fields were left blank, use % for easy searching in the DB
        if creator_id == "" or creator_id is None:
            creator_id = "%"
        if full_name == "" or full_name is None:
            full_name = "%"

        # Get the search results to display on the Creators page.
        search_query = sq.post_creators_query_results()
        cur.execute(search_query, (creator_id, full_name))
        search_results = cur.fetchall()

        # Get the list of creators to prevent deletion
        prevent = sq.prevent_creator_delete()
        cur.execute(prevent)
        prevent_delete = cur.fetchall()
        # Convert list of dictionaries to list of Creator ID's
        prevent_delete = [value for elem in prevent_delete for value in
                          elem.values()]

        # If no results are found, show the user a nice message.
        if len(search_results) == 0:
            flash("No search results found.")

        return render_template('creators.j2', headers=headers,
                               search_results=search_results,
                               prevent_delete=prevent_delete)

    # If all those other things fail return the user back ot the homepage
    return render_template('index.j2')


@app.route("/new_creator", methods=["POST"])
def new_creator():
    """Add a new creator.

    Used to send values from the creators page to the database to add a new
    Creator. Once the data is added to the database, the page is redirected
    to the Creators page.

    Returns:
        Str: The rendered HTML for the creators page.
    """
    cur = mysql.connection.cursor()

    # Get the creator name from the form after user submission
    full_name = request.form.get('full_name')
    insert = sq.new_creator_insert_query()

    # Execute insertion query and commit to database
    cur.execute(insert, (full_name,))
    mysql.connection.commit()

    # Reload the page so the user can see the newly added Creator
    return redirect("/creators")


@app.route("/delete_creator/<int:delete_id>", methods=["GET", "POST"])
def delete_creator(delete_id):
    """Delete a creator from the database.

    Returns:
        Str: The rendered HTML for the creators page.
    """

    cur = mysql.connection.cursor()

    # Get the deletion query, and execute deletion
    delete = sq.delete_creator_query()
    cur.execute(delete, (delete_id,))
    mysql.connection.commit()

    # Return to the page and reload to show deleted Creator
    return redirect("/creators")


@app.route("/edit_creator/<int:edit_id>", methods=["POST", "GET"])
def edit_creator(edit_id=None):
    """
    Used to edit the contents of a creator entry in the database. If the
    request method is GET, the contents of the creator entry are loaded into
    the edit page for the user. If the method is POST, then the results of
    the update are sent to the database.

    Args:
        edit_id: The ID of the creator to edit

    Returns:
        Str: The rendered HTML for the creators page.
    """

    cur = mysql.connection.cursor()

    # Get method is used for populating the edit page with details to edit
    if request.method == "GET":

        # Get the headers to display on the edit page
        header = sq.creators_query_headers()
        cur.execute(header)
        headers = cur.fetchall()

        # Get the details for the creator to edit
        find = sq.get_edit_creators_find_query()
        cur.execute(find, (edit_id,))
        creator = cur.fetchall()

        # Display the page to the user.
        return render_template('edit_creator.j2',
                               headers=headers, creator=creator)

    # Post method is used for saving edits to creator object
    if request.method == "POST":

        # Get values from the form fields
        creator_id = request.form.get('edit_creator_id')
        full_name = request.form.get('edit_creator_full_name')

        # Execute and commit update based on user inputs.
        update = sq.post_edit_creators_update_query()
        cur.execute(update, (full_name, creator_id))
        mysql.connection.commit()

        # Return back to creators page to show user edits successful.
        return redirect("/creators")

    # if all else fails, show homepage.
    return render_template("index.j2")


@app.route("/suppliers", methods=["GET", "POST"])
def suppliers():
    """
    Renders the HTML for the suppliers page of the website. If the method is
    GET then the page will be rendered with all suppliers shown. If the method
    is POST then search results from the page will be used to return a custom
    result.

    Returns:
        str: The HTML to render the suppliers page.
    """
    cur = mysql.connection.cursor()

    # Get method used on initial page load.
    if request.method == "GET":

        # Get headers for data tables on suppliers page
        header = sq.suppliers_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get default search results to display in search table
        results = sq.get_suppliers_results_query()
        cur.execute(results)
        search_results = cur.fetchall()

        # Show user the page
        return render_template('suppliers.j2', headers=headers,
                               search_results=search_results)

    # Post method is used when user runs a dynamic query
    if request.method == "POST":

        # Get headers for data tables on suppliers page
        header = sq.suppliers_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get user supplied search values from the form.
        supplier_id = request.form.get('supplier_id_lookup')
        supplier_name = request.form.get('supplier_name_lookup')
        phone_number = request.form.get('supplier_phone_number_lookup')

        # Replace blank or empty values with % for easy searching the DB
        if supplier_id == "" or supplier_id is None:
            supplier_id = "%"
        if supplier_name == "" or supplier_name is None:
            supplier_name = "%"
        if phone_number == "" or phone_number is None:
            phone_number = "%"

        # Get the query and execute with user supplied parameters
        search = sq.post_suppliers_results_query()
        params = (supplier_id, supplier_name, phone_number)
        cur.execute(search, params)
        search_results = cur.fetchall()

        # If the search yields no results, display a nice message to the user.
        if len(search_results) == 0:
            flash("No search results found.")

        # Show the user the results of their search.
        return render_template('suppliers.j2', headers=headers,
                               search_results=search_results)

    return render_template('index.j2')


@app.route("/new_supplier", methods=["GET", "POST"])
def new_supplier():
    """
    Used to send values from the suppliers page to the database to add a new
    Supplier. Once the data is added to the database, the page is redirected
    to the Suppliers page.

    Returns:
        Str: The rendered HTML for the suppliers page.
    """
    cur = mysql.connection.cursor()

    # Get user submitted details from form for new supplier
    supplier_name = request.form.get('supplier_name')
    supplier_address = request.form.get('supplier_address')
    phone_number = request.form.get('phone_number')

    # Get the insert query, execute insert statement and commit to DB
    insert = sq.new_suppliers_insert_query()
    params = (supplier_name, supplier_address, phone_number)

    cur.execute(insert, params)
    mysql.connection.commit()

    # Update the page to show new supplier added.
    return redirect("/suppliers")


@app.route("/delete_supplier/<int:delete_id>", methods=["POST", "GET"])
def delete_supplier(delete_id):
    """Delete a supplier from the database.

    Returns:
        Str: The rendered HTML for the suppliers page.
    """

    # Get delete query, and delete supplier provided in URL
    cur = mysql.connection.cursor()
    delete = sq.delete_suppliers_query()
    cur.execute(delete, (delete_id,))
    mysql.connection.commit()

    # Reload the page to show user that supplier is deleted
    return redirect("/suppliers")


@app.route("/edit_supplier/<int:edit_id>", methods=["POST", "GET"])
def edit_supplier(edit_id=None):
    """
        Used to edit the contents of a supplier entry in the database. If the
        request method is GET, the contents of the supplier entry are loaded
        into the edit page for the user. If the method is POST, then the
        results of the update are sent to the database.

        Args:
            edit_id: The ID of the supplier to edit

        Returns:
            Str: The rendered HTML for the suppliers page.
        """
    cur = mysql.connection.cursor()

    # Get method is used to display the supplier details to the user for editing
    if request.method == "GET":

        # Get data table headers for supplier edit page.
        header = sq.suppliers_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get the details of the supplier to edit
        find = sq.get_edit_suppliers_find_query()
        cur.execute(find, (edit_id,))
        supplier = cur.fetchall()

        # Show the user the page.
        return render_template('edit_supplier.j2', headers=headers,
                               supplier=supplier)

    # Post method is used for saving user edits for suppliers
    if request.method == "POST":

        # Get user entered data from the submitted form
        supplier_id = request.form.get('edit_supplier_id')
        supplier_name = request.form.get('edit_supplier_name')
        supplier_address = request.form.get('edit_supplier_address')
        phone_number = request.form.get('edit_supplier_phone_number')

        # Execute the update query and commit to DB
        params = (supplier_name, supplier_address, phone_number, supplier_id)
        update = sq.post_edit_suppliers_update_query()
        cur.execute(update, params)
        mysql.connection.commit()

        # Reload the page so the user can see the edits were saved
        return redirect("/suppliers")

    return render_template('index.j2')


@app.route("/employees", methods=["GET", "POST"])
def employees():
    """
    Renders the HTML for the employees page of the website. If the method is
    GET then the page will be rendered with all employees shown. If the method
    is POST then search results from the page will be used to return a custom
    result.

    Returns:
        str: The HTML to render the employees page.
    """
    cur = mysql.connection.cursor()

    # Get method for initial page load
    if request.method == "GET":

        # Get headers for employee data tables
        header = sq.employee_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get default search results for employees page
        results = sq.get_employee_results_query()
        cur.execute(results)
        search_results = cur.fetchall()

        # Get list of employees not to be deleted
        restrict = sq.prevent_employee_delete()
        cur.execute(restrict)
        prevent_delete = cur.fetchall()
        # Convert list of dictionaries to list of employee ID's
        prevent_delete = [value for elem in prevent_delete for value in
                          elem.values()]

        # Show the user the page
        return render_template('employees.j2', headers=headers,
                               search_results=search_results,
                               prevent_delete=prevent_delete)

    # Post method used for dynamic user search
    if request.method == "POST":

        # Get the headers for the data tables on the employees page
        header = sq.employee_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get user search values from the form
        employee_id = request.form.get('employee_id_lookup')
        first_name = request.form.get('employee_first_name_lookup')
        last_name = request.form.get('employee_last_name_lookup')
        phone_number = request.form.get('employee_phone_number_lookup')

        # Replace blanks with % for easy DB searches
        if employee_id == "" or employee_id is None:
            employee_id = "%"
        if first_name == "" or first_name is None:
            first_name = "%"
        if last_name == "" or last_name is None:
            last_name = "%"
        if phone_number == "" or phone_number is None:
            phone_number = "%"

        # Find results based on user inputs
        search = sq.post_employee_results_query()
        params = (employee_id, first_name, last_name, phone_number)
        cur.execute(search, params)
        search_results = cur.fetchall()

        # Get list of employess that shouldn't be deleted
        restrict = sq.prevent_employee_delete()
        cur.execute(restrict)
        prevent_delete = cur.fetchall()
        # Convert list of dictionaries to list of employee ID's
        prevent_delete = [value for elem in prevent_delete for value in
                          elem.values()]

        # If no results, display a nice message to the user
        if len(search_results) == 0:
            flash("No search results found.")

        # Show employees page to the user with search results
        return render_template('employees.j2', headers=headers,
                               search_results=search_results,
                               prevent_delete=prevent_delete)

    return render_template('index.j2')


@app.route("/new_employee", methods=["GET", "POST"])
def new_employee():
    """
    Used to send values from the employees page to the database to add a new
    Employee. Once the data is added to the database, the page is redirected
    to the Employees page.

    Returns:
        Str: The rendered HTML for the employee page.
    """
    cur = mysql.connection.cursor()

    # Get user input from form for new employee
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone_number = request.form.get('phone_number')
    address = request.form.get('address')

    # Set phone number to None if it's an empty string for null value in DB
    if phone_number == "" or phone_number is None:
        phone_number = None

    # Get query and execute/commit to database
    insert = sq.new_employee_insert_query()
    params = (first_name, last_name, phone_number, address)

    cur.execute(insert, params)
    mysql.connection.commit()

    # Reload employees page to show new addition
    return redirect("/employees")


@app.route("/delete_employee/<int:delete_id>", methods=["POST", "GET"])
def delete_employee(delete_id):
    """Delete an employee from the database.

    Returns:
        Str: The rendered HTML for the employee page.
    """
    cur = mysql.connection.cursor()

    # Get the deletion query and execute using id from URL
    delete = sq.delete_employee_query()
    cur.execute(delete, (delete_id,))
    mysql.connection.commit()

    # Reload employees page to show employee deletion
    return redirect("/employees")


@app.route("/edit_employee/<int:edit_id>", methods=["POST", "GET"])
def edit_employee(edit_id=None):
    """
    Used to edit the contents of an employee entry in the database. If the
    request method is GET, the contents of the employee entry are loaded
    into the edit page for the user. If the method is POST, then the
    results of the update are sent to the database.

    Args:
        edit_id: The ID of the employee to edit

    Returns:
        Str: The rendered HTML for the Employees page.
    """
    cur = mysql.connection.cursor()

    # Get method used to show details to user for editing employee
    if request.method == "GET":

        # Get headers for data table on employee edit page
        header = sq.employee_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get details about employee to edit.
        find = sq.get_edit_employee_find_query()
        cur.execute(find, (edit_id,))
        employee = cur.fetchall()

        # Show user the page
        return render_template('edit_employee.j2', headers=headers,
                               employee=employee)

    # Post method used to save employee edits
    if request.method == "POST":

        # Get user entered form data
        employee_id = request.form.get('edit_employee_id')
        first_name = request.form.get('edit_employee_first_name')
        last_name = request.form.get('edit_employee_last_name')
        phone_number = request.form.get('edit_employee_phone_number')
        address = request.form.get('edit_employee_address')

        # Set phone number to none if empty string
        if phone_number == "" or phone_number is None:
            phone_number = None

        # Execute and commit update query
        params = (first_name, last_name, phone_number, address, employee_id)
        update = sq.post_edit_employee_update_query()
        cur.execute(update, params)
        mysql.connection.commit()

        # Reload employees page to show user that edits were saved.
        return redirect("/employees")

    return render_template('index.j2')


@app.route("/patrons", methods=["GET", "POST"])
def patrons():
    """
    Renders the HTML for the patrons page of the website. If the method is GET
    then the page will be rendered with all patrons shown. If the method is
    POST then search results from the page will be used to return a custom
    result.

    Returns:
        Str: The rendered HTML for the patrons page.
    """
    cur = mysql.connection.cursor()

    # Get method used on page load
    if request.method == "GET":

        # Get headers for data tables on patrons page
        header = sq.patrons_query_headers()
        cur.execute(header)
        headers = cur.fetchall()

        # Get default search results to display in search table
        search = sq.get_patrons_query_results()
        cur.execute(search)
        search_results = cur.fetchall()

        # Get list of patrons that shouldn't be deleted
        restrict = sq.prevent_patron_delete()
        cur.execute(restrict)
        prevent_delete = cur.fetchall()
        # convert list of dictionaries to list of patron id's
        prevent_delete = [value for elem in prevent_delete for value in
                          elem.values()]

        # Show the patrons page
        return render_template('patrons.j2', headers=headers,
                               search_results=search_results,
                               prevent_delete=prevent_delete)

    # Post method used for dynamic searches
    if request.method == "POST":

        # Get the headers for data tables on patrons page
        header = sq.patrons_query_headers()
        cur.execute(header)
        headers = cur.fetchall()

        # Get user entered search data from form
        patron_id = request.form.get('patron_id_lookup')
        first_name = request.form.get('patron_first_name_lookup')
        last_name = request.form.get('patron_last_name_lookup')
        phone_number = request.form.get('patron_phone_number_lookup')

        # Replace empty string or None with % for easy DB searches
        if patron_id == "" or patron_id is None:
            patron_id = "%"
        if first_name == "" or first_name is None:
            first_name = "%"
        if last_name == "" or last_name is None:
            last_name = "%"
        if phone_number == "" or phone_number is None:
            phone_number = "%"

        # Get search results
        search = sq.post_patrons_query_results()
        params = (patron_id, first_name, last_name, phone_number)
        cur.execute(search, params)
        search_results = cur.fetchall()

        # Get list of patrons that shouldn't be deleted
        restrict = sq.prevent_patron_delete()
        cur.execute(restrict)
        prevent_delete = cur.fetchall()
        # Convert list of dictionaries to list of patron id's
        prevent_delete = [value for elem in prevent_delete for value in
                          elem.values()]

        # If no results, display nice message to user
        if len(search_results) == 0:
            flash("No search results found.")

        # Show user page with search results
        return render_template('patrons.j2', headers=headers,
                               search_results=search_results,
                               prevent_delete=prevent_delete)

    return render_template('index.j2')


@app.route("/new_patron", methods=["POST"])
def new_patron():
    """Add a new patron.

    Used to send values from the patrons page to the database to add a new
    Patron. Once the data is added to the database, the page is redirected
    to the Patrons page.

    Returns:
        Str: The rendered HTML for the patrons page.
    """
    cur = mysql.connection.cursor()

    # Get new patron data from form
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone_number = request.form.get('phone_number')
    fine_amount = request.form.get('fine_amount')
    address = request.form.get('address')

    # allow fine to be null, set to None if empty string
    if fine_amount == "" or fine_amount is None:
        fine_amount = None

    # Get insert query and execute/commit to DB
    insert = sq.new_patrons_insert_query()
    params = (first_name, last_name, phone_number, fine_amount, address)
    cur.execute(insert, params)
    mysql.connection.commit()

    # Reload patrons page to show user new patron added
    return redirect("/patrons")


@app.route("/delete_patron/<int:delete_id>", methods=["GET", "POST"])
def delete_patron(delete_id):
    """Delete a patron from the database.

    Returns:
        Str: The rendered HTML for the patrons page.
    """

    cur = mysql.connection.cursor()

    # Get delete query and delete patron id from URL
    delete = sq.delete_patrons_query()
    cur.execute(delete, (delete_id,))
    mysql.connection.commit()

    # Reload patrons page to show patron deletion to user
    return redirect("/patrons")


@app.route("/edit_patron/<int:edit_id>", methods=["POST", "GET"])
def edit_patron(edit_id=None):
    """
    Used to edit the contents of a patron entry in the database. If the
    request method is GET, the contents of the patron entry are loaded into
    the edit page for the user. If the method is POST, then the results of
    the update are sent to the database.

    Args:
        edit_id: The ID of the patron to edit

    Returns:
        Str: The rendered HTML for the patrons page.
    """
    cur = mysql.connection.cursor()

    # Get method used to display patron details for editing
    if request.method == "GET":

        # Get headers for patron editing data tables
        header = sq.patrons_query_headers()
        cur.execute(header)
        headers = cur.fetchall()

        # Get details about patron to edit
        find = sq.get_edit_patrons_find_query()
        cur.execute(find, (edit_id,))
        patron = cur.fetchall()

        # Display page to user
        return render_template('edit_patron.j2',
                               headers=headers, patron=patron)

    # Post method used for saving patron edits
    if request.method == "POST":

        # Get user entered data from form
        patron_id = request.form.get('edit_patron_id')
        first_name = request.form.get('edit_patron_first_name')
        last_name = request.form.get('edit_patron_last_name')
        phone_number = request.form.get('edit_patron_phone_number')
        fine_amount = request.form.get('edit_patron_fine_amount')
        address = request.form.get('edit_patron_address')

        # Allow fine to be null
        if fine_amount == "" or fine_amount is None:
            fine_amount = None

        # Get update query and execute/commit to DB
        update = sq.post_edit_patrons_update_query()
        params = (first_name, last_name, phone_number, fine_amount, address,
                  patron_id)
        cur.execute(update, params)
        mysql.connection.commit()

        # Reload patrons page to show user edits saved successfully
        return redirect("/patrons")

    return render_template("index.j2")


@app.route("/media_items", methods=["GET", "POST"])
def media_items():
    """
    Renders the HTML for the media items page of the website. If the method is
    GET then the page will be rendered with all items shown. If the method
    is POST then search results from the page will be used to return a custom
    result.

    Returns:
        str: The HTML to render the media items page.
    """
    cur = mysql.connection.cursor()

    # Get method used for initial page load
    if request.method == "GET":

        # Get headers for media items data tables
        header = sq.media_items_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get default search results
        search = sq.get_media_items_results_query()
        cur.execute(search)
        search_results = cur.fetchall()

        # Get list of supplier information for use in dropdowns
        get_supplier_ids = sq.get_supplier_ids_query()
        cur.execute(get_supplier_ids)
        supp_ids = cur.fetchall()

        # Get list of creator information for use in dropdowns
        get_creator_ids = sq.get_creator_ids_query()
        cur.execute(get_creator_ids)
        creator_ids = cur.fetchall()

        # Get list of items that shouldn't be deleted
        prevent = sq.prevent_item_delete()
        cur.execute(prevent)
        prevent_delete = cur.fetchall()
        # Convert list of dictionaries to list of item ids
        prevent_delete = [value for elem in prevent_delete for value in
                          elem.values()]


        # List of options for media types for dropdowns
        media_types = (
                {"Media Type": "", "Display": "-- Select Media Type --"},
                {"Media Type": "Book", "Display": "Book"},
                {"Media Type": "Magazine", "Display": "Magazine"},
                {"Media Type": "Movie", "Display": "Movie"},
                {"Media Type": "Music", "Display": "Music"})

        # Show page to user
        return render_template('media_items.j2', headers=headers,
                               search_results=search_results, supp_ids=supp_ids,
                               creator_ids=creator_ids, media_types=media_types,
                               prevent_delete=prevent_delete)

    # Post method is used for dynamic search results
    if request.method == "POST":

        # Get data table headers for media items page
        header = sq.media_items_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get user entered search data from form
        item_id = request.form.get('media_item_id_lookup')
        media_type = request.form.get('media_type_lookup')
        supplier_id = request.form.get('media_supplier_id_lookup')
        title = request.form.get('title_lookup')
        creator_id = request.form.get('media_creator_id_lookup')

        # Replace blanks with % for easy DB searching
        if item_id == "" or item_id is None:
            item_id = "%"
        if media_type == "" or media_type is None:
            media_type = "%"
        if supplier_id == "" or supplier_id is None:
            supplier_id = "%"
        if title == "" or title is None:
            title = "%"
        if creator_id == "" or creator_id is None:
            creator_id = "%"

        # Get dynamic search results
        search = sq.post_media_items_search_query()
        params = (item_id, media_type, supplier_id, supplier_id,
                 title, creator_id, creator_id)
        cur.execute(search, params)
        search_results = cur.fetchall()

        # Get supplier data for dropdowns
        get_supplier_ids = sq.get_supplier_ids_query()
        cur.execute(get_supplier_ids)
        supp_ids = cur.fetchall()

        # Get creator data for dropdowns
        get_creator_ids = sq.get_creator_ids_query()
        cur.execute(get_creator_ids)
        creator_ids = cur.fetchall()

        # Get list of items that shouldn't be deleted
        prevent = sq.prevent_item_delete()
        cur.execute(prevent)
        prevent_delete = cur.fetchall()
        # Convert list of dictionaries to list of item id's
        prevent_delete = [value for elem in prevent_delete for value in
                          elem.values()]

        # if search yields no results, display nice message to user
        if len(search_results) == 0:
            flash("No search results found.")

        # list of media types for dropdowns.
        media_types = (
                {"Media Type": "", "Display": "-- Select Media Type --"},
                {"Media Type": "Book", "Display": "Book"},
                {"Media Type": "Magazine", "Display": "Magazine"},
                {"Media Type": "Movie", "Display": "Movie"},
                {"Media Type": "Music", "Display": "Music"})

        # Show dynamic search results to user
        return render_template('media_items.j2', headers=headers,
                               search_results=search_results, supp_ids=supp_ids,
                               creator_ids=creator_ids, media_types=media_types,
                               prevent_delete=prevent_delete)

    return render_template('index.j2')

@app.route("/new_media_item", methods=["GET", "POST"])
def new_media_item():
    """
    Used to send values from the media items page to the database to add a new
    media item. Once the data is added to the database, the page is redirected
    to the media items page.

    Returns:
        Str: The rendered HTML for the media items page.
    """
    cur = mysql.connection.cursor()

    # Get user data from form for new media item
    media_type = request.form.get('media_type')
    supplier_id = request.form.get('supplier_id')
    title = request.form.get('title')
    creator_id = request.form.get('creator_id')
    release_date = request.form.get('release_date')
    replacement_cost = request.form.get('replacement_cost')
    quantity_owned = request.form.get('quantity_owned')

    # allow supplier id to be null
    if supplier_id == "" or supplier_id is None:
        supplier_id = None

    # allow replacement cost to be null
    if replacement_cost == "" or replacement_cost is None:
        replacement_cost = None

    # Get insert query, execute, commit to DB
    insert = sq.new_media_item_insert_query()
    params = (media_type, supplier_id, title, creator_id, release_date,
              replacement_cost, quantity_owned)
    cur.execute(insert, params)
    mysql.connection.commit()

    # Reload media items page to show user newly added item
    return redirect("/media_items")

@app.route("/delete_media_item/<int:delete_id>", methods=["POST", "GET"])
def delete_media_item(delete_id):
    """Delete a media item from the database.

    Returns:
        Str: The rendered HTML for the media items page.
    """
    cur = mysql.connection.cursor()

    # Get delete query and delete item from URL
    delete_query = sq.delete_media_item_query()
    cur.execute(delete_query, (delete_id,))
    mysql.connection.commit()

    # Reload media items page to show user item deletion successful
    return redirect("/media_items")

@app.route("/edit_media_item/<int:edit_id>", methods=["POST", "GET"])
def edit_media_item(edit_id=None):
    """
        Used to edit the contents of a media item entry in the database. If the
        request method is GET, the contents of the media item entry are loaded
        into the edit page for the user. If the method is POST, then the
        results of the update are sent to the database.

        Args:
            edit_id: The ID of the media item to edit

        Returns:
            Str: The rendered HTML for the Media Items page.
        """
    cur = mysql.connection.cursor()

    # Get method used to load media item details for editing
    if request.method == "GET":

        # Get headers for edit page data table
        header = sq.media_items_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get media item details for user to see and edit
        find = sq.edit_media_item_find_query()
        cur.execute(find, (edit_id,))
        item = cur.fetchall()

        # get supplier data for dropdowns
        get_supplier_ids = sq.get_supplier_ids_query()
        cur.execute(get_supplier_ids)
        supp_ids = cur.fetchall()

        # get creator data from dropdowns
        get_creator_ids = sq.get_creator_ids_query()
        cur.execute(get_creator_ids)
        creator_ids = cur.fetchall()

        # media types for dropdowns
        media_types = (
                {"Media Type": "", "Display": "-- Select Media Type --"},
                {"Media Type": "Book", "Display": "Book"},
                {"Media Type": "Magazine", "Display": "Magazine"},
                {"Media Type": "Movie", "Display": "Movie"},
                {"Media Type": "Music", "Display": "Music"})

        # show media item to edit to user
        return render_template('edit_media_item.j2', headers=headers,
                               item=item, supp_ids=supp_ids,
                               creator_ids=creator_ids,
                               media_types=media_types)

    # Post method used for saving user edits to media item
    if request.method == "POST":

        # Get user data from form
        item_id = request.form.get('item_id')
        media_type = request.form.get('media_type')
        supplier_id = request.form.get('supplier_id')
        title = request.form.get('title')
        creator_id = request.form.get('creator_id')
        release_date = request.form.get('release_date')
        replacement_cost = request.form.get('replacement_cost')
        quantity_owned = request.form.get('quantity_owned')

        # allow supplier ID to be null
        if supplier_id == "" or supplier_id is None:
            supplier_id = None

        # allow replacement cost to be null
        if replacement_cost == "" or replacement_cost is None:
            replacement_cost = None

        # Get update query, execute, and commit to DB
        params = (media_type, supplier_id, title, creator_id, release_date,
                  replacement_cost, quantity_owned, item_id)
        update = sq.post_edit_media_item_query()
        cur.execute(update, params)
        mysql.connection.commit()

        # reload page to show edits successful
        return redirect("/media_items")

    return render_template('index.j2')


@app.route("/media_transactions", methods=["GET", "POST"])
def media_transactions():
    """Displays the media transactions page.

    Returns:
        str: The rendered HTML for the media transactions page.
    """
    cur = mysql.connection.cursor()

    # Get method used for initial page load
    if request.method == "GET":

        # Get headers for media transactions data tables
        header = sq.media_transactions_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get default search results (only items currently checked out)
        search = sq.get_media_transactions_all_checkouts_query()
        cur.execute(search)
        search_results = cur.fetchall()

        # Get patron data for dropdowns
        patron_id = sq.get_patron_ids_query()
        cur.execute(patron_id)
        patron_ids = cur.fetchall()

        # Get employee data for dropdowns
        employee_query = sq.get_employee_ids_query()
        cur.execute(employee_query)
        employee_ids = cur.fetchall()

        # Get item data for dropdowns
        item_query = sq.get_items_query()
        cur.execute(item_query)
        items = cur.fetchall()

        # List of transaction types
        types = (
                 {"Type": "", "Display": "-- Select Transaction Type --"},
                 {"Type": "checkin", "Display": "Checkin"},
                 {"Type": "checkout", "Display": "Checkout"})

        # Show user media transactions page
        return render_template('media_transactions.j2', headers=headers,
                               search_results=search_results,
                               patron_ids=patron_ids, employee_ids=employee_ids,
                               transaction_types=types, items=items)

    # Post method used for dynamic search
    if request.method == "POST":

        # Get search results from form submission
        patron_id = request.form.get("transaction_patron_id_lookup")
        employee_id = request.form.get('transaction_employee_id_lookup')
        transaction_type = request.form.get('transaction_type_lookup')
        item_id = request.form.get('transaction_item_id_lookup')
        transaction_date = request.form.get('transaction_date_lookup')
        get_history = request.form.get('get_all_history')
        # Used for date range for search.
        next_day = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

        # convert blanks to % for easy DB searches
        if patron_id == "" or patron_id is None:
            patron_id = "%"
        if employee_id == "" or employee_id is None:
            employee_id = "%"
        if transaction_type == "" or transaction_type is None:
            transaction_type = "%"
        if item_id == "" or item_id is None:
            item_id = "%"
        # Set transaction date to date before business started
        if transaction_date == "" or transaction_date is None:
            transaction_date = "1970-01-01 00:00:01"
        # If user enters date, add one day to next day for a 1 day range
        else:
            transaction_date = datetime.strptime(transaction_date,
                                                 "%Y-%m-%d")
            next_day = transaction_date + timedelta(days=1)
            transaction_date = datetime.strftime(transaction_date,
                                                 "%Y-%m-%d %H:%M:%S")
            next_day = datetime.strftime(next_day,
                                         "%Y-%m-%d %H:%M:%S")

        # get data table headers for media transactions page
        header = sq.media_transactions_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # Get patron data for dropdowns
        patron_id_query = sq.get_patron_ids_query()
        cur.execute(patron_id_query)
        patron_ids = cur.fetchall()

        # Get employee data for dropdowns
        employee_query = sq.get_employee_ids_query()
        cur.execute(employee_query)
        employee_ids = cur.fetchall()

        # Get item data for dropdowns
        item_query = sq.get_items_query()
        cur.execute(item_query)
        items = cur.fetchall()

        # If a user searches for checkins, show all history since checkins will
        # be filtered out by default
        if transaction_type == "checkin":
            get_history = "on"

        # Get a different query if the user wants all history
        if get_history == "on":
            search = sq.get_all_media_transactions_custom_query()
        else:
            search = sq.post_media_transactions_checkouts_custom_query()

        # Execute wildly complicated search...
        params = (patron_id, patron_id, patron_id, patron_id, employee_id,
                  employee_id, employee_id, employee_id, transaction_type,
                  item_id, item_id, transaction_date, next_day)

        cur.execute(search, params)
        search_results = cur.fetchall()

        # If no results, display nice message to user
        if len(search_results) == 0:
            flash("No search results found.")

        # list of transaction types for dropdowns
        types = (
                 {"Type": "", "Display": "-- Select Transaction Type --"},
                 {"Type": "checkin", "Display": "Checkin"},
                 {"Type": "checkout", "Display": "Checkout"})

        # Show user dynamic search results
        return render_template('media_transactions.j2', headers=headers,
                               search_results=search_results,
                               patron_ids=patron_ids, employee_ids=employee_ids,
                               transaction_types=types, items=items)

    return render_template('media_transactions.j2')


@app.route("/new_media_transaction", methods=["GET", "POST"])
def new_media_transaction():
    """
    Used to send values from the media transactions page to the database to
    add a new media transaction. Once the data is added to the database, the
    page is redirected to the media transactions page.

    Returns:
        Str: The rendered HTML for the media transactions page.
    """
    cur = mysql.connection.cursor()

    # Get user data from form for new media transaction
    patron_id = request.form.get('patron_id')
    transaction_type = request.form.get('transaction_type')
    employee_id = request.form.get('employee_id')
    item_id = request.form.get('item_id')
    # generate a transaction datetime stamp
    transaction_date = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')

    # Get insert query, execute, and commit to DB
    insert = sq.new_media_transaction_insert_query()
    params = (patron_id, transaction_type, employee_id, item_id,
              transaction_date)

    cur.execute(insert, params)
    mysql.connection.commit()

    # Reload the page so new media transaction is shown to user
    return redirect("/media_transactions")

@app.route("/edit_media_transaction/<int:edit_id>", methods=["POST", "GET"])
def edit_media_transaction(edit_id=None):
    """
    Used to edit the contents of a media transaction entry in the database.
    If the request method is GET, the contents of the media transaction
    entry are loaded into the edit page for the user. If the method is
    POST, then the results of the update are sent to the database.

    Args:
        edit_id: The ID of the media transaction to edit

    Returns:
        Str: The rendered HTML for the media transactions page.
    """
    cur = mysql.connection.cursor()

    # get method used to show edit details to user
    if request.method == "GET":

        # get data table headers for editing media transaction
        header = sq.media_transactions_header_query()
        cur.execute(header)
        headers = cur.fetchall()

        # get patron data for dropdowns
        patron_id = sq.get_patron_ids_query()
        cur.execute(patron_id)
        patron_ids = cur.fetchall()

        # get employee data for dropdowns
        employee_query = sq.get_employee_ids_query()
        cur.execute(employee_query)
        employee_ids = cur.fetchall()

        # get item data for dropdowns
        item_query = sq.get_items_query()
        cur.execute(item_query)
        items = cur.fetchall()

        # find details about media transaction to edit
        find = sq.edit_media_transaction_find_query()
        cur.execute(find, (edit_id,))
        transaction = cur.fetchall()

        # list of transaction types for dropdowns
        types = (
                 {"Type": "", "Display": "-- Select Transaction Type --"},
                 {"Type": "checkin", "Display": "Checkin"},
                 {"Type": "checkout", "Display": "Checkout"})

        # Show user details about media transaction to edit
        return render_template('edit_media_transaction.j2', headers=headers,
                               transaction=transaction, patron_ids=patron_ids,
                               employee_ids=employee_ids,
                               transaction_types=types, items=items)

    # post method used for saving media transaction edits
    if request.method == "POST":

        # get user entered form data
        patron_id = request.form.get('edit_patron_id')
        transaction_type = request.form.get('edit_transaction_type')
        employee_id = request.form.get('edit_employee_id')
        item_id = request.form.get('edit_item_id')

        # Update the transaction details
        params = (patron_id, transaction_type, employee_id, item_id,
                  edit_id)
        update = sq.post_edit_media_transaction_update_query()
        cur.execute(update, params)
        mysql.connection.commit()

        # reload page to show user edits saved
        return redirect("/media_transactions")

    return render_template('index.j2')

@app.route("/delete_media_transaction/<int:delete_id>", methods=["POST", "GET"])
def delete_media_transaction(delete_id):
    """Delete a media transaction from the database.

    Returns:
        Str: The rendered HTML for the media transaction page.
    """
    cur = mysql.connection.cursor()
    # get deletion query and delete id of media transaction from url
    delete = sq.delete_media_transaction_query()
    cur.execute(delete, (delete_id,))
    mysql.connection.commit()

    # Reload the page to show transaction deletion
    return redirect("/media_transactions")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 53266))

    app.run(debug=True, port=port)
