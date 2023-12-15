month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) and month==2:
    return month_days[1] + 1
  else:
    return month_days[month-1]

#code has gotten so much better!
