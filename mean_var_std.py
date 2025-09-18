import numpy as np

def calculate(list):
    # Validate input length
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(list).reshape((3,3))
    
    # Calculate statistics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # columns
            matrix.mean(axis=1).tolist(),  # rows
            matrix.mean().tolist()         # flattened
        ],
        'variance' : [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation' : [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist(),
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # columns
            matrix.max(axis=1).tolist(),   # rows
            matrix.max().tolist()          # flattened
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # columns
            matrix.min(axis=1).tolist(),   # rows
            matrix.min().tolist()          # flattened
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # columns
            matrix.sum(axis=1).tolist(),   # rows
            matrix.sum().tolist()          # flattened
        ]
    }
    
    return calculations