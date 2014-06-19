TESTS = {
    "Basics": [
        {
            "input": [[0, 1, 0, 1, 0, 1], [1, 8, 1, 0, 0, 0], [0, 1, 2, 0, 0, 1], [1, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 3, 1], [1, 0, 1, 0, 1, 2]],
            "answer": 8,
            "explanation": {0: 0, 1: 0, 2: 2, 3: 0, 4: 1, 5: 0},
        },
        {
            "input": [[0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0], [0, 1, 2, 0, 0, 1], [1, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 3, 1], [1, 0, 1, 0, 1, 2]],
            "answer": 4,
            "explanation": {0: 0, 1: 0, 2: 1, 3: 0, 4: 1, 5: 0},
        },
        {
            "input": [[0, 1, 1], [1, 9, 1], [1, 1, 9]],
            "answer": 9,
            "explanation": {0: 0, 1: 0, 2: 0},
        },
    ],
    "Extra": [
        {
            "input": [[0, 1, 0, 1, 0, 0],
                      [1, 8, 1, 0, 0, 0],
                      [0, 1, 2, 0, 0, 1],
                      [1, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 3, 1],
                      [0, 0, 1, 0, 1, 2]],
            "answer": 8,
        },
        {
            "input": [[0, 1, 0, 1, 0, 0],
                      [1, 1, 1, 0, 0, 0],
                      [0, 1, 2, 0, 0, 1],
                      [1, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 3, 1],
                      [0, 0, 1, 0, 1, 2]],
            "answer": 4,
        },
        {
            "input": [[0, 1, 1],
                      [1, 9, 1],
                      [1, 1, 9]],
            "answer": 9,
        }
    ]
}
