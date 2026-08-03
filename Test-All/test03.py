

kilometers=float(input("Enter values in kilometers:"))

one_km=0.621371
miles=kilometers* one_km

print("%.2f kilometers is = %.2f miles" %(kilometers,miles))
print("{:.2f} kilometers is = {:.2f} miles".format(kilometers,miles))
print(f"{kilometers:.2f} kilometers is + {miles:.2f} miles")