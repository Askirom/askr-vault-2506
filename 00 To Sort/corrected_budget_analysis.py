import csv
from collections import defaultdict

print('CORRECTED BUDGET ANALYSIS - WITH PAUSCHALE RATES')
print('=' * 70)

# Track different categories with correct pauschale rates
billable_revenue = 0
billable_hours = 0
pauschale_hours = 0
pauschale_revenue = 0
nonbillable_hours = 0

service_stats = defaultdict(lambda: {'hours': 0, 'revenue': 0, 'count': 0})

# Pauschale rates
IS_PAUSCHALE_RATE = 130  # €130/h
DS_PAUSCHALE_RATE = 185  # €185/h

with open('clockodo_2025-06-30_1724.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # skip header
    
    for row in reader:
        if len(row) >= 6:
            service = row[0].strip('"')
            billable = row[1].strip('"')
            billed = row[2].strip('"') 
            description = row[3].strip('"')
            try:
                hours = float(row[4]) if row[4] else 0
                revenue = float(row[5]) if row[5] else 0
                
                # Skip internal organization (Secudor work)
                if service == 'Int. Organisation':
                    continue
                
                # Calculate actual revenue including pauschale
                actual_revenue = revenue
                if service == 'IS-Pauschale':
                    actual_revenue = hours * IS_PAUSCHALE_RATE
                    pauschale_hours += hours
                    pauschale_revenue += actual_revenue
                elif service == 'DS-Pauschale':
                    actual_revenue = hours * DS_PAUSCHALE_RATE
                    pauschale_hours += hours
                    pauschale_revenue += actual_revenue
                
                service_stats[service]['hours'] += hours
                service_stats[service]['revenue'] += actual_revenue
                service_stats[service]['count'] += 1
                
                if billable == '1':
                    billable_hours += hours
                    billable_revenue += actual_revenue
                else:
                    nonbillable_hours += hours
                    
            except ValueError:
                continue

total_client_hours = billable_hours + nonbillable_hours
total_client_revenue = billable_revenue

print('CORRECTED REVENUE BREAKDOWN:')
print('=' * 70)
print(f'Direct billable work: {billable_hours-pauschale_hours:6.2f}h  €{billable_revenue-pauschale_revenue:8.2f}')
print(f'Pauschale work:       {pauschale_hours:6.2f}h  €{pauschale_revenue:8.2f}')
print(f'  - IS-Pauschale:     {service_stats["IS-Pauschale"]["hours"]:6.2f}h  €{service_stats["IS-Pauschale"]["revenue"]:8.2f} (@€130/h)')
print(f'  - DS-Pauschale:     {service_stats["DS-Pauschale"]["hours"]:6.2f}h  €{service_stats["DS-Pauschale"]["revenue"]:8.2f} (@€185/h)')
print(f'Non-billable work:    {nonbillable_hours:6.2f}h  €0.00')
print(f'TOTAL CLIENT WORK:    {total_client_hours:6.2f}h  €{total_client_revenue:8.2f}')

print(f'\nCORRECTED SERVICE BREAKDOWN:')
print('=' * 70)
for service, stats in sorted(service_stats.items(), key=lambda x: x[1]['revenue'], reverse=True):
    if stats['revenue'] > 0:
        rate = stats['revenue'] / stats['hours'] if stats['hours'] > 0 else 0
        print(f'{service:<20} {stats["hours"]:6.2f}h  €{stats["revenue"]:8.2f}  (€{rate:6.2f}/h)  [{stats["count"]} tasks]')

print(f'\nCORRECTED BUDGET ANALYSIS:')
print('=' * 70)
avg_rate = total_client_revenue / total_client_hours if total_client_hours > 0 else 0
print(f'ACTUAL monthly revenue: €{total_client_revenue:.2f}')
print(f'Daily average: {total_client_hours/30:.2f}h/day')
print(f'Average rate: €{avg_rate:.2f}/hour')

# Target calculations
target_min = 10000
target_ideal = 12000
shortfall_min = target_min - total_client_revenue
shortfall_ideal = target_ideal - total_client_revenue

print(f'\nTARGET STATUS:')
if shortfall_min <= 0:
    print(f'🎉 €10k target: ACHIEVED! (€{total_client_revenue:.2f})')
    print(f'€12k target: need €{shortfall_ideal:.2f} more = {shortfall_ideal/avg_rate:.1f} more hours' if avg_rate > 0 else 'Need revenue data')
else:
    print(f'€10k target: need €{shortfall_min:.2f} more = {shortfall_min/avg_rate:.1f} more hours' if avg_rate > 0 else 'Need revenue data')
    print(f'€12k target: need €{shortfall_ideal:.2f} more = {shortfall_ideal/avg_rate:.1f} more hours' if avg_rate > 0 else 'Need revenue data')

# Previous vs current
old_revenue = 7545.03
old_hours = 84.00
improvement_revenue = total_client_revenue - old_revenue
improvement_hours = total_client_hours - old_hours

print(f'\nIMPROVEMENT FROM CORRECTIONS:')
print(f'Revenue increase: +€{improvement_revenue:.2f}')
print(f'Hours increase: +{improvement_hours:.2f}h')
print(f'Now at {(total_client_revenue/target_ideal)*100:.1f}% of €12k target')

print(f'\nKEY INSIGHTS:')
print(f'• Pauschale work contributes €{pauschale_revenue:.2f} ({(pauschale_revenue/total_client_revenue)*100:.1f}% of revenue)')
print(f'• Your blended rate is €{avg_rate:.2f}/hour')
print(f'• You need {(210-total_client_hours):.1f} more hours to hit 7h/day target')
if shortfall_min <= 0:
    print(f'• You\'ve hit your minimum revenue target!')
else:
    print(f'• You\'re {(total_client_revenue/target_min)*100:.1f}% to minimum target')