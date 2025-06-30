import csv

print('DETAILED ROUNDUP RECOMMENDATIONS WITH DATES')
print('=' * 80)

roundup_candidates = []

with open('clockodo_2025-06-30_1650.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # skip header
    
    for i, row in enumerate(reader, 1):
        if len(row) >= 6 and row[0] != 'secudor':
            client = row[0].strip('"')
            project = row[1].strip('"')
            service = row[2].strip('"')
            description = row[3].strip('"')
            try:
                hours = float(row[4]) if row[4] else 0
                revenue = float(row[5]) if row[5] else 0
                
                # Flag potentially under-tracked entries
                flag = False
                new_hours = hours
                reason = ""
                
                # 15-30 min tasks (likely took longer)
                if hours == 0.25:
                    flag = True
                    new_hours = 0.5  # Round to 0.5h
                    reason = "15min → 30min (realistic minimum)"
                
                # 30 min complex tasks
                elif hours == 0.5 and any(task in description for task in ['Erstellung', 'Prüfung', 'Update', 'Bewertung']):
                    flag = True
                    new_hours = 1.0  # Round to 1h
                    reason = "Complex 30min → 1h (includes thinking time)"
                
                # 1h creation/review tasks (often take 1.5h)
                elif hours == 1.0 and any(task in description for task in ['Erstellung', 'Prüfung', 'Bewertung']):
                    flag = True
                    new_hours = 1.5  # Round to 1.5h
                    reason = "Creation/review 1h → 1.5h (realistic for quality work)"
                
                # Short coordination tasks
                elif hours <= 0.5 and any(task in description for task in ['Abstimmung', 'Vorbereitung', 'Terminplanung', 'Jour Fixe']):
                    flag = True
                    new_hours = hours + 0.25  # Add 15min
                    reason = f"Coordination +15min (prep/followup time)"
                
                if flag and revenue > 0:  # Only paying clients
                    additional_hours = new_hours - hours
                    additional_revenue = additional_hours * (revenue/hours) if hours > 0 else 0
                    
                    roundup_candidates.append({
                        'line': i,
                        'client': client,
                        'project': project,
                        'description': description,
                        'current_hours': hours,
                        'new_hours': new_hours,
                        'additional_hours': additional_hours,
                        'reason': reason,
                        'additional_revenue': additional_revenue
                    })
                    
            except ValueError:
                continue

# Sort by additional revenue (highest impact first)
roundup_candidates.sort(key=lambda x: x['additional_revenue'], reverse=True)

print('LINE# CLIENT                    CURRENT → NEW    TASK DESCRIPTION                    REASON')
print('-' * 80)

total_additional_hours = 0
total_additional_revenue = 0

for item in roundup_candidates:
    total_additional_hours += item['additional_hours']
    total_additional_revenue += item['additional_revenue']
    
    line_info = f"L{item['line']:2d}"
    client_short = item['client'][:20]
    hours_change = f"{item['current_hours']:4.2f}h → {item['new_hours']:4.2f}h"
    desc_short = item['description'][:30]
    revenue_gain = f"+€{item['additional_revenue']:5.2f}"
    
    print(f"{line_info} {client_short:<20} {hours_change:<12} {desc_short:<30} {revenue_gain}")
    print(f"    Reason: {item['reason']}")
    print()

print('=' * 80)
print(f'SUMMARY:')
print(f'Total entries to adjust: {len(roundup_candidates)}')
print(f'Additional hours: +{total_additional_hours:.2f}h')
print(f'Additional revenue: +€{total_additional_revenue:.2f}')
print(f'New totals: {84 + total_additional_hours:.2f}h, €{7545.03 + total_additional_revenue:.2f}')
print(f'New daily average: {(84 + total_additional_hours)/30:.2f}h/day')

print(f'\nACTION ITEMS:')
print(f'□ Go through CSV lines and update the hours column')
print(f'□ Focus on high-revenue adjustments first (top 10 entries)')
print(f'□ These adjustments are conservative and defensible')