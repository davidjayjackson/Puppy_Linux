#!/usr/bin/gawk -f

BEGIN {
    FS="," # set the field separator to a comma
    OFS="," # set the output field separator to a comma
    print "Country,Date,Cases" # print the header row
}

# Keep a count of the cases for each country and date
{
    cases[$1][$2] += $3
}

END {
    # iterate over the countries and dates
    for (country in cases) {
        for (date in cases[country]) {
            # print the country, date, and case count
            print country, date, cases[country][date]
        }
    }
}

