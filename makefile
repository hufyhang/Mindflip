INDEX = index.html
COMPOSER = compose.py

default:
	python $(COMPOSER)

.PHONY: clean
clean:
	rm -f $(INDEX)

