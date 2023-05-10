"""
Your colleagues have been looking over you shoulder. When you should have been doing your
boring real job, you've been using the work computers to smash in endless hours of codewars.
In a team meeting, a terrible, awful person declares to the group that you aren't working.
You're in trouble. You quickly have to gauge the feeling in the room to decide whether or not
you should gather your things and leave.
Given an object (meet) containing team member names as keys, and their happiness rating out
 of 10 as the value, you need to assess the overall happiness rating of the group. If <= 5,
 return 'Get Out Now!'. Else return 'Nice Work Champ!'.
Happiness rating will be total score / number of people in the room.
Note that your boss is in the room (boss), their score is worth double it's face value
(but they are still just one person!).
"""


def outed(meet, boss):
    meet[boss] = meet[boss] * 2
    sum_of_values = sum(meet.values())
    sum_of_keys = len(meet.keys())
    rating = sum_of_values / sum_of_keys
    if rating <= 5:
        return "Get Out Now!"
    else:
        return 'Nice Work Champ!'


# def outed(meet, boss):
#     return 'Get Out Now!' if (sum(meet.values()) + meet[boss] ) / len(meet) <= 5 else 'Nice Work Champ!'

# def outed(meet, boss):
# return 'Get Out Now!' if sum(meet[person] if not person == boss else meet[person] * 2 for person in meet) / len(meet) <= 5 else 'Nice Work Champ!'

# print(outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2,
#          'mr':0}, 'laura'), 'Get Out Now!')
# print(outed({'tim':1, 'jim':3, 'randy':9, 'sandy':6, 'andy':7, 'katie':6, 'laura':9, 'saajid':9, 'alex':9, 'john':9,
#          'mr':8}, 'katie'), 'Nice Work Champ!')
# print(outed({'tim':2, 'jim':4, 'randy':0, 'sandy':5, 'andy':8, 'katie':6, 'laura':2, 'saajid':2, 'alex':3, 'john':2,
#          'mr':8}, 'john'),'Get Out Now!')

"""
Every now and then people in the office moves teams or departments. 
Depending what people are doing with their time they can become more or less boring.
 Time to assess the current team.

You will be provided with an object(staff) containing the staff names as keys, 
and the department they work in as values.

Each department has a different boredom assessment score, as follows:

accounts = 1
finance = 2
canteen = 10
regulation = 3
trading = 6
change = 6
IS = 8
retail = 5
cleaning = 4
pissing about = 25

Depending on the cumulative score of the team, return the appropriate sentiment:

<=80: 'kill me now'
< 100 & > 80: 'i can handle this'
100 or over: 'party time!!'
"""


# def b(staff):
#     dictscores = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3,
#                   'trading': 6, 'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}
#     resd = {}
#     for d in dictscores:
#         cnt = 0
#         for s in staff.values():
#             if d == s:
#                 cnt += 1
#         resd.update({d: dictscores[d] * cnt})
#     res = sum(resd.values())
#     if res <= 80:
#         return 'kill me now'
#     elif 100 > res > 80:
#         return 'i can handle this'
#     else:
#         return 'party time!!'

def boredom(staff):
    dictscores = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3,
                  'trading': 6, 'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}
    resd = sum([dictscores[i] for i in staff.values()])
    if resd < 80:
        return "kill me now"
    elif 100 > resd > 80:
        return 'i can handle this'
    else:
        return 'party time!!'


print(boredom({"tim": "change", "jim": "accounts",
               "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
               "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
               "mr": "finance"}), "kill me now")
print(boredom({"tim": "IS", "jim": "finance",
               "randy": "pissing about", "sandy": "cleaning", "andy": "cleaning",
               "katie": "cleaning", "laura": "pissing about", "saajid": "regulation",
               "alex": "regulation", "john": "accounts", "mr": "canteen"}), "i can handle this")
print(boredom({"tim": "accounts", "jim": "accounts",
               "randy": "pissing about", "sandy": "finance", "andy": "change",
               "katie": "IS", "laura": "IS", "saajid": "canteen", "alex": "pissing about",
               "john": "retail", "mr": "pissing about"}), "party time!!")


def boRedom(staff):
    lookup = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25
    }
    n = sum(lookup[s] for s in staff.values())
    if n <= 80:
        return "kill me now"
    if n < 100:
        return "i can handle this"
    return "party time!!"


scores = {
    "accounts": 1, "finance": 2, "canteen": 10, "regulation": 3, "trading": 6,
    "change": 6, "IS": 8, "retail": 5, "cleaning": 4, "pissing about": 25
}


def boredoM(staff):
    score = sum(scores[activity] for activity in staff.values())
    return "party time!!" if score >= 100 else "i can handle this" if score > 80 else "kill me now"


"""
Your job at E-Corp is both boring and difficult. It isn't made any easier by the fact that everyone constantly 
wants to have a meeting with you, and that the meeting rooms are always taken!

In this kata, you will be given an array. Each value represents a meeting room. Your job? Find the first empty 
one and return its index (N.B. There may be more than one empty room in some test cases).

'X' --> busy
'O' --> empty
"""


