users = [
  {'id': 0, 'name': 'Hero'},
  {'id': 1, 'name': 'Dun'},
  {'id': 2, 'name': 'Sue'},
  {'id': 3, 'name': 'Chi'},
  {'id': 4, 'name': 'Thor'},
  {'id': 5, 'name': 'Clive'},
  {'id': 6, 'name': 'Hicks'},
  {'id': 7, 'name': 'Devin'},
  {'id': 8, 'name': 'Kate'},
  {'id': 9, 'name': 'Klein'}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
  (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# Let's create a dict where the keys are user ids and the values
# are lists of friend ids, we want it to look like this:
# {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [4, 6, 7], 6: [5, 8], 7: [5, 8], 8: [6, 7, 9], 9: [8]}

# Initialize the dict with an empty list for each user id:
friendships = {user['id'] : [] for user in users}

# And loop over the friendship pairs to populate it:
for (i, j) in friendship_pairs:
  friendships[i].append(j) # Add j as a friend of user i
  friendships[j].append(i) # Add i as a friend of user j
  # lis = friendships.get(i, [])
  # lis.append(j)
  # friendships[i] = lis

  # lis = friendships.get(j, [])
  # lis.append(i)
  # friendships[j] = lis

# Q: what's the average number of connections?

def number_of_friends(user):
  """ How many friends does _user_ have?"""
  user_id = user['id']
  friend_ids = friendships[user_id]
  return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)  # 24
num_users = len(users)
avg_connections = total_connections / num_users    # 24 / 10 == 2.4


# Q: Whate are the most connected people?

# Create a list (user_id, number_of_friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

# Sort the from 'most friends' to 'least friends'
num_friends_by_id.sort(reverse=True, key=lambda x : x[1]) # network metric degree centrality

# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

#Q. Data scientists you may know

def foaf_ids_bad(user):
  """ returns a list that contains friends of friends.
  for example foaf_ids_bad(users[0]) = [0, 2, 3, 0, 1, 3]
  """
  return [ foaf_id
    for friend_id in friendships[user['id']]
      for foaf_id in friendships[friend_id]
  ]
  # foaf = []
  # user_id = user['id']
  # friend_ids = friendships[user_id]
  # for friend_id in friend_ids:
  #   # foaf += friendships[friend_id]
  # return foaf

from collections import Counter

def friends_of_friends(user):
  """ returns counts of friends of friends, exclude people already known to the user.
  for example friends_of_friends(users[3]) = Counter({0: 2, 5: 1})
  """
  user_id = user['id']
  return Counter(
   foaf_id
    for friend_id in friendships[user_id]
      for foaf_id in friendships[friend_id]
        if (foaf_id != user_id and foaf_id not in friendships[user_id])
  )


# interests is a list of pairs (user_id, interest)
interests = [
  (0, 'Hadoop'), (0, 'Big Data'), (0, 'HBase'), (0, 'Java'),
  (0, 'Spark'), (0, 'Storm'), (0, 'Cassandra'),
  (9, 'Hadoop'), (9, 'Java'), (9, 'MapReduce'), (9, 'Big Data')
]

def data_scientists_who_like(target_interest):
  """ Find the ids of all users who like the target interest.
  For example, data_scientists_who_like('Big Data') = [0, 9]
  """
  return [ user_id
  for (user_id, user_interest) in interests
    if (user_interest == target_interest)
  ]

# But If we have a lot of users and interests of if we want to do a lot of searches,
# we should probably build an index from interests to users (so that we don't have to examine the whole
# list of interests for every search).

from collections import defaultdict

# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for (user_id, user_interest) in interests:
  user_ids_by_interest[user_interest].append(user_id)

# Keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)
for (user_id, user_interest) in interests:
  interests_by_user_id[user_id].append(user_interest)

# Q: Who has the most interests in common with a given user

def most_common_interests_with(user):
  user_id = user['id']
  user_interests = interests_by_user_id[user_id]
  return Counter(
    id
    for interest in user_interests
      for id in user_ids_by_interest[interest]
        if id != user_id

  )

# Salaries and Experience
salaries_and_tenures = [
  (83000, 8.7), (88000, 8.1),
  (48000, 0.7), (76000, 6),
  (69000, 6.5), (76000, 7.5),
  (60000, 2.5), (83000, 10),
  (48000, 1.9), (63000, 4.2)  
]

# Plot the data
from matplotlib import pyplot as plt

tenures = [tenure for (salary, tenure) in salaries_and_tenures]
salaries = [salary for (salary, tenure) in salaries_and_tenures]
# plt.scatter(tenures, salaries)
# plt.show()

# Q: What is the average salary for each tenure?

# Keys are years, values ar lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)
for (salary, tenure) in salaries_and_tenures:
  salary_by_tenure[tenure].append(salary)

#Keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
  tenure: sum(salaries) / len(salaries) 
  for (tenure, salaries) in salary_by_tenure.items()
}

# Bucket the tenures
def tenure_bucket(tenure):
  if tenure < 2:
    return 'less than two'
  elif tenure < 5:
    return 'between two and five'
  else:
    return 'More than five'
  
# we can group together the salaries corresponding to each bucket
# Keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)
for (salary, tenure) in salaries_and_tenures:
  bucket = tenure_bucket(tenure)
  salary_by_tenure_bucket[bucket].append(salary)

# Compute average salary for each group
# Keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
  bucket: sum(salaries) / len(salaries)
  for (bucket, salaries) in salary_by_tenure_bucket.items()
}


interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Lowercase each interest, split it into words, count the results
# words = []
# for (user_id, interest) in interests:
#   words += interest.lower().split()

# words_and_counts = Counter(words)

words_and_counts = Counter(
  word
  for (user_id, interest) in interests
    for word in interest.lower().split()
)

for (word, count) in words_and_counts.most_common():
  if count > 1:
    print(word, count)