import os
import csv

with open("PyBank_Resources_budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    BankData=list(csvreader)

    profit=[]
    loss=[]
    profitlosses=[]
    months=[]

    for row in BankData:
        profitlosses.append(int(row[1]))
        months.append(str(row[0]))
        if int(row[1]) >= 0:
            profit.append(int(row[1]))
        else:
            loss.append(int(row[1]))
    
        totallosses=int(sum(loss))
        totalprofit=int(sum(profit))
        totalammount=totalprofit + totallosses

    totalmonths = len(months)

    change=[(y -x) for (x, y) in zip(profitlosses[:-1], profitlosses[1:])]
    
    average_change=int(sum(change))/int(len(change))

    maxincrease=max(change)
    maxdecrease=min(change)

    for row in range(len(BankData)-1):
        if maxincrease==int(BankData[row+1][1])-int(BankData[row][1]):
            month_increase=str(BankData[row+1][0])

    for row in range(len(BankData)-1):
        if maxdecrease==int(BankData[row+1][1])-int(BankData[row][1]):
            month_decrease=str(BankData[row+1][0])

    print("Financial Analysis")
    print("------------------------------------")
    print(f"Total months: {totalmonths}")
    print(f'Net total: $ {totalammount}')
    print(f'Average change: {average_change}')
    print(f'Greatest increase: {month_increase} $ {maxincrease}')
    print(f'Greatest decrease: {month_decrease} $ {maxdecrease}')

    
f = open('Results_PyBank.txt','w')
f.write("\n")
f.write("Financial Analysis")
f.write("\n")
f.write("------------------------------------")
f.write("\n")
f.write(f"Total months: {totalmonths}")
f.write("\n")
f.write(f'Net total: $ {totalammount}')
f.write("\n")
f.write(f'Average change: {average_change}')
f.write("\n")
f.write(f'Greatest increase: {month_increase} $ {maxincrease}')
f.write("\n")
f.write(f'Greatest decrease: {month_decrease} $ {maxdecrease}')
f.close()