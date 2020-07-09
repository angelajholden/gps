# lab_3_starting extra example...
#
# An interesting problem in probability...
# For a class of number students, calculate both theoretical and
#   experimental probabilities of NO two sharing the same birthday

import random

number = int(input("enter the number of students: "))

# first the theoretical prob:

# two accumulator variables
prob_of_unique_bdays = 1.0 # accumulates % probability of unique birthdays

days_still_available_for_unique_birthdays = 365 # after a birthday is picked at random, its no longer available

for count in range(1, number + 1):
    prob_of_unique_bdays = prob_of_unique_bdays * (days_still_available_for_unique_birthdays / 365)

    days_still_available_for_unique_birthdays -= 1

print("Theoretical probability that", number, "students all have unique birthdays is",
      prob_of_unique_bdays)

# Now the empirical prob:

NUM_TRIALS = 100000

num_with_unique_bdays = 0 # accumulate the number of trials having all unique birthdays

for count in range(NUM_TRIALS):

    # Generate a list of number random birthdays within the year
    # => uses a list comprehension: a compact 'functional' way of generating the list

    bdays = [random.randint(1, 365) for s in range(number)]

    # Python sets don't have duplicates, so casting list bdays to a set removes any duplicates

    unique_bdays = set(bdays)

    # If the set has the same # of elements as the list, there must have been...

    if len(unique_bdays) == number:
        # ...no duplicates in original list, so increment count

        num_with_unique_bdays += 1

# Out of NUM_TRIALS, we generated num_with_unique_bdays lists that had all unique birthdays:

# Finally compute the experimental probability == number of unique / total number

experimental_probability = num_with_unique_bdays / NUM_TRIALS

print("Experimentally-determined probability:", experimental_probability)

# How close are the two values?

print("Difference is:", abs(experimental_probability-prob_of_unique_bdays))
