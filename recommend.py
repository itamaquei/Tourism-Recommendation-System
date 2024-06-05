# recommend.py
import random

my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}

# Get a random key-value pair
tourism_places = {
    "Osun-Osogbo Sacred Grove": ["at pretty might street along princess hostel", "open at 9", "close at 10"],
    "Osogbo Grand Hotel": ["5-star luxury hotel", "open 24/7"],
    "Taste of Osogbo": ["local restaurant", "open from 8 AM to 10 PM"],
    "Osun Osogbo Carnival": ["annual cultural festival", "held every August"]
}

tourist_attractions = {
    "Oshun Shrine": "The Oshun Shrine is one of the most important religious sites in Oshogbo. It is dedicated to the Yoruba goddess of fertility and love, and is a popular pilgrimage site for worshippers from all over the world. The shrine is home to a number of sacred artifacts, including a bronze statue of Oshun, a stone altar, and a sacred pool.",
    "Osun Sacred Grove": "The Osun Sacred Grove is a UNESCO World Heritage Site and is home to one of the most important religious sites in Nigeria. It is a forested area dedicated to the Yoruba goddess of fertility and is home to a number of shrines and sacred artifacts. Visitors can take a guided tour of the grove and learn about the history and culture of the Yoruba people.",
    "Ipole Ille Rainforest": "Ipole Ille is a lush rainforest located in Oshogbo. It is home to a number of endangered species, including the African elephant, the African wild dog, and the African lion. Visitors can explore the rainforest on guided tours and spot some of the wildlife that inhabits the area.",
    "Oke Idanre": "Oke Idanre is a mountain located in the Ondo State of Nigeria. It is home to a number of ancient sites, including the Idanre Hills which are believed to be over 5,000 years old. Visitors can explore the area on guided tours and learn about the history and culture of the Idanre people.",
    "Olumirin Waterfalls": "The Olumirin Waterfalls are located in the Erin-Ijesha National Park and are one of the most beautiful waterfalls in Nigeria. The falls cascade down the rocky cliffs and are a great spot for swimming and taking in the stunning views.",
    "Erin-Ijesha National Park": "The Erin-Ijesha National Park is located in the Osun State of Nigeria and is home to a number of endangered species, including the African elephant, the African wild dog, and the African lion. Visitors can explore the park on guided tours and spot some of the wildlife that inhabits the area.",
    "Osun Osogbo Festival": "The Osun Osogbo Festival is an annual festival held in Oshogbo to honor the Yoruba goddess of fertility. The festival includes traditional music and dance, and is a great opportunity to experience the culture and traditions of the Yoruba people.",
    "Olumirin Sacred Pool": "The Olumirin Sacred Pool is located in the Osun State of Nigeria and is a popular pilgrimage site for worshippers from all over the world. The pool is believed to have healing powers and is a great spot to take a dip and soak in the spiritual energy of the area.",
    "Sabo Market": "The Sabo Market is one of the largest markets in Oshogbo and is a great place to pick up traditional crafts and souvenirs. Visitors can browse through the stalls and find a variety of items, from clothing to jewelry to traditional artifacts.",
    "Ooni Palace": "The Ooni Palace is the official residence of the Ooni of Ife, the traditional ruler of the Yoruba people. The palace is a great spot to take in the history and culture of the area and is a popular tourist destination.",
    "National Museum of Oshogbo": "The National Museum of Oshogbo is a great spot to learn about the history and culture of the area. The museum houses a variety of artifacts, including traditional art and sculptures, and is a great place to explore the history of Oshogbo.",
    "Osun Osogbo Sacred Grove": "The Osun Osogbo Sacred Grove is a UNESCO World Heritage Site and is home to one of the most important religious sites in Nigeria. The grove is home to a number of shrines and sacred artifacts and is a great place to explore the culture and history of the Yoruba people.",
    "Osun Shrine": "The Osun Shrine is located in the Osun State of Nigeria and is dedicated to the Yoruba goddess of fertility and love. The shrine is home to a number of sacred artifacts, including a bronze statue of Oshun, a stone altar, and a sacred pool.",
    "Ogbere Beach": "Ogbere Beach is located in the Osun State of Nigeria and is a great spot to take in the stunning views of the Atlantic Ocean. The beach is a popular spot for swimming and sunbathing and is a great place to relax and enjoy the beauty of the area.",
    "Oke-Igbo": "Oke-Igbo is a mountain located in the Osun State of Nigeria and is home to a number of ancient sites, including the Idanre Hills which are believed to be over 5,000 years old. Visitors can explore the area on guided tours and learn about the history and culture of the Idanre people.",
    "Ile-Ife Museum": "The Ile-Ife Museum is located in the Osun State of Nigeria and is a great spot to learn about the history and culture of the area. The museum houses a variety of artifacts, including traditional art and sculptures, and is a great place to explore the history of Oshogbo.",
    "Iwo Road Market": "The Iwo Road Market is one of the oldest markets in Oshogbo and is a great place to pick up traditional crafts and souvenirs. Visitors can browse through the stalls and find a variety of items, from clothing to jewelry to traditional artifacts.",
    "Oke-Afa": "Oke-Afa is a mountain located in the Osun State of Nigeria and is home to a number of ancient sites, including the Idanre Hills which are believed to be over 5,000 years old. Visitors can explore the area on guided tours and learn about the history and culture of the Idanre people.",
    "Ijebu-Ode": "Ijebu-Ode is a city located in the Osun State of Nigeria and is home to a number of ancient sites, including the Idanre Hills which are believed to be over 5,000 years old. Visitors can explore the area on guided tours and learn about the history and culture of the Idanre people.",
    "Osun State University": "The Osun State University is located in the Osun State of Nigeria and is a great spot to learn about the history and culture of the area. The university houses a variety of artifacts, including traditional art and sculptures, and"
}


def generate_recommendations(interests, budget, duration, previous_experiences):
    recommendations = []
    for place, details in tourism_places.items():
        recommendations.append(f"{place}: {', '.join(details)}")
    return "\n\n".join(recommendations)


def generate_recommendations2(interests=0, budget=0, duration=0, previous_experiences=0):
    # Get a list of random key-value pairs as strings
    num_pairs = 1
    if num_pairs >= 2:
        random_pairs = random.sample(
            list(tourist_attractions.items()), num_pairs)
        random_pairs_str = ""
        for pair in random_pairs:
            random_pairs_str += f"{"____" *
                                   10}\n-{pair[0]}:\n\t{pair[1]}\n\n"
        # Output: "cherry:\n\t\t8\napple:\n\t\t5" or some other combination
        # print(random_pairs_str.strip())
        recommendations = random_pairs_str
    else:
        random_pair = random.choice(list(tourist_attractions .items()))
        recommendations = f"-{random_pair[0]}:\n\t{random_pair[1]}"

    recommendations = f"Based on your interests ({interests}), budget ({budget}), duration ({
        duration} days, and previous experiences ({previous_experiences}), we recommend: \n\n{recommendations}"
    print(recommendations)
    return recommendations


# generate_recommendations2()
