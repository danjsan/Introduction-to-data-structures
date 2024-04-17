#Solution

#The following list has an impostor, find it, take it out of the list, expose it.

regular_list = ['orange','banana','grape','onion','peach','apple','kiwi']

#Hint: use the pop operation to get to onion and store it in one variable to later it print it as shown below


impostor = regular_list.pop()
impostor = regular_list.pop()
impostor = regular_list.pop()
impostor = regular_list.pop()

print(f'The impostor was {impostor}')