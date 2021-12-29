all_restaurants = [
    "Taco City",
    "Burgertown",
    "Tacovilla",
    "Hotdog station",
    "House of tacos",
]

def tacos_only(restaurants):
    taco_joints = restaurants.copy()
    # taco_joints is now a copy of the original list
    for taco_joint in taco_joints.copy():
        #this iterates through a copy of taco_joints, meaning no iterations will be missed
        if "taco" not in taco_joint.lower():
            taco_joints.remove(taco_joint)
            #this removes the restaurant that doesn't have 'taco' from taco_joints (OG) without missing any iterations
        return taco_joints

dinner_options = tacos_only(all_restaurants)
