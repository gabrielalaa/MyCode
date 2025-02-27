def removeKeySpaces(input_dict):
    output_dict = {}
    # Create lists to save the key which repeats and its values
    save_data = []
    duplicate = []
    for key, values in input_dict.items():
        # Remove spaces from the dict keys
        key = ''.join(key.split())
        # If the key already exists, save the values and the repeated key in lists
        if key in output_dict:
            duplicate.append(key)
            save_data.append(output_dict[key])
        # Update the dictionary
        output_dict.update({key: values})

    # This will print the last update of the dictionary
    print(f"The last update of the dictionary is: {output_dict}")

    # If we have duplicates
    if len(duplicate) > 0:
        # For each key which repeats in our dictionary, change its values and print the other possible (previous) output
        for i in range(len(duplicate)):
            if duplicate[i] in output_dict.keys():
                output_dict[duplicate[i]] = save_data[i]
                print(f"Another output is: {output_dict}")


my_dict = {'a b c': [2, 3, 5],
            'b d e': [1, 8, 4],
            'c f g': [9, 0, 1],
            'bd e': [100, 10, 1]}

removeKeySpaces(my_dict)