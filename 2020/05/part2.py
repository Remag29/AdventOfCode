from part1 import calculate_place
from part1 import load_data

if __name__ == '__main__':
    # load data
    lines = load_data()

    # Get the places
    places = []
    for line in lines:
        places.append(calculate_place(line))

    # Create a list from 0 to 1023
    all_places = list(range(0, 1024))

    # Subtract the place ids from the list
    for place_id in places:
        all_places.remove(place_id)

    # Get min and max id from places id
    min_id = min(places)
    max_id = max(places)

    # Remove all ids under min_id and over max_id
    for i in range(0, min_id):
        if i in all_places:
            all_places.remove(i)

    for i in range(max_id, 1024):
        if i in all_places:
            all_places.remove(i)

    print("My place is: ", all_places[0])
