cat:
	cat Makefile

Image='tbutzer/yaml-python'

build:
	docker build -t ${Image} .


run:
	docker run -it -v `pwd`:/home/host ${Image} bash


test:
	python3 yaml2py.py


graph:
	#mkdir -p ./graph
	./pyan3 -c --dot ./code/demo.py | dot -Tsvg -o ./host/demo.svg
	./pyan3 -c --dot ./code/demo.py | dot -Tpng -o ./host/demo.png


demo:
	./pyan3 -c --dot ./code/demo.py


docker-login:
	docker login


docker-publish:
	docker push ${Image}
