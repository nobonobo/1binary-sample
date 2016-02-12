DIST=$(PWD)/dist
VIRTUALENVCMD=virtualenv

.PHONY: all depends run test build release

all: depends build release

./env:
	$(VIRTUALENVCMD) ./env

depends: ./env
	env/bin/python src/setup.py develop

build:
	mkdir -p $(DIST)
	docker build --rm -t localhost/cent6py3 .
	docker create --name build-app localhost/cent6py3 && \
	docker cp build-app:/src/dist/app $(DIST)/ && docker rm build-app

run:
	./env/bin/python src/manage.py runserver

test:

release:
