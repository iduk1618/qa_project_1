from utils.web_utils import open_page
from utils.db_utils import execute_query

def main():
    print("Dobrodošli u QA Automation projekat!")
    # Primer korišćenja funkcija iz utils modula
    query = "SELECT * FROM users"
    result = execute_query(query)
    print(result)

if __name__ == "__main__":
    main()