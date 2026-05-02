import ast

def parse_prediction(prediction):
    """
    Converts model output string into list of tuples
    """
    try:
        return ast.literal_eval(prediction[0])
    except Exception as e:
        return [("Error parsing prediction", str(e))]


def chunk_list(data, chunk_size=10):
    """
    Splits list into chunks (used for table rendering)
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]