from collections import Counter

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

print(avg_conn)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]  #loop and create pairs of id and num of friends
num_friends_by_id.sort(key = lambda id_of_friends: id_of_friends[1],reverse= True) #sort based on based on number of friends

def foaf_id_bad(user):
	""" find the connections of the user and then their connections """
	return [foaf_id 
				for friend_id in friendships[user["id"]]
				for foaf_id in friendships[friend_id]]
				
print(foaf_id_bad(users[0]))

def friends_of_friends(user):
	user_id = user["id"]
	return Counter(
	foaf_id
	for friend_id in friendships[user_id]
	for foaf_id in friendships[friend_id]
	if foaf_id != user_id 
	and foaf_id not in friendships[user_id]
	)
	
print(friends_of_friends(users[3]))	