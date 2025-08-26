import phonenumbers
from phonenumbers import carrier, geocoder, timezone, PhoneNumberFormat

mob = input("Enter phone number with country code (+xx xxxxxxxxx): ")

try:
    parsed_mob = phonenumbers.parse(mob)

    if phonenumbers.is_valid_number(parsed_mob):
        print("\nPhone Number Details:")

        # Timezone, Carrier, Region
        print("Timezone:", timezone.time_zones_for_number(parsed_mob))
        print("Carrier:", carrier.name_for_number(parsed_mob, "en"))
        print("Region:", geocoder.description_for_number(parsed_mob, "en"))

        # Country code and national number
        print("Country Code:", parsed_mob.country_code)
        print("National Number:", parsed_mob.national_number)

        # Formats
        print("E.164 Format:", phonenumbers.format_number(parsed_mob, PhoneNumberFormat.E164))
        print("International Format:", phonenumbers.format_number(parsed_mob, PhoneNumberFormat.INTERNATIONAL))
        print("National Format:", phonenumbers.format_number(parsed_mob, PhoneNumberFormat.NATIONAL))

        # Other checks
        print("Possible Number:", phonenumbers.is_possible_number(parsed_mob))
        print("Extension:", parsed_mob.extension if parsed_mob.extension else "None")

    else:
        print("Please enter a valid mobile number.")

except phonenumbers.NumberParseException:
    print("Invalid format! Use format like: +14155552671")
