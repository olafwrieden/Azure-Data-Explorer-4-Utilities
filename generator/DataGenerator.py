import json
from random import randint
from datetime import datetime, timedelta, timezone

class DataGenerator():
	def __init__(self, path, interval) -> None:
		self.path = path
		self.readInterval = interval
	
	def __repr__(self) -> str:
		# print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])
		return "DataGen: path='{}'".format(self.path)
	
	def generate(self, serial):
		print("Generating for: {} every {}mins".format(serial, self.readInterval))

		file = dict()
		file['type'] = 'meterdata'
		file['meter'] = self._constructMeter(serial)
		file['payload'] = self._constructPayload()
		return file
	
	def _constructMeter(self, serial):
		meter = dict()
		meter['serial'] = serial
		meter['version'] = 1.0
		meter['location'] = self._generateLocation()
		meter['configuration'] = self._generateConfig()
		return meter

	def _generateLocation(self):
		location = dict()
		location['latitude'] = "-27.4744023"
		location['longitude'] = "153.0337845"
		return location

	def _generateConfig(self):
		config = dict()
		config['readInterval'] = self.readInterval
		return config

	def _constructPayload(self):
		readings = self._constructReadings()

		payload = dict()
		payload['generatedAt'] = readings[0][-1].get('timestamp')
		payload['channels'] = self._constructChannels()
		payload['channelReadings'] = readings
		return payload

	def _constructChannels(self):
		names = ['PositiveActiveEnergy', 'NegativeActiveEnergy', 'PositiveReactiveEnergy', 'NegativeReactiveEnergy']
		
		channels = []
		for n in names:
			channel = dict()
			channel['name'] = n
			channels.append(channel)

		return channels

	def _constructReadings(self):
		channelReadings = []

		for i in range(4):
			# readings = dict()
			# readings['readings'] = self._genChannelReadings("2021-07-01T00:00:00.100")
			channelReadings.append(self._genChannelReadings("2021-07-01T00:00:00.100"))

		return channelReadings
	
	def _genChannelReadings(self, time_str):
		readings = [] # Data Structure

		given_time = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%f')
		final_time = datetime.strptime(str(given_time + timedelta(minutes=self.readInterval)).replace(" ", "T"), '%Y-%m-%dT%H:%M:%S.%f')

		# print("Creating data at '{}'".format(given_time))
		end_of_day = datetime(given_time.date().year, given_time.date().month, given_time.date().day, 23, 50, 10,10)
		# print(final_time.date().day , end_of_day.date().day)

		if final_time.date().day == end_of_day.date().day: #datetime.now().date(): #datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f'):
			reading = dict()
			reading['timestamp'] = str(given_time)[:-3].replace(" ", "T")
			reading['value'] = str(randint(0, 600))
			readings.append(reading)
			readings += self._genChannelReadings(str(final_time).replace(" ", "T"))
		
		return readings



if __name__ == "__main__":
	datagen = DataGenerator("../samples/", 15)

	for i in range(100):
		file = datagen.generate(str(i+1).zfill(5))
		genTime = (file.get('payload', {}).get('channelReadings', {})[0][-1].get('timestamp'))

		file_name = "meterdata-{}-{}.json".format(file.get('meter', {}).get('serial'), datetime.strptime(genTime, "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y%m%d%H%M%S"))
		with open('./samples/{}'.format(file_name), 'w') as f:
			json_string = json.dumps(file, default=lambda o: o.__dict__, sort_keys=False, indent=2)
			f.write(json_string)