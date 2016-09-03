
# building deployment directory

build: clean requirements copy tar

clean:
    rm -rf dist dist.tar.gz
    
requirements:
	pip freeze > requirements.txt

copy:
    mkdir dist
    cp -R cricinfo dist
    cp -R requirements.txt dist

tar:
    tar -zc dist/ | gzip > dist.tar.gz

.PHONY: build
