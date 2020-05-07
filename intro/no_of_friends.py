from collections import Counter
from collections import defaultdict

users = [{ "id" : 0, "name" : "Hero"},
	{"id" : 1, "name" : "Dunn"},
	{"id" : 2  ,"name" : "Sue"},
	{"id" : 3, "name" :"Chi"},
   {"id" : 4, "name" : "Thor"},
   {"id" : 5, "name" : "Clive"},
   {"id" : 6, "name" : "Hicks"}]
   
friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), 
   (4,5), (5,6)]
   
friendships = {user["id"]: [] for user in users}
for i, j in friendship_pairs:
   	friendships[i].append(j)
   	friendships[j].append(i)
   	
   	
def number_of_friends(user):
   	""" How many friends does _user_ have """
   	user_id = user["id"]
   	friends_ids = friendships[user_id]
   	return len(friends_ids)
   	
total_connections = sum(number_of_friends(user) for user in users)
no_of_user = len(users)
avg_conn = total_connections/no_of_user

print("average connections of all the user ",avg_conn)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]  #loop and create pairs of id and num of friends
num_friends_by_id.sort(key = lambda id_of_friends: id_of_friends[1],reverse= True) #sort based on based on number of friends

def foaf_id_bad(user):
	""" find the connections of the user and then their connections """
	return [foaf_id 
				for friend_id in friendships[user["id"]]
				for foaf_id in friendships[friend_id]]
				
print("connections of the user ", foaf_id_bad(users[0]))

def friends_of_friends(user):
	user_id = user["id"]
	return Counter(
	foaf_id
	for friend_id in friendships[user_id]
	for foaf_id in friendships[friend_id]
	if foaf_id != user_id 
	and foaf_id not in friendships[user_id]
	)
	
print("friends of a friends of user ",friends_of_friends(users[3]))	

interests = [
(0,"Hadoop"),(0,"Big Data"),(0," HBase"),(0, "Java"), (0,"Spark"), (0,"Storm"), (0," Cassandra"),
(1,"No Sql"),(1,"MongoDb"),(1," HBase"), (1,"Postgress"),(1," Cassandra"),
(2, "Scikit-learn"), (2,"Sci Py"), (2,"Numpy"), (2,"StatsModels"), (2,"Pandas"),
(3,"R"),(3, "Python"),(3,"statistics"),(3, "regression"),(3,"Probability"),
(4,"Machine learning"),(4, "regression"),(4,"Decision Trees"),(4, "libsvm"),
(5,"R"),(5, "Python"),(5,"Java"),(5, "C++"),(5,"Haskell"), (5, "Programming languages"),
(6,"theory"),(6, "mathematics"),(6,"Probability"), (6, "Statistics")
]

#find persons with similiar interests
def data_scientists_with_who_like(target_interest):
	return [user_id for user_id, interest in interests
				if interest == target_interest]
				
				
#keys are interests and values are user ids				
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
	 user_ids_by_interest[interest].append(user_id)

#keys are user ids and values are interests
interests_by_user_id = defaultdict(list)		
for user_id,interest in interests:
	interests_by_user_id[user_id].append(interest)
	
	
def  most_common_interests_with(user):
	return Counter(interested_user_id
	for user_interests in interests_by_user_id[user["id"]]
    for interested_user_id in user_ids_by_interest[user_interests] if interested_user_id != user["id"]
	)
	
print("with most common interest with ",most_common_interests_with(users[0]))					

salaries_and_tenures = [(83000,8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)
]

#Keys are years, values are lists of salaries for each year
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	salary_by_tenure[tenure].append(salary)
	
#Keys are years and value is average salary
avg_salary_by_tenure = {
	tenure : sum(salaries)/ len(salaries)
	for tenure, salaries in salary_by_tenure.items()
}

print("average salary by tenure ", avg_salary_by_tenure)

def tenure_bucket(tenure):
	if tenure < 2:
		return "less than two"
	elif tenure < 5:
		return "between 2 and 5"
	else:
		return "greater than 5"

#keys are the bucket and values are the list of salaries falling in the bucket
salary_by_tenure_bucket = defaultdict(list)

for salary,tenure in salaries_and_tenures:
	bucket = tenure_bucket(tenure)
	salary_by_tenure_bucket[bucket].append(salary)								

#keys are tenure buckets and values are the average salaries of that bucket
avg_salary_by_bucket = {
	bucket : sum(salaries)/ len(salaries)
	for bucket, salaries in salary_by_tenure_bucket.items()
}											

print("average salary by tenure bucket ", avg_salary_by_bucket)					