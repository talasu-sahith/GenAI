# we can call functions inside another function. refer below

def fetchSalesdata():
    print("Fetching Sales data")

def filterData():
    print("Data has been filtered")

def summarize_the_data():
    print("Data summary")

def generate_report():
    fetchSalesdata()
    filterData()
    summarize_the_data()
    print("report has been generated")

generate_report()