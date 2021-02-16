# ORM with Delta Air Lines historical data

Query output from `dal-history-db.py`:

``` bash
...
<Airline(name"American Airlines", id="3" IATA carrier code="AA">
<Airline(name"Alaska Airlines", id="5" IATA carrier code="AS">
<Airline(name"Delta Air Lines", id="1" IATA carrier code="DL">
<Airline(name"Spirit Airlines", id="6" IATA carrier code="NK">
<Airline(name"United Airlines", id="2" IATA carrier code="UA">
<Airline(name"Southwest Airlines", id="4" IATA carrier code="WN">
...
<Event(id="1" airline id="1" year="1925", description="Huff Daland Dusters, the predecessor of Delta, is founded in Macon, Ga., before moving to Monroe, La., a few months later. This was the first commercial agricultural flying company, and Huff Daland's 18 planes become the largest privately owned fleet in the world. Crop-dusting operations range from Florida to Arkansas, and west to California and Mexico. Later Huff Daland operates the first international mail and passenger route on the west coast of South America for Pan Am subsidiary Peruvian Airways. ">
<Event(id="2" airline id="1" year="1928", description="C.E. Woolman, the principal founder of what would become Delta Air Lines, leads movement to buy Huff Daland Dusters. Renamed Delta Air Service for the Mississippi Delta region it served, the new airline is incorporated on Dec. 3, 1928. D.Y. Smith, President; Woolman first Vice President. ">
<Event(id="3" airline id="1" year="1929", description="Delta operates its first passenger flight from Dallas, Texas, to Jackson, Miss., with stops in Shreveport and Monroe, La. Service soon expands to Birmingham and Tuscaloosa, Ala., and Meridian, Miss.">
<Event(id="4" airline id="1" year="1930", description="Service expands to Atlanta and Fort Worth. Delta does not receive mail contract from U.S. government; forcing suspension of passenger service. Company renamed Delta Air Corporation.">
<Event(id="5" airline id="1" year="1934", description="Delta receives Air Mail Route 24 from U.S. Post Office; resumes passenger service. Begins operating as Delta Air Lines.">
```

Sample SQL query:

``` mysql
mysql> SELECT airlines.iata_code, events.year, events.description FROM events INNER JOIN airlines WHERE airlines.id=events.airline_id AND events.year > 1930 AND events.year < 1945;
```

Output:

``` mysql
+-----------+------+----------------------------------------------------------------------------------------------------------------------------------+
| iata_code | year | description                                                                                                                      |
+-----------+------+----------------------------------------------------------------------------------------------------------------------------------+
| DL        | 1934 | Delta receives Air Mail Route 24 from U.S. Post Office; resumes passenger service. Begins operating as Delta Air Lines.          |
| DL        | 1935 | Delta offers first night service with the Stinson Model A; first Delta aircraft with two pilots.                                 |
| DL        | 1940 | Douglas DC-2 and DC-3 service introduced. Flight attendants, called "stewardesses," added to flight crews.                       |
| DL        | 1941 | Delta headquarters moves from Monroe, La., to Atlanta.                                                                           |
| DL        | 1942 | Delta contributes to the war effort. Modifies 1,000+ aircraft, over-hauls engines/instruments, trains Army pilots and mechanics. |
+-----------+------+----------------------------------------------------------------------------------------------------------------------------------+
5 rows in set (0.00 sec)
```

#### \*Source of Delta Air Lines historical data: https://news.delta.com/deltas-history-dusting-crops-connecting-world
