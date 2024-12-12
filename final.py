class Rectangle:
    # Constructor to initialize width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #Set the width
    def set_width(self, width):
        self.width = width

    #Get the width
    def get_width(self):
        return self.width

    #Set the height
    def set_height(self, height):
        self.height = height

    #Get the height
    def get_height(self):
        return self.height

    # Method to calculate the perimeter of the rectangle
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    # Method to calculate the area of the rectangle
    def calculate_area(self):
        return self.width * self.height

    # Method to display the details of the rectangle
    def display(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")


if __name__ == "__main__":
    rect = Rectangle(5, 10)
    rect.display()


def count_frequencies(input_strings):
    # Initialize an empty dictionary to store word frequencies
    frequency_dict = {}
    
    # Iterate over each word in the input list
    for word in input_strings:
        # If the word is already in the dictionary, increment its count
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            # If the word is not in the dictionary, add it with a count of 1
            frequency_dict[word] = 1
    
    return frequency_dict

# Example usage
input_strings = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency_count = count_frequencies(input_strings)

print("Frequency Count:", frequency_count)
