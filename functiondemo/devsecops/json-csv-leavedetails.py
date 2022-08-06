import json
import os
import pandas


def read_json(filename: str) -> dict:
	try:
		with open(filename, "r") as f:
			data = json.loads(f.read())
	except:
		raise Exception(f"Reading {filename} file encountered an error")
	return data


def create_dataframe(data: list) -> pandas.DataFrame:
	# Declare an empty dataframe to append records
	dataframe = pandas.DataFrame()
	# Looping through each record
	for d in data:
		# Normalize the column levels
		record = pandas.json_normalize(d)
		# Append it to the dataframe
		dataframe = dataframe.append(record, ignore_index=True)
	return dataframe


def main():
	# Read the JSON file as python dictionary
  data = read_json(filename="leavedetails.json")
  #os.remove("details.csv")
	# Generate the dataframe for the array items in
	# details ke
  i = 0
  count = sum([len(data['Results'])])
  print(count)

  while i < count:
      print(i)
      dataframe = create_dataframe(data=data['Results'][i]['Vulnerabilities'])
      dataframe.to_csv("leavedetails" + str(i) + ".csv", index=False)
      i += 1


if __name__ == '__main__':
	main()

