#!/bin/sh
# docker run --rm -v /Users/wan/Work/bp/beproudbot:/beproudbot -it beproudbot_dev sh
docker run --rm -v `pwd`:/app -it beproudbot_dev sh
