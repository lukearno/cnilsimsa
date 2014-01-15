clean:
	rm .virt/ -rf
develop:
	virtualenv .virt
	. .virt/bin/activate && pip install nose
test: clean develop
	. .virt/bin/activate && nosetests tests
release: clean develop tests
	python setup.py sdist upload
