
# building deployment directory

build: clean copy tar

clean:
    rm -rf dist dist.tar.gz

copy:
    mkdir dist
    cp -R bingo dist
    cp -R .crossbar dist
    cp requirements.txt dist
    cp crossbar-keyfile dist
    cp Makefile dist

tar:
    tar -zc dist/ | gzip > dist.tar.gz

.PHONY: build
