counties_0 = [ 'bradford', 'calhoun', 'charlotte', 'columbia', 'de_soto', 'duval', 'hendry', 'hillsborough', 'jefferson', 'levy', 'miami_dade', 'monroe', 'orange', 'palm_beach', 'putnam', 'santa_rosa', 'suwannee', 'taylor' ]
print(counties_0)

counties_1 = [ 'bay', 'nassau' ]
print(counties_1)

counties_2 = [ 'baker', 'highlands', 'lake' ]
print(counties_2)

counties_3 = [ 'citrus', 'dixie', 'gadsden', 'jackson' ]
print(counties_3)

counties_4 = [ 'alachua', 'brevard', 'broward', 'clay', 'collier', 'escambia', 'franklin', 'flagler', 'gilchrist', 'glades', 'gulf', 'hamilton', 'hernando', 'holmes', 'indian_river', 'lafayette', 'leon', 'liberty', 'madison', 'manatee', 'marion', 'martin', 'okaloosa', 'okechobee', 'pasco', 'pinellas', 'polk', 'st_lucie', 'st_john', 'sarasote', 'seminole', 'sumter', 'union', 'volusia', 'wakulla', 'walton', 'washington' ]
print(counties_4)


for county in counties_0:
   print(county)

for county in counties_1:
   print(county)

for county in counties_2:
   print(county)

for county in counties_3:
   print(county)

for county in counties_4:
   print(county)

ev_start_date = [ 'august_8', 'august_10', 'august_11', 'august_12', 'august_13' ]
print(ev_start_date)


print(ev_start_date[0])


print(ev_start_date[1])


print(ev_start_date[2])


print(ev_start_date[3])


print(ev_start_date[4])


for county in counties_0:
    print(f"if you live in {county} then early voting starts on {ev_start_date[0]}")


for county in counties_1:
	print(f"if you live in {county} then early voting starts on {ev_start_date[1]}")


for county in counties_2:
    print(f"if you live in {county} then early voting starts on {ev_start_date[2]}")


for county in counties_3:
    print(f"if you live in {county} then early voting starts on {ev_start_date[3]}")


for county in counties_4:
    print(f"if you live in {county} then early voting starts on {ev_start_date[4]}") 

