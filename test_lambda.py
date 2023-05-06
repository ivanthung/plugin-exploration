from lambda_function import lambda_handler

sample_event1 = {
    "body": '{"message": "Hello World", "plugin": "reverse"}',
    "httpMethod": "POST",
    "headers": {"Content-Type": "application/json"},
}

sample_event2 = {
    "body": '{"message": "Hello World", "plugin": "capitalize"}',
    "httpMethod": "POST",
    "headers": {"Content-Type": "application/json"},
}

sample_event3 = {
    "body": '{"message": "Hello World", "plugin": "eric"}',
    "httpMethod": "POST",
    "headers": {"Content-Type": "application/json"},
}


if __name__ == '__main__':

    result1 = lambda_handler(sample_event1, {})
    print("Result for event 1:", result1)

    result2 = lambda_handler(sample_event2, {})
    print("Result for event 2:", result2)

    result3 = lambda_handler(sample_event3, {})
    print("Result for event 3:", result3)