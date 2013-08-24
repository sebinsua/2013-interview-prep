def avg_stopwatch(laptime1, laptime2):
    """Write a function that accepts two lap times and calculates their average, returning the result in the same
        string format.
        For example, given the strings "00:02:20" and "00:04:40" the function would return "00:03:30".
        """

    # Python time does not seem to support centiseconds, so...
    m1, s1, hs1 = map(int, laptime1.split(":"))
    m2, s2, hs2 = map(int, laptime2.split(":"))

    average_in_hundredths = ((hs1 + hs2)
                             + (100 * (s1 + s2))
                             + (6000 * (m1 + m2))) // 2   # We don't need more granularity
    total_secs, hundredths = divmod(average_in_hundredths, 100)
    minutes, secs = divmod(total_secs, 60)

    return "{minutes:02d}:{seconds:02d}:{hundredths:02d}".format(minutes=minutes, seconds=secs, hundredths=hundredths)


if __name__ == "__main__":
    print avg_stopwatch("00:02:20", "00:04:40")
    print avg_stopwatch("00:59:00", "01:01:00")
    print avg_stopwatch("01:00:00", "02:00:00")
