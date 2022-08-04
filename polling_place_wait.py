class PollingPlace:
   """A simple attempt to model a polling place."""
    
    
   def  __init__ (self, precinct, wait_time):
      """Initialize precinct name and wait time attributes."""
      self.precinct = precinct
      self.wait_time = wait_time


   def precinct(self):
      """Describe name of precinct."""
      print(f"{self.precinct} is your polling place.")

   
   def wait_time(self):
      """Describe how long is the wait time."""
      print(f"{self.wait_time} is expected time to wait.")


   def update_wait_time(self, new_time):
      """Set the wait time to the given value."""
      self.wait_time = new_time
      print(f"my wait time is now {self.wait_time} minutes.")





class PollingPlace:


    my_polling_place = PollingPlace('Lakeland Courthouse', '20')	
    your_polling_place = PollingPlace('Mulberry Civic Center', '45')
    amandas_polling_place = PollingPlace('Bartow Community Center', '52')
    

    PollingPlace.name = ('Lakeland Courthouse')
    PollingPlace.wait_time = ('20')


    your_polling_place.name = ('Mulberry Civic Center')
    your_polling_place.wait_time = ('45')

    
    amandas_polling_place.name = ('Bartow Community Center')
    amandas_polling_place.wait_time = ('52')


    print(f"My polling place is {my_polling_place.name}.")
    print(f"My expected wait time is {my_polling_place.wait_time} minutes.")


    print(f"Your polling place is {your_polling_place.name}.")
    print(f"Your expected wait time is {your_polling_place.wait_time} minutes.")


    print(f"Amandas polling place is {amandas_polling_place.name}.")
    print(f"Amandas expected wait time is {amandas_polling_place.wait_time} minutes")


    my_polling_place.update_wait_time(19)
    print(f"My expected wait time is {my_polling_place.wait_time} minutes.")


  
