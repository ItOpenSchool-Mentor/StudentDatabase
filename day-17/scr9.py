# Script 6 : Traffic Light System

signal = input("Enter Signal Color[red/yellow/green] : ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Error: Invalid Signal Color!")
