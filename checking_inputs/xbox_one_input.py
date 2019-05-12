from inputs import get_gamepad


def controller_status():
    """
    function checks for controller inputs
    """
    while True:
        events = get_gamepad()
        for event in events:
            print("code")
            print(event.code)
            print('-------------')
            print("state")
            print(event.state)


if __name__ == "__main__":
    controller_status()
