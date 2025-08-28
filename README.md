# Phone Number Analyzer

A Python script that analyzes phone numbers and extracts detailed information including carrier, location, timezone, and various formatting options.

## Disclaimer
This tool is for educational purposes only. Use responsibly and respect privacy laws in your jurisdiction.

## Features

- **Phone Number Validation**: Checks if the entered phone number is valid
- **Carrier Information**: Identifies the mobile carrier/network provider
- **Geographic Location**: Shows the region/country for the phone number
- **Timezone Detection**: Lists all possible timezones for the number
- **Multiple Formats**: Displays the number in E.164, International, and National formats
- **Additional Details**: Shows country code, national number, and extension (if any)

## Requirements

```bash
pip install phonenumbers
```

## Usage

1. Run the script:
```bash
python phone_analyzer.py
```

2. Enter a phone number with country code when prompted:
```
Enter phone number with country code (+xx xxxxxxxxx): +14155552671
```

3. The script will display comprehensive information about the phone number:
```
✅ Phone Number Details:
Timezone: ('America/Los_Angeles',)
Carrier: Verizon
Region: San Francisco, CA
Country Code: 1
National Number: 4155552671
E.164 Format: +14155552671
International Format: +1 415-555-2671
National Format: (415) 555-2671
Possible Number: True
Extension: None
```

## Input Format

The phone number must include the country code with a '+' prefix:
- ✅ Correct: `+14155552671` (US number)
- ✅ Correct: `+447700900123` (UK number)
- ✅ Correct: `+919876543210` (India number)
- ❌ Incorrect: `4155552671` (missing country code)
- ❌ Incorrect: `14155552671` (missing + prefix)

## Output Information

| Field | Description |
|-------|-------------|
| **Timezone** | All possible timezones for the phone number |
| **Carrier** | Mobile network operator (when available) |
| **Region** | Geographic location/city |
| **Country Code** | International dialing code |
| **National Number** | Phone number without country code |
| **E.164 Format** | Standard international format |
| **International Format** | Human-readable international format |
| **National Format** | Local format for the country |
| **Possible Number** | Whether the number format is possible |
| **Extension** | Phone extension if present |

## Error Handling

The script handles two main error scenarios:

1. **Invalid Number**: If the phone number is not valid for the given country
2. **Parse Error**: If the phone number format is incorrect (missing country code, wrong format, etc..)

## Dependencies

- `phonenumbers`: Google's libphonenumber library for Python
  - `phonenumbers.carrier`: Carrier identification
  - `phonenumbers.geocoder`: Geographic location
  - `phonenumbers.timezone`: Timezone information

## Notes

- Carrier information may not be available for all numbers
- Geographic information is based on the phone number's area code/prefix
- Some numbers may have multiple possible timezones
- The script works with mobile and landline numbers from all countries

## Privacy Notice

This tool only analyzes the structure and public information associated with phone numbers. It does not make any external API calls or store any data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.