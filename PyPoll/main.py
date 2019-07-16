import os
import csv

with open("PyPoll_Resources_election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    PollData=list(csvreader)

    votes=[]
    candidates=[]
    unique_candidates=[]
    Li_votes=[]
    Khan_votes=[]
    Correy_votes=[]
    OTooley_votes=[]


    for row in PollData:
        votes.append(str(row[0]))
    total_votes=len(votes)
    for row in PollData:
        candidates.append(str(row[2]))
    
    unique_candidates=list(set(candidates))
    
    for row in PollData:
        if row[2]=="Li":
            Li_votes.append(str(row[0]))
        if row[2]=="Khan":
            Khan_votes.append(str(row[0]))
        if row[2]=="Correy":
            Correy_votes.append(str(row[0]))
        if row[2]=="O'Tooley":
            OTooley_votes.append(str(row[0]))
    
    Li_tvotes=len(Li_votes)
    Khan_tvotes=len(Khan_votes)
    Correy_tvotes=len(Correy_votes)
    OTooley_tvotes=len(OTooley_votes)


    Li_percent=(int(len(Li_votes))/int(len(votes)))*100
    Khan_percent=(int(len(Khan_votes))/int(len(votes)))*100
    Correy_percent=(int(len(Correy_votes))/int(len(votes)))*100
    OTooley_percent=(int(len(OTooley_votes))/int(len(votes)))*100

    if Li_percent>Khan_percent and Li_percent>Correy_percent and Li_percent>OTooley_percent:
        winner= "Li"
    if Khan_percent>Li_percent and Khan_percent>Correy_percent and Khan_percent>OTooley_percent:
        winner ="Khan"
    if Correy_percent>Li_percent and Correy_percent>Khan_percent and Correy_percent>OTooley_percent:
        winner="Correy"
    if OTooley_percent>Li_percent and OTooley_percent>Khan_percent and OTooley_percent>Correy_percent:
        winner="O'Tooley"
    
    print()
    print("Election Results")
    print("----------------------------------------------")
    print(f"Total votes: {total_votes}")
    print("----------------------------------------------")
    print(f'Khan: {round(Khan_percent,0)}% ({Khan_tvotes})')
    print(f'Correy: {round(Correy_percent,0)}% ({Correy_tvotes})')
    print(f'Li: {round(Li_percent,0)}% ({Li_tvotes})')
    print(f"O'Tooley: {round(OTooley_percent,0)}% ({OTooley_tvotes})")
    print("----------------------------------------------")
    print(f"Winner: {winner}")

f = open('Results_PyPoll.txt','w')
f.write("\n")
f.write("Election Results")
f.write("\n")
f.write("------------------------------------")
f.write("\n")
f.write(f"Total votes: {total_votes}")
f.write("\n")
f.write(f'Khan: {round(Khan_percent,0)}% ({Khan_tvotes})')
f.write("\n")
f.write(f'Correy: {round(Correy_percent,0)}% ({Correy_tvotes})')
f.write("\n")
f.write(f'Li: {round(Li_percent,0)}% ({Li_tvotes})')
f.write("\n")
f.write(f"O'Tooley: {round(OTooley_percent,0)}% ({OTooley_tvotes})")
f.write("\n")
f.write("----------------------------------------------")
f.write("\n")
f.write(f"Winner: {winner}")

f.close()