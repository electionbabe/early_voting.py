class Polling_place:
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


class Polling_place:


    my_polling_place = Polling_place('Lakeland Courthouse', '20')	
    

    Polling_place.name = ('Lakeland Courthouse')
    Polling_place.wait_time = ('20')

    print(f"My polling place is {my_polling_place.name}.")
    print(f"My expected wait time is {my_polling_place.wait_time} minutes.")
