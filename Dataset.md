# Understanding the Dataset

To expedite your ADX learning experience, a Python script has been included for the purpose of generating sample data in a format similar to that sent by a typical electicity meter.

**File Format:** `meterdata-[meter_id]-[date].json`
_Note:_ `Meter ID` and `Serial` are synonymous in our examples

## Generating a Dataset

1. Execute the Python script. This generates a set of meter data for a meter with 4 channels, and readings at a 15 minute intervals. By default, a single day's worth of data is generated for 100 meters (Meter ID: `00001` to `00100`), and only for a single day (from `00:00` to `23:45`).
2. Navigate to the `/samples` directory to find the newly generated meter data.

## What are meter channels?

An electricity meter takes readings from multiple channels at a pre-determined interval. Channels import interval data for a meter. Channel data can be used to generate chargeback bills. Interval data provides a more granular view of use and demand.

Each meter can have multiple channels to import different types of interval data. Think of channels on a meter as being similar to channels on a television. One channel for sports, one channel for the news, etc.

## Meter Data Schema

```javascript
{
  "type": String                  // Type of data being sent (default: "meterdata")
  "meter": {                      // Info as reported by the meter about itself
    "serial": String
    "version": Number
    "location": {
      "latitude": String
      "longitude": String
    }
    "configuration": {
      "readInterval": Number      // Reading interval (default: 15)
    }
  }
  "payload": {                    // Data payload (meter readings)
    "generatedAt": Date           // Time this data was generated
    "channels": [                 // Array of meter channels names being read
      {
        "name": String
      }
    ]
    "channelReadings": [          // Array of readings from each channel
      [                           // Array of the channel's readings at each interval
        {
          "timestamp": Date       // Timestamp of the reading (eg. 00:15 or 17:00)
          "value": String         // Channel reading at this interval
        }
      ]
    ]
  }
}
```

**More info:**
In this example, given a meter with 4 channels, there will also be 4 elements in the `channelReadings` array. Each element in `channelReadings` is an array, itself consisting of channel readings.

As such, values for `channels[0]` are located in `channelReadings[0]` or `channels[1]` are located in `channelReadings[1]` and so forth...
