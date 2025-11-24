Companies = ["ADP","TCS","WIPRO"]
'''
for names in Companies:
    if 'A' in names:
        print(names)
    else:
        print("No matching not found")
'''

print("=== With numbers ===")
for i, company in enumerate(Companies, start=1):
    print(f"{i}. {company}")
