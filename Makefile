# Note: This is meant for tifffile developer use only
.PHONY: all clean test release update

export TEST_ARGS=--exe -v
export NAME=tifffile
export VERSION=`python -c "import $(NAME); print($(NAME).__version__)"`

all: clean
	python setup.py build_ext -i
	python setup.py install

clean:
	rm -rf build
	rm -rf dist
	find . -name "*.pyc" -o -name "*.py,cover"| xargs rm -f

test: clean
	python setup.py build_ext -i
	export PYTHONWARNINGS="all"; nosetests $(TEST_ARGS)
	make clean

release: test
	python setup.py register
	python setup.py sdist --formats=gztar,zip upload
	git tag v$(VERSION)
	git push origin --all
	git push origin --tags

update: clean
	export SITE=http://www.lfd.uci.edu/~gohlke/code/
	wget $SITE/tifffile.py -o tifffile.py
	wget $SITE/tifffile.c -o tifffile.c
	make test
