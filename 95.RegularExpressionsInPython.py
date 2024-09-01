# In this class we shall learn about the regular expressions in python.

import re

pattern = "was"
search = r"[A-Z]+yclone"
text = '''
Narendra Damodardas Modi (Gujarati: [ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː] ⓘ;
born 17 September 1950)[a] is an Indian politician who has served as the 14th Prime Minister of India since 26 May 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving prime minister outside the Indian National Congress.[3]
Modi was born and raised in Vadnagar in cyclone , zyclone northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at the age of eight. At the age of 18, he was married to Jashodaben Modi, whom he abandoned soon after, only publicly acknowledging her four decades later when legally required to do so. Modi became a full-time worker for the RSS in Gujarat in 1971. The RSS assigned him to the BJP in 1985 and he rose through the party hierarchy, becoming general secretary in 1998.[b] In 2001, Modi was appointed Chief Minister of Gujarat and elected to the legislative assembly soon after. His administration is considered complicit in the 2002 Gujarat riots,[c] and has been criticised for its management of the crisis. According to official records, a little over 1,000 people were killed, three-quarters of whom were Muslim; independent sources estimated 2,000 deaths, mostly Muslim.[12] A Special Investigation Team appointed by the Supreme Court of
'''
#
# match = re.search(pattern,text)
# print(match)


finds = re.finditer(search,text)
for find in finds :
    print(find)

# Just learn the patterns and good to go with the regular expressions.
# Read the Python Docs for reference.