def meeting(rooms):
    if "O" in rooms:
        return rooms.index("O")
    else:
        return 'None available!'


# print(meeting(['X', 'O', 'X']), 1)
# print(meeting(['O', 'X', 'X', 'X', 'X']), 0)
# print(meeting(['X', 'X', 'O', 'X', 'X']), 2)
# print(meeting(['X']), 'None available!')

def meetinG(rooms):
    try:
        return rooms.index('O')
    except ValueError:
        return 'None available!'


"""
The bloody photocopier is broken... Just as you were sneaking
 around the office to print off your favourite binary code!

Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.

Given a string of binary, return the version the photocopier gives you as a string.
"""


def broken(inp):
    res = ""
    for i in inp:
        res += '1' if i == '0' else '0'
    return res


def bRoken(inp):
    """Replace each '0' with '1' and vice versa."""
    return inp.translate(str.maketrans("01", "10"))


def brokEn(inp):
    d = {"1": "0", "0": "1"}
    return "".join([d[i] for i in str(inp)])


brokeN = lambda s: s.translate({48: "1", 49: "0"})

"""
So you've found a meeting room - phew! You arrive there ready to present, and find that someone has taken
 one or more of the chairs!! You need to find some quick.... 
 check all the other meeting rooms to see if all of the chairs are in use.

Your meeting room can take up to 8 chairs. need will tell you how many have been taken. You need to find that many.

Find the spare chairs from the array of meeting rooms. Each meeting room tuple will 
have the number of occupants as a string. Each occupant is represented by 'X'. 
The room tuple will also have an integer telling you how many chairs there are in the room.

You should return an array of integers that shows how many chairs you take from each room in order,
 up until you have the required amount.

example:

[['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9], ['XXX',2]] when you need 4 chairs:

result -> [0, 1, 3] no chairs free in room 0, take 1 from room 1, take 3 from room 2.
 no need to consider room 3 as you have your 4 chairs already.

If you need no chairs, return "Game On". If there aren't enough spare chairs available, return "Not enough!".
"""


def meeting2(rooms, need):
    resd = []
    if need == 0:
        return 'Game On'
    for r in rooms:
        kilk = r[1] - len(r[0])
        if need >= kilk > 0:
            resd.append(kilk)
            need -= kilk
        elif kilk >= need > 0:
            resd.append(need)
            return resd
        elif need > 0:
            resd.append(0)
    return 'Not enough!' if need >0 else resd


# print(meeting2([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4), [0, 1, 3])
# print(meeting2([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5), [0, 0, 1, 2, 2])
# print(meeting2([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 0), "Game On")
# print(meeting2([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 8), "Not enough!")
# print(meeting2([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 2), [0, 2])
# print(meeting2([['X', 4], ['XXXXXXX', 6], ['X', 5], ['XXX', 1], ['XXXXXXX', 1]], 5), [3, 0, 2])
# print(meeting2([['XXXXXXXX', 2], ['X', 2], ['XXXXXXXXX', 6], ['XX', 8], ['X', 7], ['', 5], ['XXXXXX', 3]], 1), 'should equal [0, 1]')
# print(meeting2([['XXXX', 7], ['X', 10], ['XXXXXXXXX', 7], ['XXXX', 4], ['XXXXXX', 3], ['XXXXX', 1], ['XXXXXXX', 0],
#                 ['XXXXX',7], ['XXXXXXXXXX', 8], ['XXXX', 8]], 3), 'should equal [3]' )
# print(meeting2([['X', 4], ['XXXXXX', 0], ['XXXXX', 4], ['XXXXXXXXXX', 10], ['XXX', 2], ['XX', 7], ['XXXXXXXXX', 6],
#                 ['XXXXX', 6],['X', 9]], 8), [3, 0, 0, 0, 0, 5])
# print(meeting2([['XXXXXX', 2], ['XXX', 1], ['XXXXXX', 8]], 4), 'Not enough!')


def mEeting(rooms, need):
    if need == 0: return "Game On"

    result = []
    for people, chairs in rooms:
        taken = min(max(chairs - len(people), 0), need)
        result.append(taken)
        need -= taken
        if need == 0: return result

    return "Not enough!"

print(mEeting([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5), [0, 0, 1, 2, 2])


def meEtinG(rooms, need):
    if need == 0:
        return "Game On"
    take = []
    for people, seat in rooms:
        take.append(min(need, max(0, seat - len(people))))
        need -= take[-1]
        if need == 0:
            return take
    return "Not enough!"

def meetIng(rooms, n):
    if n==0: return "Game On"
    chairs, res = (max(0, chair - len(occ)) for occ, chair in rooms), []
    for c in chairs:
        if c >= n: return res+[n]
        res.append(c)
        n -= c
    return "Not enough!"



