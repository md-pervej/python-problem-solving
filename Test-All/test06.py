
kilometers=float(input("Enter a value in kilometer:"))

one_km=0.621371
miles=kilometers*one_km
print("%.2f kilometers = %.2f miles"%(kilometers,miles))
print("{:.2f} kilometers = {:.2f}miles".format(kilometers,miles))
print(f"{kilometers:.2f} kilometers = {miles:.2f} miles")