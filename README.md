# ORM with Delta Air Lines historical data

Query output from `dal-history-db.py`:

``` bash
<Airline(name"American Airlines", IATA carrier code="AA">
<Airline(name"Alaska Airlines", IATA carrier code="AS">
<Airline(name"Delta Air Lines", IATA carrier code="DL">
<Airline(name"Spirit Airlines", IATA carrier code="NK">
<Airline(name"United Airlines", IATA carrier code="UA">
<Airline(name"Southwest Airlines", IATA carrier code="WN">
2021-02-15 15:49:39,433 INFO sqlalchemy.engine.base.Engine SELECT airline_history.events.id AS airline_history_events_id, airline_history.events.airline_id AS airline_history_events_airline_id, airline_history.events.year AS airline_history_events_year, airline_history.events.description AS airline_history_events_description
FROM airline_history.events ORDER BY airline_history.events.year
 LIMIT %(param_1)s
2021-02-15 15:49:39,434 INFO sqlalchemy.engine.base.Engine {'param_1': 5}
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
