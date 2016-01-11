#this is to create a the variable "cars"
cars=100
#use underscores to create spaces
space_in_cars=4.0
drivers=30
passengers=90
#this makes variables about calculations of previouse variables
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_cars
average_passengers_per_car=passengers/cars_driven

#Now we are going to print out the various results 
#when the program is executed
print "there are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "there will be", cars_not_driven, "empty cars."
print "we can transport", carpool_capacity, "people today"
print "we have", passengers, "to carpool today"
print "we need to put", average_passengers_per_car, "in each car."
