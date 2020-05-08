#THE BORDERLESS TOURIST

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wikes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    destination_index = None
    for i in destinations:
        if i == destination:
            destination_index = destinations.index(i)
    return destination_index

print(get_destination_index("Los Angeles, USA"))

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    if destination_index == None:
        return
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attractions_for_destination

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)