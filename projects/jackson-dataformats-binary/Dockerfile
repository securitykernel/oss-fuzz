# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################

FROM gcr.io/oss-fuzz-base/base-builder-jvm
RUN apt-get update && apt-get install -y maven

ENV JACKSON_BRANCH=2.13

RUN git clone --depth 1 --branch=$JACKSON_BRANCH https://github.com/FasterXML/jackson-dataformats-binary
RUN git clone --depth 1 --branch=$JACKSON_BRANCH https://github.com/FasterXML/jackson-databind
RUN git clone --depth 1 --branch=$JACKSON_BRANCH https://github.com/FasterXML/jackson-core
RUN git clone --depth 1 --branch=$JACKSON_BRANCH https://github.com/FasterXML/jackson-annotations

COPY build.sh $SRC/
COPY CborFuzzer.java SmileFuzzer.java $SRC/
WORKDIR $SRC/
