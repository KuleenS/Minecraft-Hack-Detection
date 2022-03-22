from scipy.interpolate import interp1d

def interpolate(timeseries_group : tuple, min: int, max: int):
    times = timeseries_group[0]
    time_series = timeseries_group[1:]
    interpolated_time_series = []
    interpolated_time_series.append(list(range(min, max+1)))
    for series in time_series:
        f = interp1d(times, series)
        new_series = []
        for i in range(min, max+1):
            new_series.append(f(i))
        interpolated_time_series.append(new_series)
    return interpolated_time_series
        
