import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

#number of responses for Ceballos
total_ceballos = survey_responses.count("Ceballos")
total_all = len(survey_responses)
print(total_ceballos)
print(total_all)
#% of ceballos-votes
percentage_ceballos = 100*total_ceballos/total_all
print(percentage_ceballos)
#our survey as binomial distribution example
possible_surveys=np.random.binomial(total_all, 0.54, size=10000) / float(total_all)
#plot the results
plt.hist(possible_surveys, 20, (0,1))
plt.show()
ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print(ceballos_loss_surveys)

#simulating a larger survey
large_survey = np.random.binomial(7000, 0.54, 10000) / 7000.
print()
print(large_survey)
ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new)

#thus it becomes clear that a larger survey makes the results way more accurate
