import csv
from collections import defaultdict

print('BUDGET & BILLABILITY ANALYSIS - UPDATED JUNE 2025')
print('=' * 70)

# Track different categories
billable_revenue = 0
billable_hours = 0
billed_revenue = 0
billed_hours = 0
nonbillable_hours = 0
zero_revenue_hours = 0

service_stats = defaultdict(lambda: {'hours': 0, 'revenue': 0, 'count': 0})

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
                    
                service_stats[service]['hours'] += hours
                service_stats[service]['revenue'] += revenue
                service_stats[service]['count'] += 1
                
                if billable == '1':  # Billable work
                    billable_hours += hours
                    billable_revenue += revenue
                    
                    if billed == '1':  # Already billed
                        billed_hours += hours
                        billed_revenue += revenue
                else:
                    nonbillable_hours += hours
                    
                if revenue == 0:
                    zero_revenue_hours += hours
                    
            except ValueError:
                continue

total_client_hours = billable_hours + nonbillable_hours
total_client_revenue = billable_revenue

print('BILLABILITY BREAKDOWN:')
print('=' * 70)
print(f'Billable work:     {billable_hours:6.2f}h  €{billable_revenue:8.2f}')
print(f'  - Already billed: {billed_hours:6.2f}h  €{billed_revenue:8.2f}')
print(f'  - Not yet billed: {billable_hours-billed_hours:6.2f}h  €{billable_revenue-billed_revenue:8.2f}')
print(f'Non-billable work: {nonbillable_hours:6.2f}h  €0.00')
print(f'Zero revenue work: {zero_revenue_hours:6.2f}h  €0.00')
print(f'TOTAL CLIENT WORK: {total_client_hours:6.2f}h  €{total_client_revenue:8.2f}')

print(f'\nSERVICE TYPE BREAKDOWN:')
print('=' * 70)
for service, stats in sorted(service_stats.items(), key=lambda x: x[1]['revenue'], reverse=True):
    if stats['revenue'] > 0:
        rate = stats['revenue'] / stats['hours'] if stats['hours'] > 0 else 0
        print(f'{service:<20} {stats["hours"]:6.2f}h  €{stats["revenue"]:8.2f}  (€{rate:6.2f}/h)  [{stats["count"]} tasks]')

# Zero revenue services
print(f'\nZERO REVENUE SERVICES (budget concern):')
for service, stats in service_stats.items():
    if stats['revenue'] == 0 and stats['hours'] > 0:
        print(f'{service:<20} {stats["hours"]:6.2f}h  €0.00  [{stats["count"]} tasks]')

print(f'\nBUDGET ANALYSIS:')
print('=' * 70)
avg_rate = total_client_revenue / total_client_hours if total_client_hours > 0 else 0
print(f'Current monthly revenue: €{total_client_revenue:.2f}')
print(f'Current daily average: {total_client_hours/30:.2f}h/day')
print(f'Average rate: €{avg_rate:.2f}/hour')

# Target calculations
target_min = 10000
target_ideal = 12000
shortfall_min = target_min - total_client_revenue
shortfall_ideal = target_ideal - total_client_revenue

print(f'\nTO REACH TARGETS:')
print(f'€10k target: need €{shortfall_min:.2f} more = {shortfall_min/avg_rate:.1f} more hours' if avg_rate > 0 else 'Need revenue data')
print(f'€12k target: need €{shortfall_ideal:.2f} more = {shortfall_ideal/avg_rate:.1f} more hours' if avg_rate > 0 else 'Need revenue data')

# Unbilled work analysis
unbilled_value = billable_revenue - billed_revenue
print(f'\nCASH FLOW:')
print(f'Unbilled work value: €{unbilled_value:.2f}')
print(f'Unbilled hours: {billable_hours-billed_hours:.2f}h')

print(f'\nKEY INSIGHTS:')
print(f'• {(zero_revenue_hours/total_client_hours)*100:.1f}% of time generates no revenue')
print(f'• {(nonbillable_hours/total_client_hours)*100:.1f}% of time is non-billable')
print(f'• {(unbilled_value/billable_revenue)*100:.1f}% of billable work not yet invoiced')