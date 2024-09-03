import os

# Define a function to create a multiplication table and save it to a file
def generate_table(n):
    # Build the multiplication table for the number `n`
    tables = ""
    for i in range(1, 11):
        tables += f"{n} x {i} = {n * i}\n"
    
    # Ensure the 'tables' Folder exists
    os.makedirs("tables", exist_ok=True)
    
    # Save the table content to a file named 'tables_n.txt' inside the 'tables' folder
    with open(f"tables/tables_{n}.txt", "w") as file:
        file.write(tables)
        
# Generate multiplication tables for numbers from 1 to 20
for i in range(1, 21):
    generate_table(i)


