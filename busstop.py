a3_bus = {
    'bus 130': [0, 10, 20, 30, 40, 50],
    'bus 146': [3, 13, 23, 33, 43, 53],
    'bus 156': [6, 16, 26, 36, 46, 56],
    'bus 75': [7, 17, 27, 37, 47, 57],
    'bus 101': [8, 18, 28, 38, 48, 58],
    'bus 34': [9, 19, 29, 39, 49, 59],
}


def bus_timing(bus_stop, minutes):
    for value in bus_stop:
        if value >= minutes:
            next_time = value
            result = next_time - minutes
            print(f"Bus come in: {result} min.")
            return result
    print('Today there are no more buses.')
    return -1


def main():
    print("Bus schedule for 8 am. Arrival time is indicated in minutes:")
    for bus, schedule in a3_bus.items():
        print(f"{bus}:{schedule}")
    print('\n')

    your_bus = input("Enter your bus: ")
    if your_bus in a3_bus:
        selected_bus = a3_bus[your_bus]
    else:
        print("Invalid bus selection. Choose bus from list.")
        return

    your_time = int(input("Enter your time (8:XX): "))
    if 0 <= your_time < 60:
        pass
    else:
        print("Enter minutes from 1 to 59")
        return

    bus_timing(selected_bus, your_time)


def test_bus_timing():
    result1 = bus_timing(a3_bus['bus 34'], 8)
    assert result1 == 1

    result2 = bus_timing(a3_bus['bus 75'], 10)
    assert result2 == 7

    result3 = bus_timing(a3_bus['bus 130'], 10)
    assert result3 == 0

    result4 = bus_timing(a3_bus['bus 130'], 9)
    assert result4 == 1

    print("Asserts passed.")


if __name__ == "__main__":
    main()
    test_bus_timing()
