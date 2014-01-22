clean:
	rm .virt/ -rf
	rm build -rf
	rm dist -rf
	rm *.egg-info -rf
	rm */*.pyc
develop:
	virtualenv .virt
	. .virt/bin/activate && pip install nose
	. .virt/bin/activate && pip install -e '.'
test: clean develop
	. .virt/bin/activate && nosetests tests
release: clean develop tests
	python setup.py sdist upload
