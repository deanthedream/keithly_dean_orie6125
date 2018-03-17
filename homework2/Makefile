DIR := ${CURDIR}

.PHONY: clean

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +
	rm -rf env

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr htmlcov/

env:
	virtualenv --setuptools $@
	$@/bin/pip install -U "setuptools>=19,<20"
	$@/bin/pip install -U "pip>=7,<8"
	$@/bin/pip install -U "pip-tools==1.6.4"
	make env/.requirements

env/.requirements: requirements.txt requirements-test.txt | env
	$|/bin/pip-sync $^
	touch $@

requirements.txt requirements-test.txt: %.txt: %.in | env
	$|/bin/pip-compile --no-index $^

# To run a test
# make test ARG='-k test_location'
test: env/.requirements
	env/bin/py.test tests $(ARG)

script:
	coverage run -m unittest discover -v

cover:
	find ../../ -name "*flake8*"
	make lint #I am no longer calling make lint. It produces several errors that are actually necessary to run the programs
	make cover_tests
	mkdir -p coverage
	cp coverage.xml coverage/cobertura-coverage.xml


lint: env/.requirements
	#pwd
	#ls
	#ls ./env
	ls ./env/bin
	#env/bin/flake8 --max-line-length=100 tests
	flake8 --max-line-length=100 tests

cover_tests: env/.requirements
	#env/bin/py.test -s --tb short --cov-config .coveragerc --cov=homework2 --cov=findElement --cov=RBTree --cov=hybridSort --cov=binaryArray --cov-report term-missing --cov-report xml \
	--cov-report html \
	--junitxml junit.xml \
	--no-cov-on-fail \
	--cov-fail-under=85 \
	tests
	py.test -s --tb short --cov-config .coveragerc --cov=homework2 --cov=findElement --cov=RBTree --cov=hybridSort --cov=binaryArray --cov-report term-missing --cov-report xml \
	--cov-report html \
	--junitxml junit.xml \
	--no-cov-on-fail \
	--cov-fail-under=85 \
	tests
