# hour = int(input("Starting time (hours): "))
start_hours = 12
# mins = int(input("Starting time (minutes): "))
start_minutes = 17
# dura = int(input("Event duration (minutes): "))
duration_minutes = 59

end_hours = (start_hours + (start_minutes + duration_minutes) // 60) % 24
end_minutes = (start_minutes + duration_minutes) % 60

print(f"Закінчення годин {end_hours:02}:{end_minutes:02}")
