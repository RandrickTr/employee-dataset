import csv
from collections import defaultdict

def clean_employee_data():
    input_file = 'Employee.csv'
    output_file = 'Employee_Cleaned.csv'
    
    print("=" * 50)
    print("EMPLOYEE DATA CLEANING TOOL")
    print("=" * 50)
    
    # Read CSV
    print("\n[1/5] Reading data...")
    rows = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        print(f"✓ Loaded {len(rows)} rows")
    except FileNotFoundError:
        print(f"✗ Error: {input_file} not found!")
        return
    
    initial_count = len(rows)
    
    # Remove duplicates
    print("\n[2/5] Removing duplicates...")
    seen = set()
    unique_rows = []
    for row in rows:
        row_str = str(sorted(row.items()))
        if row_str not in seen:
            seen.add(row_str)
            unique_rows.append(row)
    duplicates = len(rows) - len(unique_rows)
    print(f"✓ Removed {duplicates} duplicate rows")
    rows = unique_rows
    
    # Clean and standardize
    print("\n[3/5] Standardizing data...")
    cleaned = []
    for row in rows:
        # Check for empty values
        if any(v.strip() == '' for v in row.values()):
            continue
        
        # Standardize text fields
        row['Education'] = row['Education'].strip().title()
        row['City'] = row['City'].strip().title()
        row['Gender'] = row['Gender'].strip().capitalize()
        row['EverBenched'] = row['EverBenched'].strip().capitalize()
        
        cleaned.append(row)
    
    print(f"✓ Removed {len(rows) - len(cleaned)} rows with missing values")
    rows = cleaned
    
    # Validate and remove outliers
    print("\n[4/5] Validating numeric data...")
    valid_rows = []
    invalid = 0
    
    for row in rows:
        try:
            year = int(row['JoiningYear'])
            age = int(row['Age'])
            tier = int(row['PaymentTier'])
            exp = int(row['ExperienceInCurrentDomain'])
            leave = int(row['LeaveOrNot'])
            
            # Validate ranges
            if not (2012 <= year <= 2018): 
                invalid += 1
                continue
            if not (18 <= age <= 70): 
                invalid += 1
                continue
            if tier not in [1, 2, 3]: 
                invalid += 1
                continue
            if not (0 <= exp <= 5): 
                invalid += 1
                continue
            if leave not in [0, 1]: 
                invalid += 1
                continue
            
            # Validate categories
            if row['Education'] not in ['Bachelors', 'Masters', 'Phd']: 
                invalid += 1
                continue
            if row['City'] not in ['Bangalore', 'Pune', 'New Delhi']: 
                invalid += 1
                continue
            if row['Gender'] not in ['Male', 'Female']: 
                invalid += 1
                continue
            if row['EverBenched'] not in ['Yes', 'No']: 
                invalid += 1
                continue
            
            valid_rows.append(row)
        except:
            invalid += 1
    
    print(f"✓ Removed {invalid} rows with invalid data")
    rows = valid_rows
    
    # Save cleaned data
    print("\n[5/5] Saving cleaned data...")
    if rows:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"✓ Saved to {output_file}")
    
    # Summary
    print("\n" + "=" * 50)
    print("CLEANING SUMMARY")
    print("=" * 50)
    print(f"Original rows:  {initial_count}")
    print(f"Cleaned rows:   {len(rows)}")
    print(f"Removed:        {initial_count - len(rows)}")
    print("=" * 50)
    
    # Show value counts
    if rows:
        print("\nEDUCATION:")
        ed = defaultdict(int)
        for r in rows:
            ed[r['Education']] += 1
        for k, v in sorted(ed.items()):
            print(f"  {k}: {v}")
        
        print("\nCITY:")
        ct = defaultdict(int)
        for r in rows:
            ct[r['City']] += 1
        for k, v in sorted(ct.items()):
            print(f"  {k}: {v}")
        
        print("\nGENDER:")
        gn = defaultdict(int)
        for r in rows:
            gn[r['Gender']] += 1
        for k, v in sorted(gn.items()):
            print(f"  {k}: {v}")
        
        print("\nPAYMENT TIER:")
        pt = defaultdict(int)
        for r in rows:
            pt[r['PaymentTier']] += 1
        for k, v in sorted(pt.items()):
            print(f"  Tier {k}: {v}")

if __name__ == '__main__':
    clean_employee_data()
