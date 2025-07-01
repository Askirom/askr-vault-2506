import csv
from collections import defaultdict
import datetime

print('YEARLY ANALYSIS - 2025 GOAL ACHIEVABILITY')
print('=' * 70)

# Track monthly data
monthly_data = defaultdict(lambda: {
    'billable_hours': 0, 'billable_revenue': 0,
    'pauschale_hours': 0, 'pauschale_revenue': 0,
    'total_hours': 0, 'total_revenue': 0
})

# Pauschale rates
IS_PAUSCHALE_RATE = 130
DS_PAUSCHALE_RATE = 185

# Track service performance
service_stats = defaultdict(lambda: {'hours': 0, 'revenue': 0, 'count': 0})
client_stats = defaultdict(lambda: {'hours': 0, 'revenue': 0})

total_billable_hours = 0
total_billable_revenue = 0
total_pauschale_hours = 0
total_pauschale_revenue = 0

with open('clockodo_2025-07-01_0936.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # skip header
    
    for row in reader:
        if len(row) >= 7:
            client = row[0].strip('"')
            service = row[1].strip('"')
            billable = row[2].strip('"')
            billed = row[3].strip('"')
            description = row[4].strip('"')
            
            try:
                hours = float(row[5]) if row[5] else 0
                revenue = float(row[6]) if row[6] else 0
                
                # Skip internal work (assuming we can identify it)
                if 'secudor' in client.lower() or 'int. organisation' in service.lower():
                    continue
                
                # Calculate actual revenue including pauschale
                actual_revenue = revenue
                if service == 'IS-Pauschale':
                    actual_revenue = hours * IS_PAUSCHALE_RATE
                elif service == 'DS-Pauschale':
                    actual_revenue = hours * DS_PAUSCHALE_RATE
                
                # Track by service
                service_stats[service]['hours'] += hours
                service_stats[service]['revenue'] += actual_revenue
                service_stats[service]['count'] += 1
                
                # Track by client
                client_stats[client]['hours'] += hours
                client_stats[client]['revenue'] += actual_revenue
                
                # Separate pauschale from direct billable
                if service in ['IS-Pauschale', 'DS-Pauschale']:
                    total_pauschale_hours += hours
                    total_pauschale_revenue += actual_revenue
                else:
                    total_billable_hours += hours
                    total_billable_revenue += revenue
                    
            except ValueError:
                continue

total_hours = total_billable_hours + total_pauschale_hours
total_revenue = total_billable_revenue + total_pauschale_revenue

print('YEARLY TOTALS (2025):')
print('=' * 70)
print(f'Goal-counting work:   {total_billable_hours:8.2f}h  €{total_billable_revenue:10.2f}')
print(f'Pauschale work:       {total_pauschale_hours:8.2f}h  €{total_pauschale_revenue:10.2f}')
print(f'TOTAL CLIENT WORK:    {total_hours:8.2f}h  €{total_revenue:10.2f}')

# Calculate averages
avg_billable_rate = total_billable_revenue / total_billable_hours if total_billable_hours > 0 else 0
avg_total_rate = total_revenue / total_hours if total_hours > 0 else 0

print(f'\nRATES:')
print(f'Goal-counting rate:   €{avg_billable_rate:.2f}/hour')
print(f'Blended rate:         €{avg_total_rate:.2f}/hour')

# Monthly projections
months_passed = 6  # Assuming we're at mid-year
monthly_avg_billable = total_billable_revenue / months_passed
monthly_avg_hours = total_billable_hours / months_passed

print(f'\nMONTHLY AVERAGES (based on {months_passed} months):')
print(f'Monthly goal-counting revenue: €{monthly_avg_billable:.2f}')
print(f'Monthly goal-counting hours:   {monthly_avg_hours:.2f}h')
print(f'Daily average:                 {monthly_avg_hours/30:.2f}h/day')

# Goal analysis
target_10k = 10000
target_12k = 12000

print(f'\nGOAL ACHIEVABILITY:')
print('=' * 70)
print(f'Current monthly average: €{monthly_avg_billable:.2f}')
print(f'€10k goal: {("✅ ACHIEVABLE" if monthly_avg_billable >= target_10k else "❌ NEED IMPROVEMENT")}')
if monthly_avg_billable < target_10k:
    gap_10k = target_10k - monthly_avg_billable
    hours_needed_10k = gap_10k / avg_billable_rate if avg_billable_rate > 0 else 0
    print(f'  Gap: €{gap_10k:.2f} ({hours_needed_10k:.1f}h more per month)')

print(f'€12k goal: {("✅ ACHIEVABLE" if monthly_avg_billable >= target_12k else "❌ NEED IMPROVEMENT")}')
if monthly_avg_billable < target_12k:
    gap_12k = target_12k - monthly_avg_billable
    hours_needed_12k = gap_12k / avg_billable_rate if avg_billable_rate > 0 else 0
    print(f'  Gap: €{gap_12k:.2f} ({hours_needed_12k:.1f}h more per month)')

# Year-end projections
projected_annual_billable = monthly_avg_billable * 12
projected_annual_hours = monthly_avg_hours * 12

print(f'\nYEAR-END PROJECTIONS:')
print(f'Projected goal-counting revenue: €{projected_annual_billable:.2f}')
print(f'Projected goal-counting hours:   {projected_annual_hours:.2f}h')

# Top revenue sources
print(f'\nTOP REVENUE SOURCES:')
print('=' * 50)
for service, stats in sorted(service_stats.items(), key=lambda x: x[1]['revenue'], reverse=True)[:10]:
    if stats['revenue'] > 0:
        rate = stats['revenue'] / stats['hours'] if stats['hours'] > 0 else 0
        print(f'{service:<20} €{stats["revenue"]:8.2f} ({stats["hours"]:6.2f}h @ €{rate:6.2f}/h)')

print(f'\nTOP CLIENTS:')
print('=' * 50)
for client, stats in sorted(client_stats.items(), key=lambda x: x[1]['revenue'], reverse=True)[:10]:
    if stats['revenue'] > 0:
        rate = stats['revenue'] / stats['hours'] if stats['hours'] > 0 else 0
        print(f'{client[:30]:<30} €{stats["revenue"]:8.2f} ({stats["hours"]:5.2f}h)')

# Strategic recommendations
print(f'\nSTRATEGIC RECOMMENDATIONS:')
print('=' * 50)
if monthly_avg_billable < target_10k:
    print(f'• Focus on increasing billable hours by {(target_10k - monthly_avg_billable)/avg_billable_rate:.1f}h/month')
    print(f'• Target higher-rate services (€{avg_billable_rate:.0f}+ per hour)')
    print(f'• Convert more pauschale work to billable consulting')
else:
    print(f'• You\'re on track for €10k/month!')
    if monthly_avg_billable < target_12k:
        print(f'• For €12k, add {(target_12k - monthly_avg_billable)/avg_billable_rate:.1f}h/month more')