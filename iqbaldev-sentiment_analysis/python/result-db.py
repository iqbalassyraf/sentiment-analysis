import sqlite3
import pandas as pd

# Load the analysis results
results_df = pd.read_csv('analysis_results.csv')

# Connect to SQLite database (or create it)
conn = sqlite3.connect('analysis_results.db')

# Store the results in a table
results_df.to_sql('feedback_analysis', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
print("Results stored in analysis_results.db")