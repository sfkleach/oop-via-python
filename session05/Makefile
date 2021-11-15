.PHONY: help
help:
	# Valid targets are
	#   clean - removes the demo files
	#   start - creates the demo files

.PHONY: start
start:
	cp range_extract_05_A.py range_extract.py
	sed 's/range_extract_05_A/range_extract/' < test_range_extract_05_A.py > test_range_extract.py
	cp knights_tour_05_A.py knights_tour.py
	sed 's/knights_tour_05_A/knights_tour/' < test_knights_tour_05_A.py > test_knights_tour.py

.PHONY: clean
clean:
	rm -f range_extract.py 
	rm -f test_range_extract.py
	rm -f knights_tour.py
	rm -f test_knights_tour.py
