
resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

def display_resources(resources):
    for resource in resources:
        print("ID:", resource[0])
        print("Name:", resource[1])
        print("Category:", resource[2])
        print("Available Quantity:", resource[3])
        print()

display_resources(resources)