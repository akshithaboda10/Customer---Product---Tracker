# Customer-Product-Tracker
A simple Streamlit dashboard to track customer-product transactions.
The project is beginner-friendly and built using basic Python and a CSV file as a data source. It helped me learn about data handling, visualizations, and creating dashboards with Streamlit.

---

## Features

    - View all customer transactions in one place.
    - Filter by customer name.
    - Check product details like tyre size, quantity, etc..
    - See payment status (Paid / Due).
    - Calculate most common tyre size, total quantity sold, and other simple stats.

---

## Project Structure

    Customer-Product-Tracker/
    ├── streamlit_env
    ├── .gitignore
    ├── app.py # Streamlit app code
    ├── README.md
    ├── requirements.txt # Python libraries needed  
    ├── streamlit_CPT.gif
    ├── VSD_purchases.csv # Data file with customer purchase details
    
---

##  How to Run the App

    -> Make sure Python and Streamlit are installed.
    -> Install dependencies
       pip install -r requirements.txt
    -> Run the Streamlit app
       streamlit run app.py

---

## Sample CSV Columns
 
  The data file (VSD_purchases.csv) should have columns like:
   - Customer Name
   - Product
   - Tyre Size
   - Quantity
   - Payment Status
   - Date

---

## What I Learned

   - How to work with CSV files in Python
   - How to use Pandas for data filtering and stats
   - How to build simple dashboards using Streamlit
   - How to display tables, filters, and charts in a web app

---

## Screenrecord (gif)

   Here’s a quick look at the app in action:
   [demo](streamlit_CPT.gif)


## Future Improvements
    - Add editing options to update payment status.
    - Store data in a database instead of CSV.
    - Add charts and visualizations (bar chart, pie chart, etc.)
