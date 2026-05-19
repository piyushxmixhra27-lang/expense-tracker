import os

template_dir = 'templates'
files = [f for f in os.listdir(template_dir) if f.endswith('.html')]

for filename in files:
    filepath = os.path.join(template_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all dollar signs with rupee signs
    new_content = content.replace('$', '₹')
    
    # Check if there were any changes to avoid unnecessary writes
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

print("Currency conversion to Rupees completed!")
