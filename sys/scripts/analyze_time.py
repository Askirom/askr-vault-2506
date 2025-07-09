import csv
from collections import defaultdict
import sys

hours = defaultdict(float)
revenue = defaultdict(float)

with open('clockodo_2025-06-30_1650.csv', 'r', encoding='utf-8') as f:
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

print('CLIENT ANALYSIS (excluding Secudor):')
print('=' * 70)
for client, h in sorted(hours.items(), key=lambda x: x[1], reverse=True):
    print(f'{client:<50} {h:6.2f}h €{revenue[client]:8.2f}')

print('=' * 70)
print(f'TOTAL NON-SECUDOR HOURS: {total_hours:.2f}h')
print(f'TOTAL NON-SECUDOR REVENUE: €{total_revenue:.2f}')
if total_hours > 0:
    print(f'AVERAGE RATE: €{total_revenue/total_hours:.2f}/hour')
    
# Check if meeting 7h/day target (assuming this is June data)
days_in_period = 30  # Estimate for June
target_hours = days_in_period * 7
print(f'\nTARGET ANALYSIS:')
print(f'Target hours (7h/day * {days_in_period} days): {target_hours}h')
print(f'Actual hours: {total_hours:.2f}h')
print(f'Shortfall: {target_hours - total_hours:.2f}h')
print(f'Daily average: {total_hours/days_in_period:.2f}h/day')

# Revenue analysis
monthly_target_min = 10000
monthly_target_ideal = 12000
print(f'\nREVENUE ANALYSIS:')
print(f'Current revenue: €{total_revenue:.2f}')
print(f'Minimum target (€10k): €{monthly_target_min - total_revenue:.2f} shortfall')
print(f'Ideal target (€12k): €{monthly_target_ideal - total_revenue:.2f} shortfall')

# Calculate total hours including Secudor for context
print(f'\nOVERALL TRACKING ANALYSIS:')
total_all_hours = 0
with open('clockodo_2025-06-30_1650.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # skip header
    for row in reader:
        if len(row) >= 6:
            try:
                h = float(row[4]) if row[4] else 0
                total_all_hours += h
            except ValueError:
                continue

secudor_hours = total_all_hours - total_hours
print(f'Total hours (all clients): {total_all_hours:.2f}h')
print(f'Secudor hours: {secudor_hours:.2f}h')
print(f'Non-Secudor target: 7h/day * 30 days = 210h')
print(f'You are tracking {total_hours:.2f}h non-Secudor vs 210h target')
print(f'Missing: {210 - total_hours:.2f}h ({(210 - total_hours)/30:.2f}h per day)')

# Identify lowest revenue clients
print(f'\nLOWEST VALUE CLIENTS (consider focusing elsewhere):')
for client, h in sorted(hours.items(), key=lambda x: x[1]):
    if h < 3:  # Less than 3 hours
        rate = revenue[client]/h if h > 0 else 0
        print(f'{client:<50} {h:6.2f}h €{rate:6.2f}/h')