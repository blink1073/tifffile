# Note: This is meant for tifffile developer use only
.PHONY: all clean test release update

export TEST_ARGS=--exe -v
export NAME=tifffile
export VERSION=`python -c "import $(NAME); print($(NAME).__version__)"`
export SITE=http://www.lfd.uci.edu/~gohlke/code/

all: clean
	python setup.py build_ext -i
	python setup.py install

clean:
	rm -rf build
	rm -rf dist
	find . -name "*.so" -o -name "*.pyc" | xargs rm -f

test: clean
	python setup.py build_ext -i
	export PYTHONWARNINGS="all"; nosetests $(TEST_ARGS)
	make clean

release: test
	pip install twine
	git tag v$(VERSION); true
	git commit -a -m "Release $(VERSION)"; true
	git push origin --all
	git push origin --tags
	rm -rf dist
	python setup.py register
	python setup.py sdist
	twine upload dist/*
	printf '\nUpgrade tifffile-feedstock with release and sha256 sum:'
	shasum -a 256 dist/*.tar.gz
