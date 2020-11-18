from pymongo import MongoClient  
  
  
myclient = MongoClient("mongodb://localhost:27017/") 
  
# database  
db = myclient["GFG"] 
  
# Created or Switched to collection  
# names: GeeksForGeeks 
collection = db["Student"] 
  
# Creating a list of records which we  
# insert in the collection using the 
# update_many() method. 
mylist = [ 
  { "_id": 11, "name": "Vishwash", "Roll No": "1001", "Branch":"CSE"}, 
  { "_id": 12, "name": "Vishesh", "Roll No": "1002", "Branch":"IT"}, 
  { "_id": 32, "name": "Shivam", "Roll No": "1003", "Branch":"ME"}, 
  { "_id": 6, "name": "Yash", "Roll No": "1004", "Branch":"ECE"},
  {  "_id":5,"name": "Yasdad", "Roll No": "1000000", "Branch":"ECsdas"} 
  
] 
  
# In the above list _id field is provided so it inserted in  
# the collection as specified. 
  
# Inseting the entire list in the collection 
collection.insert_many(mylist)