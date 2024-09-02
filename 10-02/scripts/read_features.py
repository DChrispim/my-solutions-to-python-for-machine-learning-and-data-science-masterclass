def read_feature_descriptions(file_path):
    """
    Reads the feature descriptions from the specified text file.

    Args:
        file_path (str): Path to the text file containing feature descriptions.

    Returns:
        dict: A dictionary where keys are feature names and values are their descriptions.
    """
    feature_dict = {}

    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                if line and ':' in line:
                    # Split feature name and description using ':'
                    feature_name, feature_desc = line.split(':', 1)
                    feature_dict[feature_name.strip()] = feature_desc.strip()

        return feature_dict

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None