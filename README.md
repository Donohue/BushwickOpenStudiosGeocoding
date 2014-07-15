Bushwick Open Studios Geocode Tools
==============

Clean Data
--------------
Every year we get a dump of completed listings for Bushwick Open Studios. More often than not there are a handful of listings that are missing addresses, or there are not currently locations for the addresses. Use the scripts in clean\_listings to get the unruly listing data into a list of unique Bushwick Open Studios location\_ids:

- Use output\_missing\_addresses.py to give that information back to the core organizers.
- Use output\_complete\_addresses.py to get the addresses that have been completed.
- Output of output\_complete\_addresses.py becomes the input for geocode\_and\_insert\_locations.py which creates a new location\_id and automatically geocodes it automatically. Be careful with this script. You should carefully review the output before executing the query (which is commented out by default).
- After running geocode\_and\_insert\_locations.py you should use the output of output\_complete\_addresses.py and run output\_complete\_locations.py
- output\_complete\_locations.py gives a list of unique location\_ids so we can number them properly.

Number Locations
--------------
Now that the hard part is done, we can run the final steps with the list of unique location\_ids:

- Manually remove any hub location\_ids from the list ascertained from the clean data, put these location\_ids in a separate list.
- Run detect\_zones.py which will output location\_id, BOS number, zone ID, latitude, and longitude with location\_ids, and save output to a file.
- Run detect\_zones.py again with only the hub location\_ids, and append the output to the same file.
- Manually open output file, and edit zone BOS numbers from numbers to letters.
- Double and triple check the output file
- Give the output file as input to update\_bos\_number.py which will write BOS numbers and zone IDs to the database.


