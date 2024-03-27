# Run from project root directory

ARG VERSION="0.0.1-SNAPSHOT"

FROM maven:3-eclipse-temurin-11 as builder

WORKDIR /usr/share/app
COPY pom.xml .

# Downloads all packages defined in pom.xml
RUN mvn clean package

COPY src src
RUN mvn clean package -Dmaven.test.skip=true

RUN ls /usr/share/app/target/

FROM eclipse-temurin:11-jre-focal

ARG VERSION
WORKDIR /usr/share/app
ENV JAR="ogc-resource-server-dev-${VERSION}-fat.jar"

# Copying openapi docs
COPY docs docs
# replace all instances of the server URL in OGC OpenAPI spec to the jenkins URL, since the OGC compliance
# tests actually parses the server URL in the OpenAPI spec
RUN sed -i 's|https://ogc.iudx.io|http://jenkins-slave1:8443|g' docs/openapiv3_0.json

# Copying dev fatjar from builder stage to final image
# Also copying the compiled class files to be able to generate the JaCoCo reports later on
COPY --from=builder /usr/share/app/target/${JAR} ./fatjar.jar
COPY --from=builder /usr/share/app/target/classes/ ./built-classes

# downloading JaCoCo JAR to run with the server JAR in javaagent mode
RUN wget https://repo1.maven.org/maven2/org/jacoco/jacoco/0.8.11/jacoco-0.8.11.zip -O /tmp/jacoco.zip
RUN apt update && apt install -y unzip && rm -rf /var/lib/apt/lists/*
RUN unzip /tmp/jacoco.zip -d /tmp/jacoco
RUN apt remove -y unzip && rm /tmp/jacoco.zip

EXPOSE 8080 8443
# Creating a non-root user
RUN useradd -r -u 1001 -g root ogc-user
# Setting non-root user to use when container starts
USER ogc-user
