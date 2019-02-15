#This class represents a time.
#It stores times with different representations but similar meanings as equal (1 hour 20 mintues vs. 80 minutes)

class Time: #We create the Time class.
	def __init__(self): #This time class has an init function
		self.hours = 0 #In which the timer has no hours
		self.minutes = 0 #nor minutes logged.
	
	def set_values(self, hours, minutes): #We can set the value of our timer.
		self.minutes = minutes #We begin by plugging in the basic values of minutes
		self.hours = hours #and hours given.
		self.format() #We now make this of the form where 0 <= minutes < 60 (a unique representation for a given time)

	def get_time(self): #We can request to see the amount of time stored
		return [self.hours, self.minutes] #In which we return a list of [hours, minutes]

	def compound(self, minutes, hours): #We can append some more time to our timer.
		self.hours += hours #We start by incrementing the bare hours
		self.minutes += minutes #and minutes
		self.format() #We then proceed to make sure our times meet the minutes requirements (0 <= minutes < 60)

	def subtract(self, minutes, hours): #We can furthermore subtract an amount of time from our timer.
		self.hours -= hours #We begin by taking off the appropriate number of hours
		self.minutes -= minutes #and minutes.
		self.format() #We then format.

	def __gt__(self, other): #Finally, we can compare two timers to see which one has the larger time represented.
		self_hours, self_mins = self.get_time() #We first get the number of hours and minutes from self
		other_hours, other_mins = other.get_time() #And from other.
		if (self_hours > other_hours): return True #Because of our unique formatting condition, if the number of hours in self is greater than the number of hours in other, self has more time.
		if (self_mins > other_mins and self_hours == other_hours): return True #If there is a tie between the two hours, we go down to the minutes. If the minutes of self are greater than the minutes of other, self is greater.
		return False #If neither of these two conditions is met, then we can conclude that other is larger (or equal).

	def format(self): #"format" makes our time meet the unique form requirement: 0 <= minutes < 60
		while (self.minutes >= 60): #If minutes is too large,
                        self.minutes -= 60 #We take one hour out of minutes
                        self.hours += 1 #and put it into hours.
                while (self.minutes < 0): #If minutes is too small,
                        self.minutes += 60 #We make minutes bigger
                        self.hours -= 1 #By taking off hours
