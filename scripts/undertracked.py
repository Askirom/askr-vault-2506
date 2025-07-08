import csv

print('POTENTIALLY UNDER-TRACKED ENTRIES (could reasonably round up):')
print('=' * 80)

# Categories of tasks that often take longer than tracked
complex_tasks = ['Erstellung', 'Prüfung', 'Update', 'Bewertung', 'Durchführung']
coordination_tasks = ['Abstimmung', 'Vorbereitung', 'Terminplanung', 'Jour Fixe']

roundup_candidates = []

with open('clockodo_2025-06-30_1650.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # skip header
    
    for row in reader:
        if len(row) >= 6 and row[0] != 'secudor':
            client = row[0].strip('"')
            project = row[1].strip('"')
            description = row[3].strip('"')
            try:
                hours = float(row[4]) if row[4] else 0
                revenue = float(row[5]) if row[5] else 0
                
                # Flag potentially under-tracked entries
                flag = False
                potential_add = 0
                reason = ""
                
                # 15-30 min tasks (likely took longer)
                if hours == 0.25:
                    flag = True
                    potential_add = 0.25  # Round to 0.5h
                    reason = "15min tasks usually take 30min"
                
                # 30 min complex tasks
                elif hours == 0.5 and any(task in description for task in complex_tasks):
                    flag = True
                    potential_add = 0.5  # Round to 1h
                    reason = "Complex tasks rarely take only 30min"
                
                # 1h creation/review tasks (often take 1.5h)
                elif hours == 1.0 and any(task in description for task in ['Erstellung', 'Prüfung', 'Bewertung']):
                    flag = True
                    potential_add = 0.5  # Round to 1.5h
                    reason = "Creation/review tasks often need extra time"
                
                # Short coordination tasks
                elif hours <= 0.5 and any(task in description for task in coordination_tasks):
                    flag = True
                    potential_add = 0.25  # Add 15min
                    reason = "Coordination includes prep/followup time"
                
                if flag and revenue > 0:  # Only paying clients
                    roundup_candidates.append({
                        'client': client,
                        'hours': hours,
                        'description': description,
                        'potential_add': potential_add,
                        'reason': reason,
                        'revenue_impact': potential_add * (revenue/hours) if hours > 0 else 0
                    })
                    
            except ValueError:
                continue

# Sort by potential revenue impact
roundup_candidates.sort(key=lambda x: x['revenue_impact'], reverse=True)

total_additional_hours = 0
total_additional_revenue = 0

print('CLIENT                              CURRENT  COULD BE  DESCRIPTION')
print('-' * 80)

for item in roundup_candidates:
    new_hours = item['hours'] + item['potential_add']
    total_additional_hours += item['potential_add']
    total_additional_revenue += item['revenue_impact']
    
    print(f"{item['client'][:30]:<30} {item['hours']:6.2f}h -> {new_hours:4.2f}h  {item['description'][:25]}")

print('=' * 80)
print(f'POTENTIAL GAINS:')
print(f'Additional hours: +{total_additional_hours:.2f}h')
print(f'Additional revenue: +€{total_additional_revenue:.2f}')
print(f'This would bring you to: {84 + total_additional_hours:.2f}h total')
print(f'New daily average: {(84 + total_additional_hours)/30:.2f}h/day')
print(f'Revenue total: €{7545.03 + total_additional_revenue:.2f}')