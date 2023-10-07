filenames = ("1.Raw Data.txt", "2.Cleaned Data.txt", "3.Analyzed Data.txt", "4.Presentation.txt", "5.Report.txt")
for filename in filenames:
    index = filename.index(".")
    a = filename.replace(".", "_")
    print(a)
