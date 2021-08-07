import camelot

# PDF file to extract tables from
file = "100100502_AES01267KY_ORG_Financial-Statement_2020.pdf"
# extract all the tables in the PDF file
tables = camelot.read_pdf(file)
# or export all in a zip
print("Total tables extracted:", tables.n)
tables.export("foo.csv", f="csv", compress=True)