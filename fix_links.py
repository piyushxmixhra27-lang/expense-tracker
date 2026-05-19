import os
import re

template_dir = 'templates'
files = [f for f in os.listdir(template_dir) if f.endswith('.html')]

links = [
    (r'<span class="material-symbols-outlined.*?>dashboard</span>\s*<span.*?>Dashboard</span>\s*</a>', 'dashboard'),
    (r'<span class="material-symbols-outlined.*?>payments</span>\s*<span.*?>Transactions</span>\s*</a>', 'transactions'),
    (r'<span class="material-symbols-outlined.*?>account_balance_wallet</span>\s*<span.*?>Budgets</span>\s*</a>', 'budget'),
    (r'<span class="material-symbols-outlined.*?>insights</span>\s*<span.*?>Analytics</span>\s*</a>', 'analytics'),
    (r'<span class="material-symbols-outlined.*?>description</span>\s*<span.*?>Reports</span>\s*</a>', 'reports'),
    (r'<span class="material-symbols-outlined.*?>logout</span>\s*<span.*?>Logout</span>\s*</a>', 'logout')
]

for filename in files:
    filepath = os.path.join(template_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will look for <a href="#"> that contains the specific icons/text
    for pattern, route in links:
        # Regex to find the <a> tag wrapping the spans
        # This regex is a bit complex. We can use a simpler approach.
        pass
    
    # Simpler approach:
    # Replace `<a class="..." href="#">\n<span class="material-symbols-outlined">dashboard</span>`
    # We will just replace `href="#"` with `href="{{ url_for('route') }}"` based on the span following it.
    
    lines = content.split('\n')
    for i in range(len(lines)):
        if '<a ' in lines[i] and 'href="#"' in lines[i]:
            # Look at next lines to find which link it is
            text = " ".join(lines[i:i+4])
            if '>Dashboard<' in text:
                lines[i] = lines[i].replace('href="#"', 'href="{{ url_for(\'dashboard\') }}"')
            elif '>Transactions<' in text:
                lines[i] = lines[i].replace('href="#"', 'href="{{ url_for(\'transactions\') }}"')
            elif '>Budgets<' in text:
                lines[i] = lines[i].replace('href="#"', 'href="{{ url_for(\'budget\') }}"')
            elif '>Analytics<' in text:
                lines[i] = lines[i].replace('href="#"', 'href="{{ url_for(\'analytics\') }}"')
            elif '>Reports<' in text:
                lines[i] = lines[i].replace('href="#"', 'href="{{ url_for(\'reports\') }}"')
            elif '>Logout<' in text:
                lines[i] = lines[i].replace('href="#"', 'href="{{ url_for(\'logout\') }}"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        
print("Links updated successfully!")
