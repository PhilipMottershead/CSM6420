from entropy import calulate_entropy

overall_probabiity_values  = [9/14,5/14]
overall_entropy = calulate_entropy(overall_probabiity_values)

# Varible spsefic 
humidity_high  = [3/7,4/7]
humidity_normal  = [6/7,1/7]
outlook_sunny = [2/5,3/5]
outlook_rain = [3/5,2/5]
outlook_overcast = [1]
temperature__hot = [2/4,2/4]
temperature__mild = [4/6,2/6]
temperature__cool = [3/4, 1/4]
wind_weak = [6/8,2/8]
wind_strong = [3/6,3/6]

# Probabilites of varibles
wind_strong_prob = 6/14
wind_weak_prob = 8/14
temperature_cool_prob = 4/14
temperature_hot_prob = 4/14
temperature_mild_prob = 6/14
outlook_overcast_prob = 4/14
outlook_rain_prob = 5/14
outlook_sunny_prob = 5/14
humidity_high_prob = 7/14
humidity_normal_prob = 7/14 


humidity_high_entropy = calulate_entropy(humidity_high)
humidity_normal_entropy = calulate_entropy(humidity_normal)

outlook_overcast_entropy = calulate_entropy(outlook_overcast)
outlook_rain_entropy = calulate_entropy(outlook_rain)
outlook_sunny_entropy = calulate_entropy(outlook_sunny)

wind_strong_entropy = calulate_entropy(wind_strong)
wind_weak_entropy = calulate_entropy(wind_weak)

temperature__cool_entropy = calulate_entropy(temperature__cool)
temperature__hot_entropy = calulate_entropy(temperature__hot)
temperature__mild_entropy = calulate_entropy(temperature__mild)

wind_prob = [wind_strong_prob,wind_weak_prob]
humidity_prob = [humidity_high_prob,humidity_normal_prob]
temperature_prob = [temperature_cool_prob,temperature_mild_prob,temperature_cool_prob]
outlook_prob = [outlook_overcast_prob,outlook_rain_prob,outlook_sunny_prob]

humidity_entropy = [humidity_high_entropy,humidity_normal_entropy]
wind_entropy = [wind_strong_entropy,wind_weak_entropy]
outlook_entropy = [outlook_overcast_entropy,outlook_rain_entropy,outlook_sunny_entropy]
temperature__entropy = [temperature__cool_entropy,temperature__mild_entropy,temperature__hot_entropy]

def calulate_information_gain(overall_entropy,probs,entropy):

    infomation_gain = overall_entropy
    
    for i in range(len(entropy)):
        gain = (probs[i] * entropy[i])
        infomation_gain = infomation_gain - gain
    return infomation_gain

print(calulate_information_gain(overall_entropy,humidity_prob,humidity_entropy))
print(calulate_information_gain(overall_entropy,wind_prob,wind_entropy))

print(calulate_information_gain(overall_entropy,temperature_prob,temperature__entropy))
print(calulate_information_gain(overall_entropy,outlook_prob,outlook_entropy))

