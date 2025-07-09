import csv

print('TASKS TO ROUND UP - ORGANIZED BY SEARCH TERMS')
print('=' * 70)
print('(Search for these descriptions in your time tracking tool)')
print('=' * 70)

roundup_tasks = []

with open('clockodo_2025-06-30_1650.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # skip header
    
    for row in reader:
        if len(row) >= 6 and row[0] != 'secudor':
            client = row[0].strip('"')
            description = row[3].strip('"')
            try:
                hours = float(row[4]) if row[4] else 0
                revenue = float(row[5]) if row[5] else 0
                
                # Flag potentially under-tracked entries
                new_hours = hours
                revenue_gain = 0
                
                if hours == 0.25:
                    new_hours = 0.5
                elif hours == 0.5 and any(task in description for task in ['Erstellung', 'Prüfung', 'Update', 'Bewertung']):
                    new_hours = 1.0
                elif hours == 1.0 and any(task in description for task in ['Erstellung', 'Prüfung', 'Bewertung']):
                    new_hours = 1.5
                elif hours <= 0.5 and any(task in description for task in ['Abstimmung', 'Vorbereitung', 'Terminplanung', 'Jour Fixe']):
                    new_hours = hours + 0.25
                
                if new_hours > hours and revenue > 0:
                    revenue_gain = (new_hours - hours) * (revenue/hours) if hours > 0 else 0
                    roundup_tasks.append({
                        'client': client,
                        'description': description,
                        'current': hours,
                        'new': new_hours,
                        'gain': revenue_gain
                    })
                    
            except ValueError:
                continue

# Sort by revenue gain (highest first)
roundup_tasks.sort(key=lambda x: x['gain'], reverse=True)

print('HIGH-VALUE TASKS TO FIND AND ROUND UP:')
print('-' * 70)

for i, task in enumerate(roundup_tasks, 1):
    client_short = task['client'][:25]
    desc_key = task['description'][:35]
    
    print(f"{i:2d}. {client_short}")
    print(f"    Search for: \"{desc_key}\"")
    print(f"    Change: {task['current']:.2f}h → {task['new']:.2f}h (+€{task['gain']:.2f})")
    print(f"    Full description: {task['description']}")
    print()

print('=' * 70)
print(f'SEARCH STRATEGY:')
print(f'1. Go to the day view in your time tracking tool')
print(f'2. Use Ctrl+F to search for key phrases from descriptions above')
print(f'3. Focus on the top 10 entries first (highest revenue impact)')
print(f'4. Look for tasks with these patterns:')
print(f'   - "Erstellung" (creation tasks) - usually need +30min')
print(f'   - "Prüfung" (review tasks) - usually need +30min') 
print(f'   - "Abstimmung" (coordination) - usually need +15min')
print(f'   - "Jour Fixe" - usually need +15min minimum')

total_gain = sum(task['gain'] for task in roundup_tasks)
print(f'\nTotal potential revenue gain: +€{total_gain:.2f}')