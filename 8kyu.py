"""
Create a function that finds the integral of the expression passed.
In order to find the integral all you need to do is add one to the exponent (the second argument),
and divide the coefficient (the first argument) by that new number.
For example for 3x^2, the integral would be 1x^3: we added 1 to the exponent, and divided the coefficient by that new number).
Notes:
The output should be a string.
The coefficient and exponent is always a positive integer.
"""


def integral(a, b):
    return f'{int(a / (b + 1))}x^{b + 1}'


# Also works:
# exponent += 1
# coefficient /= exponent
# return '{}x^{}'.format(int(coefficient) if coefficient.is_integer() else coefficient, exponent)

print(integral(12, 5))

"""
You're writing code to control your town's traffic lights.
 You need a function to handle each change from green, to yellow, to red, and then to green again.
Complete the function that takes a string as an argument 
representing the current state of the light and returns a string representing
 the state the light should change to.

For example, when the input is green, output should be yellow.
"""


def update_light(current):
    l = ['green', 'yellow', 'red']
    return l[l.index(current) + 1] if l.index(current) < len(l) - 1 else l[0]


# return {"green": "yellow", "yellow": "red", "red": "green"}[current]
print(update_light('yellow'))

"""
As a member of the editorial board of the prestigous scientific Journal Proceedings
 of the National Academy of Sciences, you've decided to go back and review how well 
 old articles you've published stand up to modern publication best practices.
 Specifically, you'd like to re-evaluate old findings in light of recent literature
  about "researcher degrees of freedom".
You want to categorize all the old articles into three groups: "Fine", "Needs review"
 and "Pants on fire".

In order to categorize them you've enlisted an army of unpaid grad students to review 
and give you two data points from each study: (1) the p-value behind the paper's primary conclusions,
 and (2) the number of recommended author requirements to limit researcher degrees of freedom the authors satisfied:

* Authors must decide the rule for terminating data collection before data collection
 begins and report this rule in the article.
* Authors must collect at least 20 observations per cell or else provide a compelling
 cost-of-data-collection justification. 
* Authors must list all variables collected in a study.
* Authors must report all experimental conditions, including failed manipulations.
* If observations are eliminated, authors must also report what 
the statistical results are if those observations are included.
* If an analysis includes a covariate, authors must report 
the statistical results of the analysis without the covariate.
Your army of tenure-hungry grad students will give you the
 p-value as a float between 1.0 and 0.0 exclusive, and the
  number of author requirements satisfied as an integer from 0 through 6 inclusive.

You've decided to write a function, categorize_study() to automatically
 categorize each study based on these two inputs using the completely scientifically legitimate
  "bs-factor". The bs-factor for a particular paper is calculated as follows:

bs-factor when the authors satisfy all six requirements is 1
bs-factor when the authors satisfy only five requirements is 2
bs-factor when the authors satisfy only four requirements is 4
bs-factor when the authors satisfy only three requirements is 8...
Your function should multiply the p-value by the bs-factor and use that product to return one of the following strings:

product is less than 0.05: "Fine"
product is 0.05 to 0.15: "Needs review"
product is 0.15 or higher: "Pants on fire"
You've also decided that all studies meeting none of the author requirements
 that would have been categorized as "Fine" should instead be categorized as "Needs review".

For example:
categorize_study(0.01, 3) should return "Needs review" because the p-value times the bs-factor is 0.08.
categorize_study(0.04, 6) should return "Fine" because the p-value times the bs-factor is only 0.04.
categorize_study(0.0001, 0) should return "Needs review" even though the p-value times the bs-factor is only 0.0064.
categorize_study(0.012, 0) should return "Pants on fire" because the p-value times the bs-factor is 0.768.
"""

print(0.0001 * 0)


def categorize_study(p_value, requirements):
    dict_of_bs_req = {6: 1, 5: 2, 4: 4, 3: 8, 2: 16, 1: 32, 0: 64}
    bs = dict_of_bs_req[requirements]
    res = p_value * bs
    print(res)
    if res < 0.05 and p_value > 0.0009:
        return "Fine"
    elif 0.05 < res < 0.15 or (p_value < 0.0009 and res < 0.05):
        return "Needs review"
    elif res >= 0.15:
        return "Pants on fire"


print(categorize_study(0.0001, 0))

def cat_best_sol(p_value, requirements):
    study_value = p_value * (2 ** (6 - requirements))

    if study_value < 0.05 and requirements != 0:
        return "Fine"
    elif study_value < 0.05 and requirements == 0:
        return "Needs review"
    elif study_value > 0.05 and study_value < 0.15:
        return "Needs review"
    else:
        return "Pants on fire"

print(cat_best_sol(0.0001, 0))


"""
You like the way the Python + operator easily handles adding different numeric types,
 but you need a tool to do that kind of addition without killing your program with 
 a TypeError exception whenever you accidentally try adding incompatible types
  like strings and lists to numbers.
You decide to write a function my_add() that takes two arguments. 
If the arguments can be added together it returns the sum.
 If adding the arguments together would raise an error the function should return None instead.
For example, my_add(1, 3.414) would return 4.414, but my_add(42, 
" is the answer.") would return None.
Hint: using a try / except statement may simplify this kata.
"""

def my_add(a, b):
    try:
        res = a+b
    except TypeError:
        return None
    return res
print(my_add(3,4))

print('++++++++++++++++++')

def main_decor(*args):
    print(sum(args))
    def decoratior(fn):
        print(sum(args)/len(args))
        def wrapper(a,b):
            print("we are here")
            fn(a,b)
            print("last thing")
            print('args:', str(args)[1:-1])
            return fn(a,b)

        return wrapper
    return decoratior

@main_decor(2,4,6)
def addition(a,b):
    print("what")
    return a+b

print(addition(7,10))

print("+++++++++++++++++++++++")