eligible_voters = [ 'aleks', 'amber', 'ben', 'bruce' ]

print(eligible_voters[0].title())

print(eligible_voters[1].title())

print(eligible_voters[2].title())

print(eligible_voters[3].title())


eligible_voters = [ 'aleks', 'amber', 'ben', 'bruce' ]
for eligible_voter in eligible_voters:
   print(f"{eligible_voter.title()}, you are eligible to vote in this election!")
   print(f"please confirm that your voter record is correct, {eligible_voter.title()}.\n")

print("Thank you for coming to vote!")
