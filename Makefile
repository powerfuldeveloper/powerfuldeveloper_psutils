build-image:
	docker build -t $(slug):latest .
	docker run --rm  $(slug):latest make
