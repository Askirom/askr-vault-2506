import csv
from collections import defaultdict

print('UPDATED TIME TRACKING ANALYSIS - JUNE 2025')
print('=' * 70)

# Analyze the updated file
hours = defaultdict(float)
revenue = defaultdict(float)

with open('clockodo_2025-06-30_1724.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # skip header
    for row in reader:
        if len(row) >= 6 and row[0] != 'secudor':
            client = row[0].strip('"')
            try:
                h = float(row[4]) if row[4] else 0
                r = float(row[5]) if row[5] else 0
                hours[client] += h
                revenue[client] += r
            except ValueError:
                continue

total_hours = sum(hours.values())
total_revenue = sum(revenue.values())

print('TOP CLIENTS BY REVENUE (Non-Secudor):')
print('=' * 70)
for client, rev in sorted(revenue.items(), key=lambda x: x[1], reverse=True):
    if rev > 0:
        rate = rev/hours[client] if hours[client] > 0 else 0
        print(f'{client[:40]:<40} {hours[client]:6.2f}h €{rev:8.2f} (€{rate:6.2f}/h)')

print('=' * 70)
print(f'SUMMARY:')
print(f'Total non-Secudor hours: {total_hours:.2f}h')
print(f'Total non-Secudor revenue: €{total_revenue:.2f}')
print(f'Average rate: €{total_revenue/total_hours:.2f}/hour' if total_hours > 0 else 'No hours')
print(f'Daily average: {total_hours/30:.2f}h/day')

# Compare to previous
old_total_hours = 84.00
old_total_revenue = 7545.03
improvement_hours = total_hours - old_total_hours
improvement_revenue = total_revenue - old_total_revenue

print(f'\nIMPROVEMENT FROM ROUNDUP:')
print(f'Hours increase: +{improvement_hours:.2f}h')
print(f'Revenue increase: +€{improvement_revenue:.2f}')

# Target analysis
target_hours = 210  # 7h/day * 30 days
target_revenue_min = 10000
target_revenue_ideal = 12000

print(f'\nTARGET ANALYSIS:')
print(f'Target hours (7h/day): {target_hours}h')
print(f'Remaining shortfall: {target_hours - total_hours:.2f}h ({(target_hours - total_hours)/30:.2f}h/day)')
print(f'Target revenue (min): €{target_revenue_min}')
print(f'Revenue gap (min): €{target_revenue_min - total_revenue:.2f}')
print(f'Target revenue (ideal): €{target_revenue_ideal}')
print(f'Revenue gap (ideal): €{target_revenue_ideal - total_revenue:.2f}')

# Budget-relevant analysis
print(f'\nBUDGET ANALYSIS:')
print(f'Current monthly revenue: €{total_revenue:.2f}')
print(f'At current rate (€{total_revenue/total_hours:.2f}/h):')
print(f'  - To reach €10k: need {(10000 - total_revenue)/(total_revenue/total_hours):.1f} more hours')
print(f'  - To reach €12k: need {(12000 - total_revenue)/(total_revenue/total_hours):.1f} more hours')

# Check zero-revenue work
print(f'\nZERO-REVENUE WORK (budget concern):')
for client, rev in revenue.items():
    if rev == 0 and hours[client] > 0:
        print(f'{client:<40} {hours[client]:6.2f}h €0.00 (opportunity cost)')