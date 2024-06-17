import pyodbc
from kv_secrets import get_secret

connection_string = get_secret("cwwebapp-herc-extension")


print(connection_string)

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

# Assuming the stored procedure takes an integer parameter @DaysUntilAgreementEnds
days_until_agreement_ends = 120

# Execute the stored procedure with the parameter
cursor.execute("{CALL usp_Get_Eligible_Renewal_Agreements_Excluded_From_Automation (?)}", (days_until_agreement_ends,))

# Fetch the results
results = cursor.fetchall()

# Iterate through the results and print them
for row in results:
    print(row)

# Don't forget to close the cursor and connection when done
cursor.close()
conn.close()